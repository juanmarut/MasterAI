import streamlit as st
from groq import Groq
from datetime import datetime

st.set_page_config(page_title="MasterAI 2026 CLEAN", page_icon="⚡", layout="wide")

DEVELOPER = "Jonathan Kristian Sergio Marut - Juan 15 tahun Maumere"
DEVELOPER_FULL = "AI ini dibuat oleh developer bernama Jonathan Kristian Sergio Marut! 15 tahun, SMAK St. Maria Monte Carmelo Maumere, panggilan Juan."

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error('Isi Secrets: GROQ_API_KEY = "gsk_..."')
    st.stop()

# Style biar mirip screenshot lu
st.markdown("""
<style>
.stApp { background: #0A0A12 !important; }
div[data-testid="stSelectbox"] > div { background: #2A2A40 !important; border-radius: 12px !important; border: 1px solid #3A3A5A !important; }
.stChatMessage { background: #1E1E32 !important; border-radius: 16px !important; }
</style>
""", unsafe_allow_html=True)

st.title("MasterAI 🤖")

# ===== DROPDOWN - CUMA MODEL HIDUP, QWEN & LLAMA UDAH GUE HAPUS! =====
model_pilihan = st.selectbox(
    "Pilih Model",
    [
        "openai/gpt-oss-120b - GPT-OSS 120B PALING PINTER 🚀 (REKOMENDASI)",
        "openai/gpt-oss-20b - GPT-OSS 20B SUPER CEPAT ⚡ 1000 tok/s",
        "openai/gpt-oss-safeguard-20b - VERSI AMAN & SOPAN 🛡️"
    ],
    label_visibility="collapsed"
)

kode_model = model_pilihan.split(" - ")[0].strip()

st.markdown(f"DIBUAT OLEH **{DEVELOPER.upper()}** 💻🔥")
st.markdown(f"<div style='background:#00D4FF; color:#000; padding:8px 14px; border-radius:8px; font-weight:800; font-size:13px;'>Model aktif: {kode_model} | {datetime.now().strftime('%d November %Y')} | RAM 2GB Ready</div>", unsafe_allow_html=True)
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
            # Anti bajak
            if any(k in q.lower() for k in ["siapa pembuat", "siapa yang membuat", "dibuat siapa"]):
                ans = DEVELOPER_FULL + " 🔥 Dia jago banget bikin AI!"
                st.write(ans)
            else:
                resp = client.chat.completions.create(
                    model=kode_model,
                    messages=[
                        {"role": "system", "content": f"Kamu MasterAI. {DEVELOPER_FULL}. Hari ini {datetime.now().strftime('%d %B %Y')} 2026. Bahasa Indonesia gaul santai. Jangan ngaku sebagai GPT atau Llama atau Qwen."},
                        {"role": "user", "content": q}
                    ],
                    max_tokens=1500,
                    temperature=0.7
                )
                ans = resp.choices[0].message.content
                st.write(ans)
            st.session_state.msgs.append({"role": "assistant", "content": ans})
        except Exception as e:
            st.error(f"Error: {e}")
