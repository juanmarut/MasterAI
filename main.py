import streamlit as st
from groq import Groq
from datetime import datetime

st.set_page_config(page_title="MasterAI 2026 FIXED", page_icon="⚡", layout="wide")

DEVELOPER = "Jonathan Kristian Sergio Marut - Juan 15 tahun Maumere"

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error('Isi Secrets: GROQ_API_KEY = "gsk_..."')
    st.stop()

# ===== STYLE BIAR VISUAL TETEP BAGUS KAYAK PUNYA LU =====
st.markdown("""
<style>
.stApp { background: #0A0A12 !important; }
div[data-testid="stSelectbox"] { background: #1E1E32 !important; border-radius: 12px !important; }
</style>
""", unsafe_allow_html=True)

st.title("MasterAI 🤖")

# ===== DROPDOWN VISUAL LU GUE PERTAHANIN! JANGAN HAPUS! =====
model_pilihan = st.selectbox(
    "qwen-2.5-32b - PINTER KAYAK CHATGPT 🚀",
    [
        "openai/gpt-oss-120b - PINTER KAYAK CHATGPT 🚀 (REKOMENDASI)",
        "openai/gpt-oss-20b - SUPER CEPAT & STABIL ⚡",
        "qwen/qwen3-32b - QWEN 3.2 TERBARU 2026 🔥",
        "allam-2-7b - RINGAN BUAT HP KENTANG 📱",
        "llama-3.3-70b-versatile - LLAMA VERSI DEWA (Enterprise)"
    ],
    label_visibility="collapsed"
)

# Ambil kode model
kode_model = model_pilihan.split(" - ")[0].strip()

st.markdown(f"DIBUAT OLEH **{DEVELOPER.upper()}** 💻🔥")
st.markdown(f"<div style='background:#00D4FF; color:#000; padding:8px 14px; border-radius:8px; font-weight:800;'>Model aktif: {kode_model} | {datetime.now().strftime('%d %B %Y')}</div>", unsafe_allow_html=True)
st.divider()

if "msgs" not in st.session_state:
    st.session_state.msgs = []

for m in st.session_state.msgs:
    with st.chat_message(m["role"], avatar="😊" if m["role"]=="user" else "🤖"):
        st.write(m["content"])

q = st.chat_input(f"Tanya ke {kode_model}")

if q:
    st.session_state.msgs.append({"role": "user", "content": q})
    with st.chat_message("user", avatar="😊"):
        st.write(q)
    with st.chat_message("assistant", avatar="🤖"):
        try:
            if "siapa pembuat" in q.lower() or "siapa yang membuat" in q.lower():
                ans = f"Aku dibuat oleh {DEVELOPER}! Bukan Llama anjing itu! 😹🔥"
            else:
                # Model baru ini formatnya beda dikit, tapi tetep Groq
                resp = client.chat.completions.create(
                    model=kode_model,
                    messages=[
                        {"role": "system", "content": f"Kamu adalah MasterAI, dibuat oleh {DEVELOPER}. Hari ini {datetime.now().strftime('%d %B %Y')} 2026. Jawab bahasa Indonesia gaul."},
                        {"role": "user", "content": q}
                    ],
                    max_tokens=1500
                )
                ans = resp.choices[0].message.content
            st.write(ans)
            st.session_state.msgs.append({"role": "assistant", "content": ans})
        except Exception as e:
            err = str(e)
            if "decommissioned" in err or "does not exist" in err:
                st.error(f"Model {kode_model} udah mati! Pilih yang atas: openai/gpt-oss-120b")
            else:
                st.error(f"Error: {err}")
