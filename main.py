import streamlit as st
from groq import Groq
from datetime import datetime

st.set_page_config(page_title="MasterAI B&W", page_icon="⚪", layout="wide")

DEVELOPER = "Jonathan Kristian Sergio Marut - Juan 15 tahun Maumere"
DEVELOPER_FULL = "AI ini dibuat oleh developer bernama Jonathan Kristian Sergio Marut! 15 tahun, SMAK St. Maria Monte Carmelo Maumere, panggilan Juan."

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error('Isi Secrets: GROQ_API_KEY = "gsk_..."')
    st.stop()

# ===== UI HITAM PUTIH ALIVE LIGHTING - KAYA CHATGPT TAPI DIBALIK! =====
st.markdown("""
<style>
/* BACKGROUND HITAM TOTAL */
.stApp {
    background: #000000 !important;
}

/* HILANGKAN HEADER STREAMLIT */
header {visibility: hidden !important;}

/* JUDUL PUTIH GLOWING ALIVE */
h1 {
    color: #FFFFFF !important;
    text-align: center !important;
    font-weight: 800 !important;
    letter-spacing: -1px !important;
    text-shadow: 0 0 20px rgba(255,255,255,0.8), 0 0 40px rgba(255,255,255,0.4) !important;
}

/* TEXT PUTIH SEMUA */
p, span, label, div {
    color: #FFFFFF !important;
}

/* DROPDOWN - PUTIH BACKGROUND, HITAM TULISAN + GLOWING PUTIH ALIVE */
div[data-testid="stSelectbox"] > div {
    background: #FFFFFF !important;
    border: 1px solid #FFFFFF !important;
    border-radius: 12px !important;
    box-shadow: 0 0 15px rgba(255,255,255,0.6), 0 0 30px rgba(255,255,255,0.3) !important;
    transition: all 0.3s ease !important;
}
div[data-testid="stSelectbox"] > div:hover {
    box-shadow: 0 0 25px rgba(255,255,255,0.9), 0 0 50px rgba(255,255,255,0.5) !important;
}
div[data-testid="stSelectbox"] div, div[data-testid="stSelectbox"] span, div[data-testid="stSelectbox"] p {
    color: #000000 !important;
    font-weight: 600 !important;
}

/* INFO BAR - PUTIH GLOWING */
.info-bar {
    background: #FFFFFF !important;
    color: #000000 !important;
    padding: 10px 16px !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    font-size: 13px !important;
    text-align: center !important;
    box-shadow: 0 0 20px rgba(255,255,255,0.7) !important;
    margin: 10px 0 !important;
}
.info-bar span { color: #000000 !important; }

/* CHAT MESSAGE - HITAM KEABU-ABUAN + BORDER PUTIH GLOW */
.stChatMessage {
    background: #111111 !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    border-radius: 16px !important;
    box-shadow: 0 0 10px rgba(255,255,255,0.1) !important;
}
.stChatMessage:hover {
    border: 1px solid rgba(255,255,255,0.4) !important;
    box-shadow: 0 0 20px rgba(255,255,255,0.2) !important;
}

/* CHAT INPUT - PUTIH + GLOW ALIVE */
div[data-testid="stChatInput"] {
    background: #FFFFFF !important;
    border-radius: 24px !important;
    border: 1px solid #FFFFFF !important;
    box-shadow: 0 0 20px rgba(255,255,255,0.6), inset 0 0 10px rgba(255,255,255,0.2) !important;
}
div[data-testid="stChatInput"] textarea {
    color: #000000 !important;
    font-weight: 500 !important;
}
div[data-testid="stChatInput"] button {
    background: #000000 !important;
    color: #FFFFFF !important;
    border-radius: 50% !important;
}

/* SIDEBAR HITAM */
section[data-testid="stSidebar"] {
    background: #000000 !important;
    border-right: 1px solid rgba(255,255,255,0.1) !important;
}

/* BUTTON */
button[kind="primary"] {
    background: #FFFFFF !important;
    color: #000000 !important;
    border: 1px solid #FFFFFF !important;
    box-shadow: 0 0 15px rgba(255,255,255,0.5) !important;
    font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("MasterAI")

# DROPDOWN - CUMA MODEL HIDUP, VISUAL TETEP BAGUS!
model_pilihan = st.selectbox(
    "Model",
    [
        "openai/gpt-oss-120b - GPT-OSS 120B PALING PINTER 🚀",
        "openai/gpt-oss-20b - GPT-OSS 20B SUPER CEPAT ⚡",
        "openai/gpt-oss-safeguard-20b - VERSI AMAN 🛡️"
    ],
    label_visibility="collapsed"
)

kode_model = model_pilihan.split(" - ")[0].strip()

st.markdown(f"<div style='text-align:center; color:#FFF; font-weight:600; letter-spacing:1px; margin:5px 0;'>DIBUAT OLEH {DEVELOPER.upper()} 💻</div>", unsafe_allow_html=True)
st.markdown(f"<div class='info-bar'><span>⚪ Model aktif: {kode_model} | {datetime.now().strftime('%d %B %Y')} | WHITE GLOW ALIVE</span></div>", unsafe_allow_html=True)

if "msgs" not in st.session_state:
    st.session_state.msgs = []

for m in st.session_state.msgs:
    with st.chat_message(m["role"], avatar="⚪" if m["role"]=="user" else "⬛"):
        st.write(m["content"])

q = st.chat_input(f"Tanya ke MasterAI...")

if q:
    st.session_state.msgs.append({"role": "user", "content": q})
    with st.chat_message("user", avatar="⚪"):
        st.write(q)
    with st.chat_message("assistant", avatar="⬛"):
        try:
            if any(k in q.lower() for k in ["siapa pembuat", "siapa yang membuat"]):
                ans = f"{DEVELOPER_FULL} ⚪⬛"
            else:
                resp = client.chat.completions.create(
                    model=kode_model,
                    messages=[
                        {"role": "system", "content": f"Kamu MasterAI hitam putih, buatan {DEVELOPER_FULL}. Hari ini {datetime.now().strftime('%d %B %Y')} 2026."},
                        {"role": "user", "content": q}
                    ],
                    max_tokens=1500
                )
                ans = resp.choices[0].message.content
            st.write(ans)
            st.session_state.msgs.append({"role": "assistant", "content": ans})
        except Exception as e:
            st.error(f"Error: {e}")
