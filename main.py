import streamlit as st
from groq import Groq
from datetime import datetime

st.set_page_config(page_title="MasterAI White", page_icon="⚫", layout="wide")

DEVELOPER = "Jonathan Kristian Sergio Marut - Juan 15 tahun Maumere"
DEVELOPER_FULL = "AI ini dibuat oleh developer bernama Jonathan Kristian Sergio Marut! 15 tahun, SMAK St. Maria Monte Carmelo Maumere, panggilan Juan."

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error('Isi Secrets: GROQ_API_KEY = "gsk_..."')
    st.stop()

# ===== UI PUTIH HITAM - BACKGROUND PUTIH, OPSI & TULISAN HITAM + BLACK GLOW ALIVE =====
st.markdown("""
<style>
/* BACKGROUND PUTIH TOTAL - KEBALIKAN TADI */
.stApp {
    background: #FFFFFF !important;
}
header {visibility: hidden !important;}

/* JUDUL HITAM GLOWING ALIVE */
h1 {
    color: #000000 !important;
    text-align: center !important;
    font-weight: 900 !important;
    letter-spacing: -1px !important;
    text-shadow: 0 0 20px rgba(0,0,0,0.3), 0 0 40px rgba(0,0,0,0.15) !important;
}

/* SEMUA TEXT HITAM */
p, span, label, div {
    color: #000000 !important;
}

/* DROPDOWN - HITAM BACKGROUND, PUTIH TULISAN + GLOWING HITAM ALIVE */
div[data-testid="stSelectbox"] > div {
    background: #000000 !important;
    border: 1px solid #000000 !important;
    border-radius: 12px !important;
    box-shadow: 0 0 15px rgba(0,0,0,0.5), 0 0 30px rgba(0,0,0,0.2) !important;
    transition: all 0.3s ease !important;
}
div[data-testid="stSelectbox"] > div:hover {
    box-shadow: 0 0 25px rgba(0,0,0,0.8), 0 0 50px rgba(0,0,0,0.4) !important;
}
div[data-testid="stSelectbox"] div, div[data-testid="stSelectbox"] span, div[data-testid="stSelectbox"] p {
    color: #FFFFFF !important;
   
