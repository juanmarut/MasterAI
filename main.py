import streamlit as st
import sys
import subprocess

# ===== AUTO FIX MODULE NOT FOUND - INI KUNCINYA! =====
try:
    from groq import Groq
except ModuleNotFoundError:
    st.warning("⚙️ Lagi install Groq... tunggu 20 detik...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "groq"])
    from groq import Groq
    st.success("✅ Groq berhasil di-install! Lanjut...")
    time.sleep(1)
    st.rerun()

import time
import uuid
from datetime import datetime

st.set_page_config(page_title="MasterAI - FIXED", page_icon="⚡")

DEVELOPER_INFO = "AI ini dibuat oleh Jonathan Kristian Sergio Marut! 15 tahun, SMAK Monte Carmelo Maumere, panggilan Juan."

# Ambil API Key
try:
    GROQ_KEY = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=GROQ_KEY)
except Exception as e:
    st.error("❌ Belum ada GROQ_API_KEY di Secrets!")
    st.code('GROQ_API_KEY = "gsk_..."', language="toml")
    st.stop()

st.title("MasterAI 🤖")
st.write(f"**DIBUAT OLEH JONATHAN KRISTIAN SERGIO MARUT** 💻🔥")
st.caption(f"🌐 {datetime.now().strftime('%d %B %Y')} | Auto-Fixed | RAM 2GB Ready")

if "chats" not in st.session_state:
    fid = str(uuid.uuid4())
    st.session_state.chats = {fid: {"title": "Ngobrol Baru", "messages": [], "created": time.time()}}
    st.session_state.active_chat = fid

def get_active(): return st.session_state.chats[st.session_state.active_chat]

active = get_active()

for m in active["messages"]:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

pertanyaan = st.text_input("Tanya apa aja!")

if st.button("Kirim 🚀"):
    if pertanyaan:
        if len(active["messages"]) == 0:
            active["title"] = pertanyaan[:25]
        active["messages"].append({"role": "user", "content": pertanyaan})
        with st.chat_message("user"):
            st.markdown(pertanyaan)
        with st.chat_message("assistant"):
            try:
                if "siapa yang membuat" in pertanyaan.lower() or "siapa pembuat" in pertanyaan.lower():
                    ans = DEVELOPER_INFO
                else:
                    res = client.chat.completions.create(
                        model="model="llama-3.3-70b-versatile",
                        messages=[
                            {"role": "system", "content": f"Kamu MasterAI. {DEVELOPER_INFO}. Hari ini {datetime.now().strftime('%d %B %Y')} 2026. Bahasa gaul."},
                            {"role": "user", "content": pertanyaan}
                        ]
                    )
                    ans = res.choices[0].message.content
                st.markdown(ans)
                active["messages"].append({"role": "assistant", "content": ans})
            except Exception as e:
                st.error(f"Error Groq: {e}")
    else:
        st.warning("Ketik dulu bro! 🗿")
