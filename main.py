import streamlit as st
from groq import Groq
from datetime import datetime
import time, uuid

st.set_page_config(page_title="MasterAI", page_icon="⚫", layout="wide")

DEVELOPER = "Jonathan Kristian Sergio Marut - Juan Maumere"
DEVELOPER_FULL = "AI ini dibuat oleh Jonathan Kristian Sergio Marut! 15 tahun, SMAK Monte Carmelo Maumere"

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error('Isi Secrets: GROQ_API_KEY = "gsk_..."')
    st.stop()

# ===== FIX KONTRAST TINGGI =====
st.markdown("""
<style>
.stApp { background: #FFFFFF !important; }
header, footer {visibility: hidden !important;}

/* JUDUL HITAM PEKAT KONTRAST */
h1 { color: #000000 !important; text-align: center !important; font-weight: 900 !important; font-size: 42px !important; letter-spacing: -1px !important; }

/* SEMUA TEXT HITAM PEKAT */
p, span, label, div { color: #000000 !important; }

/* SIDEBAR */
section[data-testid="stSidebar"] { background: #FFFFFF !important; border-right: 3px solid #000000 !important; }

/* DROPDOWN - KONTRAST TINGGI BANGET */
div[data-testid="stSelectbox"] > div {
    background: #000000 !important;
    border: 3px solid #000000 !important;
    border-radius: 14px !important;
    min-height: 60px !important;
    box-shadow: 0 0 0 3px #FFFFFF, 0 0 0 6px #000000, 0 8px 25px rgba(0,0,0,0.3) !important;
}
div[data-testid="stSelectbox"] span, div[data-testid="stSelectbox"] p, div[data-testid="stSelectbox"] div {
    color: #FFFFFF !important;
    font-weight: 900 !important;
    font-size: 16px !important;
    letter-spacing: 0.5px !important;
    text-transform: uppercase !important;
}
div[data-testid="stSelectbox"] svg { fill: #FFFFFF !important; width: 24px !important; height: 24px !important; }

/* INFO BAR KONTRAST */
.info-bar {
    background: #000000 !important;
    border: 2px solid #000000 !important;
    padding: 14px !important;
    border-radius: 12px !important;
    text-align: center !important;
    margin: 12px 0 !important;
}
.info-bar span {
    color: #FFFFFF !important;
    font-weight: 800 !important;
    font-size: 14px !important;
    letter-spacing: 1px !important;
}

/* CHAT BUBBLE KONTRAST */
.stChatMessage { background: #FFFFFF !important; border: 2.5px solid #000000 !important; border-radius: 16px !important; box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important; }
.stChatMessage p { color: #000000 !important; font-weight: 500 !important; font-size: 16px !important; }

/* CHAT INPUT KONTRAST */
div[data-testid="stChatInput"] {
    background: #000000 !important;
    border: 3px solid #000000 !important;
    border-radius: 30px !important;
    min-height: 60px !important;
    box-shadow: 0 0 0 3px #FFFFFF, 0 0 0 6px #000000 !important;
}
div[data-testid="stChatInput"] textarea { color: #FFFFFF !important; font-weight: 700 !important; font-size: 16px !important; }
div[data-testid="stChatInput"] textarea::placeholder { color: #CCCCCC !important; font-weight: 600 !important; }
div[data-testid="stChatInput"] button { background: #FFFFFF !important; color: #000000 !important; border-radius: 50% !important; width: 40px !important; height: 40px !important; font-weight: 900 !important; }

.stButton > button { background: #000000 !important; color: #FFFFFF !important; border-radius: 12px !important; font-weight: 800 !important; font-size: 15px !important; border: 2px solid #000 !important; min-height: 50px !important; }
</style>
""", unsafe_allow_html=True)

if "chats" not in st.session_state:
    fid = str(uuid.uuid4())
    st.session_state.chats = {fid: {"title": "Ngobrol Baru", "messages": [], "created": time.time()}}
    st.session_state.active_chat = fid

with st.sidebar:
    st.markdown("### ⬛ MasterAI")
    st.markdown(f"<b style='color:#000; font-size:14px;'>{DEVELOPER}</b>", unsafe_allow_html=True)
    if st.button("➕ CHAT BARU", use_container_width=True):
        nid = str(uuid.uuid4())
        st.session_state.chats[nid] = {"title": "Ngobrol Baru", "messages": [], "created": time.time()}
        st.session_state.active_chat = nid
        st.rerun()
    st.divider()
    st.markdown("<b>📜 Riwayat</b>", unsafe_allow_html=True)
    for cid, cdata in list(st.session_state.chats.items())[::-1]:
        if st.button(f"💬 {cdata['title'][:20]}", key=f"ch_{cid}", use_container_width=True):
            st.session_state.active_chat = cid
            st.rerun()

active = st.session_state.chats[st.session_state.active_chat]

st.title("MasterAI")
st.markdown(f"<div style='text-align:center; font-weight:900; font-size:13px; letter-spacing:1.5px; color:#000; background:#FFF; border:2px solid #000; padding:8px; border-radius:8px;'>DIBUAT OLEH {DEVELOPER.upper()} 💻</div>", unsafe_allow_html=True)

model_pilihan = st.selectbox("Model", ["openai/gpt-oss-120b - GPT-OSS 120B PALING PINTER 🚀", "openai/gpt-oss-20b - GPT-OSS 20B SUPER CEPAT ⚡", "openai/gpt-oss-safeguard-20b - VERSI AMAN 🛡️"], label_visibility="collapsed")
kode_model = model_pilihan.split(" - ")[0].strip()

st.markdown(f"<div class='info-bar'><span>⬛ MODEL: {kode_model} | {datetime.now().strftime('%d %B %Y')} | KONTRAST TINGGI ⚫⚪</span></div>", unsafe_allow_html=True)

for m in active["messages"]:
    with st.chat_message(m["role"]):
        st.write(m["content"])

q = st.chat_input(f"Ketik pertanyaan ke {kode_model}...")

if q:
    if len(active["messages"]) == 0:
        active["title"] = q[:20]
    active["messages"].append({"role": "user", "content": q})
    with st.chat_message("user"):
        st.write(q)
    with st.chat_message("assistant"):
        try:
            if "siapa pembuat" in q.lower():
                ans = DEVELOPER_FULL
            else:
                r = client.chat.completions.create(model=kode_model, messages=[{"role": "system", "content": f"Kamu MasterAI buatan {DEVELOPER_FULL}"}, {"role": "user", "content": q}], max_tokens=1500)
                ans = r.choices[0].message.content
            st.write(ans)
            active["messages"].append({"role": "assistant", "content": ans})
        except Exception as e:
            st.error(f"Error: {e}")
