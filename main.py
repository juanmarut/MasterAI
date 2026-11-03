import streamlit as st
from groq import Groq
from datetime import datetime
import time, uuid

st.set_page_config(page_title="MasterAI", page_icon="⚫", layout="wide", initial_sidebar_state="collapsed")

DEVELOPER = "Jonathan Kristian Sergio Marut - Juan Maumere"
DEVELOPER_FULL = "AI ini dibuat oleh Jonathan Kristian Sergio Marut! 15 tahun, SMAK Monte Carmelo Maumere"

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error('Isi Secrets: GROQ_API_KEY = "gsk_..."')
    st.stop()

# ===== UI KONTRAST TINGGI + RESPONSIVE HP + ANIMASI =====
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;700;900&display=swap');
.stApp { background: #FFFFFF !important; font-family: 'Inter', sans-serif !important; }
header {visibility: hidden !important;} footer {visibility: hidden !important;}

/* SIDEBAR BISA DIGESER KAYAK CHATGPT - ANIMASI SLIDE */
section[data-testid="stSidebar"] {
    background: #FFFFFF !important;
    border-right: 3px solid #000000 !important;
    box-shadow: 5px 0 25px rgba(0,0,0,0.15) !important;
    transition: all 0.3s ease-in-out !important;
    width: 280px !important;
}
section[data-testid="stSidebar"] .block-container { padding-top: 20px !important; }

/* TOMBOL SIDEBAR DI HP */
button[kind="header"] { background: #000 !important; color: #FFF !important; border-radius: 10px !important; }

h1 { color: #000 !important; text-align: center !important; font-weight: 900 !important; font-size: 38px !important; }

/* DROPDOWN KONTRAST */
div[data-testid="stSelectbox"] > div {
    background: #000 !important; border-radius: 14px !important; min-height: 60px !important;
    box-shadow: 0 0 0 3px #FFF, 0 0 0 6px #000 !important;
}
div[data-testid="stSelectbox"] span, div[data-testid="stSelectbox"] p, div[data-testid="stSelectbox"] div {
    color: #FFF !important; font-weight: 900 !important; font-size: 15px !important;
}
div[data-testid="stSelectbox"] svg { fill: #FFF !important; }

/* INFO BAR */
.info-bar { background: #000 !important; padding: 12px !important; border-radius: 12px !important; text-align: center !important; }
.info-bar span { color: #FFF !important; font-weight: 800 !important; font-size: 13px !important; }

/* CHAT BUBBLE */
.stChatMessage { background: #FFF !important; border: 2.5px solid #000 !important; border-radius: 18px !important; box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important; }
.stChatMessage p { color: #000 !important; font-size: 16px !important; line-height: 1.6 !important; }

/* CURSOR KEDIP ANIMASI MENGETIK */
.typing-cursor::after {
    content: '▌';
    animation: blink 1s infinite;
    color: #000;
    font-weight: 900;
    margin-left: 2px;
}
@keyframes blink { 0%, 50% { opacity: 1; } 51%, 100% { opacity: 0; } }

/* CHAT INPUT HP FRIENDLY */
div[data-testid="stChatInput"] {
    background: #000 !important; border-radius: 30px !important; min-height: 60px !important;
    box-shadow: 0 0 0 3px #FFF, 0 0 0 6px #000 !important;
    position: sticky !important; bottom: 20px !important;
}
div[data-testid="stChatInput"] textarea { color: #FFF !important; font-weight: 700 !important; font-size: 16px !important; }
div[data-testid="stChatInput"] textarea::placeholder { color: #AAA !important; }
div[data-testid="stChatInput"] button { background: #FFF !important; color: #000 !important; border-radius: 50% !important; width: 42px !important; height: 42px !important; }

.stButton > button { background: #000 !important; color: #FFF !important; border-radius: 12px !important; font-weight: 800 !important; min-height: 50px !important; border: 2px solid #000 !important; }

/* HP RESPONSIVE */
@media (max-width: 768px) {
    h1 { font-size: 28px !important; }
    section[data-testid="stSidebar"] { width: 85% !important; }
    div[data-testid="stSelectbox"] span { font-size: 13px !important; }
    .stChatMessage { margin: 8px 0 !important; }
}
</style>
""", unsafe_allow_html=True)

if "chats" not in st.session_state:
    fid = str(uuid.uuid4())
    st.session_state.chats = {fid: {"title": "Ngobrol Baru", "messages": [], "created": time.time()}}
    st.session_state.active_chat = fid

with st.sidebar:
    st.markdown("### ⬛ MasterAI")
    st.markdown(f"<b style='font-size:13px; color:#000;'>{DEVELOPER}</b>", unsafe_allow_html=True)
    st.write("")
    if st.button("➕ CHAT BARU", use_container_width=True):
        nid = str(uuid.uuid4())
        st.session_state.chats[nid] = {"title": "Ngobrol Baru", "messages": [], "created": time.time()}
        st.session_state.active_chat = nid
        st.rerun()
    st.divider()
    st.markdown("**📜 Riwayat**")
    for cid, cdata in sorted(st.session_state.chats.items(), key=lambda x: x[1]['created'], reverse=True):
        col1, col2 = st.columns([4,1])
        with col1:
            label = f"{'▶️ ' if cid==st.session_state.active_chat else '💬 '}{cdata['title'][:18]}"
            if st.button(label, key=f"ch_{cid}", use_container_width=True):
                st.session_state.active_chat = cid
                st.rerun()
        with col2:
            if st.button("✕", key=f"del_{cid}"):
                if len(st.session_state.chats) > 1:
                    del st.session_state.chats[cid]
                    st.session_state.active_chat = list(st.session_state.chats.keys())[0]
                    st.rerun()
    st.divider()
    st.markdown(f"<div style='font-size:11px; text-align:center; color:#000;'>⚫ Geser sidebar untuk tutup/buka<br/>Kayak ChatGPT asli! 📱</div>", unsafe_allow_html=True)

active = st.session_state.chats[st.session_state.active_chat]

st.title("MasterAI")
st.markdown(f"<div style='text-align:center; font-weight:900; font-size:12px; border:2px solid #000; padding:8px; border-radius:8px; letter-spacing:1px;'>DIBUAT OLEH {DEVELOPER.upper()} 💻</div>", unsafe_allow_html=True)

model_pilihan = st.selectbox("Model", ["openai/gpt-oss-120b - GPT-OSS 120B PALING PINTER 🚀", "openai/gpt-oss-20b - GPT-OSS 20B SUPER CEPAT ⚡", "openai/gpt-oss-safeguard-20b - VERSI AMAN 🛡️"], label_visibility="collapsed")
kode_model = model_pilihan.split(" - ")[0].strip()
st.markdown(f"<div class='info-bar'><span>⬛ {kode_model} | {datetime.now().strftime('%d %B %Y')}</span></div>", unsafe_allow_html=True)

for m in active["messages"]:
    with st.chat_message(m["role"]):
        st.write(m["content"])

q = st.chat_input(f"Tanya ke {kode_model}...")

# ===== ANIMASI MENGETIK =====
def type_writer(text, placeholder):
    full = ""
    for char in text:
        full += char
        placeholder.markdown(f"{full}<span class='typing-cursor'></span>")
        time.sleep(0.015)
    placeholder.markdown(full)
    return full

if q:
    if len(active["messages"]) == 0:
        active["title"] = q[:20]
    active["messages"].append({"role": "user", "content": q})
    with st.chat_message("user"):
        st.write(q)
    
    with st.chat_message("assistant"):
        msg_placeholder = st.empty()
        try:
            if "siapa pembuat" in q.lower():
                ans = DEVELOPER_FULL + " 🔥"
                type_writer(ans, msg_placeholder)
            else:
                # STREAMING + ANIMASI MENGETIK
                stream = client.chat.completions.create(
                    model=kode_model,
                    messages=[{"role": "system", "content": f"Kamu MasterAI buatan {DEVELOPER_FULL}. Jawab singkat, jelas, gaul."}, *active["messages"][-6:]],
                    max_tokens=2000,
                    stream=True
                )
                full_text = ""
                for chunk in stream:
                    delta = chunk.choices[0].delta.content
                    if delta:
                        full_text += delta
                        msg_placeholder.markdown(f"{full_text}<span class='typing-cursor'></span>")
                        time.sleep(0.01)
                msg_placeholder.markdown(full_text)
                ans = full_text
            
            active["messages"].append({"role": "assistant", "content": ans})
        except Exception as e:
            st.error(f"Error: {e}")
