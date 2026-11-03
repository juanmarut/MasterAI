import streamlit as st
from groq import Groq
from datetime import datetime

st.set_page_config(page_title="MasterAI", page_icon="⚡")

DEVELOPER = "Jonathan Kristian Sergio Marut, 15 tahun, SMAK Monte Carmelo Maumere - Juan"

# Ambil key
try:
    key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=key)
except:
    st.error('Belum ada GROQ_API_KEY di Secrets! Isi: GROQ_API_KEY = "gsk_..."')
    st.stop()

st.title("MasterAI 🤖")
st.write(f"DIBUAT OLEH {DEVELOPER} 💻🔥")
st.caption(f"{datetime.now().strftime('%d %B %Y')} | Groq OK")

# Chat simpel
if "msgs" not in st.session_state:
    st.session_state.msgs = []

for m in st.session_state.msgs:
    with st.chat_message(m["role"]):
        st.write(m["content"])

q = st.chat_input("Tanya apa aja")

if q:
    st.session_state.msgs.append({"role": "user", "content": q})
    with st.chat_message("user"):
        st.write(q)
    with st.chat_message("assistant"):
        try:
            if "siapa pembuat" in q.lower() or "siapa yang membuat" in q.lower():
                ans = f"Aku dibuat oleh {DEVELOPER}! 🔥"
            else:
                # MODEL YANG 100% ADA DI GROQ SEKARANG
                resp = client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=[
                        {"role": "system", "content": f"Kamu MasterAI buatan {DEVELOPER}. Hari ini 2026."},
                        {"role": "user", "content": q}
                    ]
                )
                ans = resp.choices[0].message.content
            st.write(ans)
            st.session_state.msgs.append({"role": "assistant", "content": ans})
        except Exception as e:
            st.error(f"Error Groq: {e}")
