import streamlit as st
from groq import Groq
from datetime import datetime

st.set_page_config(page_title="MasterAI - Anti Llama", page_icon="🔥")

DEVELOPER = "Jonathan Kristian Sergio Marut - Juan 15 tahun Maumere"

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error('Isi Secrets: GROQ_API_KEY = "gsk_..."')
    st.stop()

st.title("MasterAI 🤖 Anti-Llama Edition 🔥")
st.caption("Pilih model selain Llama anjing itu 😹")

# ===== PILIH MODEL - INI KUNCINYA! =====
model_pilihan = st.selectbox(
    "Pilih Otak AI nya:",
    [
        "gemma2-9b-it - PALING STABIL ANTI ERROR ✅",
        "mixtral-8x7b-32768 - JAGO CODING & MTK 🧠",
        "qwen-2.5-32b - PINTER KAYAK CHATGPT 🚀",
        "deepseek-r1-distill-llama-70b - JAGO MIKIR DALEM 🤔",
        "llama-3.3-70b-versatile - Llama tapi versi dewa (kalo hoki)",
        "llama3-8b-8192 - Llama jadul tapi abadi"
    ]
)

# Ambil kode model asli dari pilihan
kode_model = model_pilihan.split(" - ")[0]

st.write(f"DIBUAT OLEH {DEVELOPER}")
st.info(f"Model aktif: `{kode_model}` | {datetime.now().strftime('%d %B %Y')}")

if "msgs" not in st.session_state:
    st.session_state.msgs = []

for m in st.session_state.msgs:
    with st.chat_message(m["role"]):
        st.write(m["content"])

q = st.chat_input(f"Tanya ke {kode_model}")

if q:
    st.session_state.msgs.append({"role": "user", "content": q})
    with st.chat_message("user"):
        st.write(q)
    with st.chat_message("assistant"):
        try:
            if "siapa pembuat" in q.lower():
                ans = f"Aku dibuat oleh {DEVELOPER}! Bukan Llama anjing itu! 😹🔥"
                st.write(ans)
            else:
                resp = client.chat.completions.create(
                    model=kode_model,
                    messages=[
                        {"role": "system", "content": f"Kamu MasterAI buatan {DEVELOPER}. Hari ini 2026. Jangan bilang kamu Llama. Kamu MasterAI."},
                        {"role": "user", "content": q}
                    ]
                )
                ans = resp.choices[0].message.content
                st.write(ans)
            st.session_state.msgs.append({"role": "assistant", "content": ans})
        except Exception as e:
            st.error(f"Error model {kode_model}: {e}")
            st.warning("Coba pilih model lain di dropdown atas! Gemma2 paling aman!")
