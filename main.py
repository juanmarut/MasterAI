import streamlit as st
from groq import Groq
from datetime import datetime
import time, uuid

st.set_page_config(page_title="MasterAI White", page_icon="⚫", layout="wide")

DEVELOPER = "Jonathan Kristian Sergio Marut - Juan Maumere"
DEVELOPER_FULL = "AI ini dibuat oleh Jonathan Kristian Sergio Marut! 15 tahun, SMAK Monte Carmelo Maumere"

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error('Isi Secrets: GROQ_API_KEY = "gsk_..."')
    st.stop()

st.markdown("""
<style>
.stApp { background: #FFFFFF !important; }
header, footer {visibility: hidden !important;}
h1 { color: #000000 !important; text-align: center !important; font-weight: 900 !important; text-shadow: 0 0 20px rgba(0,0,0,0.2) !important; }
p, span, label, div { color: #000000 !important; }
section[data-testid="stSidebar"] { background: #FFFFFF !important; border-right: 2px solid #000 !important; }
div[data-testid="stSelectbox"] > div { background: #000000 !important; border-radius: 12px !important; box-shadow: 0 0 15px rgba(0,0,0,0.4) !important; }
div[data-testid="stSelectbox"] span, div[data-testid="stSelectbox"] p, div[data-testid="stSelectbox"] div { color: #FFFFFF !important; font-weight: 600 !important; }
div[data-testid="stSelectbox"] svg { fill: #FFFFFF !important; }
.stChatMessage { background: #F5F5F5 !important; border: 1.5px solid #000 !important; border-radius: 16px !important; }
div[data-testid="stChatInput"] { background: #000000 !important; border-radius: 28px !important; box-shadow: 0 0 20px rgba(0,0,0,0.3) !important; }
div[data-testid="stChatInput"] textarea { color: #FFFFFF !important; }
div[data-testid="stChatInput"] textarea::placeholder { color: #888 !important; }
div[data-testid="stChatInput"] button { background: #FFF !important; color: #000 !important; border-radius: 50% !important; }
.stButton > button { background: #000 !important; color: #FFF !important; border-radius: 10px !important; font-weight: 700 !important; width: 100% !important; }
</style>
""", unsafe_allow_html=True)

if "chats" not in st.session_state:
    fid = str(uuid.uuid4())
    st.session_state.chats = {fid: {"title": "Ngobrol Baru", "messages": [], "created": time.time()}}
    st.session_state.active_chat = fid

with st.sidebar:
    st.markdown("### ⬛ MasterAI")
    st.write(DEVELOPER)
    if st.button("➕ Chat Baru"):
        nid = str(uuid.uuid4())
        st.session_state.chats[nid] = {"title": "Ngobrol Baru", "messages": [], "created": time.time()}
        st.session_state.active_chat = nid
        st.rerun()
    st.divider()
    st.write("📜 Riwayat")
    for cid, cdata in list(st.session_state.chats.items())[::-1]:
        if st.button(f"💬 {cdata['title'][:18]}", key=f"ch_{cid}"):
            st.session_state.active_chat = cid
            st.rerun()

active = st.session_state.chats[st.session_state.active_chat]

st.title("MasterAI")
st.markdown(f"<div style='text-align:center; font-weight:700;'>DIBUAT OLEH {DEVELOPER.upper()} 💻</div>", unsafe_allow_html=True)

model_pilihan = st.selectbox("Model", ["openai/gpt-oss-120b - GPT-OSS 120B PALING PINTER 🚀", "openai/gpt-oss-20b - GPT-OSS 20B CEPAT ⚡", "openai/gpt-oss-safeguard-20b - VERSI AMAN 🛡️"], label_visibility="collapsed")
kode_model = model_pilihan.split(" - ")[0].strip()

st.markdown(f"<div style='background:#000; color:#FFF; padding:10px; border-radius:10px; text-align:center; font-weight:700; box-shadow:0 0 20px rgba(0,0,0,0.3);'>⬛ {kode_model} | {datetime.now().strftime('%d %B %Y')}</div>", unsafe_allow_html=True)

for m in active["messages"]:
    with st.chat_message(m["role"]):
        st.write(m["content"])

q = st.chat_input(f"Tanya ke {kode_model}")

if q:
    if len(active["messages"]) == 0:
        active["title"] = q[:20]
    active["messages"].append({"role": "user", "content": q})
    with st.chat_message("user"):
        st.write(q)
    with st.chat_message("assistant"):
        try:
            if "siapa pembuat" in q.lower() or "siapa yang membuat" in q.lower():
                ans = DEVELOPER_FULL + " 🔥"
            else:
                r = client.chat.completions.create(model=kode_model, messages=[{"role": "system", "content": f"Kamu MasterAI buatan {DEVELOPER_FULL}. Hari ini 2026."}, {"role": "user", "content": q}], max_tokens=1500)
                ans = r.choices[0].message.content
            st.write(ans)
            active["messages"].append({"role": "assistant", "content": ans})
        except Exception as e:
            st.error(f"Error: {e}")
