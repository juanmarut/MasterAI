import streamlit as st
from groq import Groq
from datetime import datetime
# ===== CONFIG =====
st.set_page_config(page_title="MasterAI", page_icon="⚫", layout="wide", initial_sidebar_state="expanded")

DEVELOPER = "Jonathan Kristian Sergio Marut - Juan 15 tahun Maumere"
DEVELOPER_FULL = "AI ini dibuat oleh developer bernama Jonathan Kristian Sergio Marut! 15 tahun, SMAK St. Maria Monte Carmelo Maumere, panggilan Juan."

try:
    GROQ_KEY = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=GROQ_KEY)
except:
    st.error('❌ Belum ada GROQ_API_KEY di Secrets! Masuk ke Settings -> Secrets -> isi: GROQ_API_KEY = "gsk_..."')
    st.stop()

# ===== UI FULL WHITE BACKGROUND, BLACK OPSI & TULISAN + BLACK GLOW ALIVE =====
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
.stApp { background: #FFFFFF !important; font-family: 'Inter', sans-serif !important; }
header {visibility: hidden !important;}
footer {visibility: hidden !important;}

h1 { color: #000000 !important; text-align: center !important; font-weight: 900 !important; font-size: 2.5rem !important; text-shadow: 0 0 20px rgba(0,0,0,0.2) !important; }
h2, h3 { color: #000000 !important; }
p, span, label, div { color: #000000 !important; }

/* SIDEBAR PUTIH */
section[data-testid="stSidebar"] { background: #FFFFFF !important; border-right: 2px solid #000000 !important; }
section[data-testid="stSidebar"] * { color: #000000 !important; }

/* DROPDOWN HITAM + GLOW */
div[data-testid="stSelectbox"] > div {
    background: #000000 !important; border: 1px solid #000000 !important; border-radius: 12px !important;
    box-shadow: 0 0 15px rgba(0,0,0,0.4), 0 0 30px rgba(0,0,0,0.15) !important;
    transition: all 0.3s ease !important; min-height: 50px !important;
}
div[data-testid="stSelectbox"] > div:hover { box-shadow: 0 0 25px rgba(0,0,0,0.7), 0 0 50px rgba(0,0,0,0.3) !important; }
div[data-testid="stSelectbox"] div, div[data-testid="stSelectbox"] span, div[data-testid="stSelectbox"] p { color: #FFFFFF !important; font-weight: 600 !important; font-size: 14px !important; }
div[data-testid="stSelectbox"] svg { fill: #FFFFFF !important; }

/* INFO BAR HITAM GLOW */
.info-bar {
    background: #000000 !important; color: #FFFFFF !important; padding: 12px 18px !important;
    border-radius: 12px !important; font-weight: 700 !important; font-size: 13px !important;
    text-align: center !important; box-shadow: 0 0 20px rgba(0,0,0,0.4) !important; margin: 12px 0 !important;
    letter-spacing: 0.5px !important;
}
.info-bar span { color: #FFFFFF !important; }

/* CHAT BUBBLE */
.stChatMessage { background: #F8F8F8 !important; border: 1.5px solid #000000 !important; border-radius: 16px !important; box-shadow: 0 2px 10px rgba(0,0,0,0.08) !important; margin-bottom: 10px !important; }
.stChatMessage:hover { box-shadow: 0 4px 20px rgba(0,0,0,0.15) !important; }
.stChatMessage p { color: #000000 !important; font-size: 15px !important; line-height: 1.6 !important; }

/* CHAT INPUT HITAM GLOW */
div[data-testid="stChatInput"] {
    background: #000000 !important; border-radius: 28px !important; border: 2px solid #000000 !important;
    box-shadow: 0 0 25px rgba(0,0,0,0.3) !important; padding: 4px !important;
}
div[data-testid="stChatInput"] textarea { color: #FFFFFF !important; font-weight: 500 !important; font-size: 15px !important; }
div[data-testid="stChatInput"] textarea::placeholder { color: #888888 !important; }
div[data-testid="stChatInput"] button { background: #FFFFFF !important; color: #000000 !important; border-radius: 50% !important; width: 36px !important; height: 36px !important; }

/* BUTTON */
.stButton > button { background: #000000 !important; color: #FFFFFF !important; border-radius: 10px !important; font-weight: 700 !important; border: 1.5px solid #000000 !important; box-shadow: 0 0 15px rgba(0,0,0,0.2) !important; transition: all 0.2s !important; width: 100% !important; }
.stButton > button:hover { background: #FFFFFF !important; color: #000000 !important; box-shadow: 0 0 25px rgba(0,0,0,0.4) !important; transform: translateY(-1px) !important; }

/* CHAT HISTORY BUTTON */
.chat-history-btn { background: #FFFFFF !important; border: 1.5px solid #000000 !important; border-radius: 10px !important; padding: 10px !important; margin: 5px 0 !important; }
</style>
""", unsafe_allow_html=True)

# ===== SESSION STATE CHAT HISTORY =====
if "chats" not in st.session_state:
    first_id = str(uuid.uuid4())
    st.session_state.chats = {first_id: {"title": "Ngobrol Baru ✨", "messages": [], "created": time.time()}}
    st.session_state.active_chat = first_id

def get_active_chat():
   
