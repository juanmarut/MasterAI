import streamlit as st
from groq import Groq
from datetime import datetime
import uuid
import time

st.set_page_config(page_title="MasterAI - Groq Edition 2026", page_icon="⚡", layout="wide")

# ===== CONFIG DEVELOPER - ANTI BAJAK =====
DEVELOPER_INFO = "AI ini dibuat oleh developer bernama Jonathan Kristian Sergio Marut! Dia ADALAH seorang anak yang masih berumur 15 tahun, tetapi sudah mampu membuat AI seperti ku. Dia adalah seorang pelajar di SMAK St. Maria Monte Carmelo Maumere, dan Ia biasanya dipanggil Juan."

# ===== AMBIL GROQ API KEY YANG BENAR =====
try:
    # Key harus tanpa spasi! Pakai GROQ_API_KEY
    if "GROQ_API_KEY" in st.secrets:
        GROQ_KEY = st.secrets["GROQ_API_KEY"]
    elif "GROQ_API" in st.secrets:
        GROQ_KEY = st.secrets["GROQ_API"]
    else:
        st.error("❌ GROQ API Key belum ada!")
        st.code('GROQ_API_KEY = "gsk_..."', language="toml")
        st.info("Masuk ke Streamlit Cloud > Settings > Secrets > isi kayak di atas")
        st.stop()
    
    client = Groq(api_key=GROQ_KEY)

except Exception as e:
    st.error(f"❌ Error API Key Groq: {e} 🗿")
    st.stop()

# ===== SEARCH 2026 - BIAR GAK JAWAB 2024 LAGI =====
def search_2026(query):
    try:
        from duckduckgo_search import DDGS
        results = ""
        with DDGS() as ddgs:
            data = list(ddgs.text(f"{query} latest news 2026", max_results=5))
            for i, r in enumerate(data, 1):
                results += f"{i}. {r['title']}: {r['body']} ({r['href']})\n"
        return results
    except:
        return ""

def need_search(q):
    keys = ["apakah benar", "sudah wafat", "berita", "hari ini", "terbaru", "2025", "2026", "sekarang", "harga", "el mencho", "presiden", "skor"]
    return any(k in q.lower() for k in keys)

# ===== UI =====
st.markdown("""
<style>
.stApp { background: #0A0A12 !important; }
h1 { text-align: center !important; }
section[data-testid="stSidebar"] { background: #12121E !important; }
.stChatMessage { background: #181828 !important; border-radius: 16px !important; max-width: 720px !important; margin: 10px auto !important; }
</style>
""", unsafe_allow_html=True)

st.title("MasterAI 🤖")
st.markdown(f"**DIBUAT OLEH DEVELOPER JONATHAN KRISTIAN SERGIO MARUT** 💻🔥")
st.markdown(f"<div style='text-align:center; color:#00F5FF; font-size:12px;'>🌐 {datetime.now().strftime('%d %B %Y')} | Groq Llama 3.3 + Google Search 2026 | RAM Friendly 2GB</div>", unsafe_allow_html=True)
st.divider()

# History
if "chats" not in st.session_state:
    fid = str(uuid.uuid4())
    st.session_state.chats = {fid: {"title": "Ngobrol Baru", "messages": [], "created": time.time()}}
    st.session_state.active
