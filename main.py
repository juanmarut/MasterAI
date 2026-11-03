import streamlit as st
import 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

# Mengambil API Key langsung dari kotak Secrets Streamlit Cloud yang sudah kamu isi
try:
    API_KEY = st.secrets["API KEY KAMU"]
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error("Waduh, Kunci API Google belum terpasang di Secrets! 🗿")

# Inisialisasi model resmi yang stabil dan cepat
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("MasterAI 🤖")
st.write("DIBUAT OLEH DEVELOPER JONATHAN KRISTIAN SERGIO MARUT 💻🔥")

# Input pertanyaan dari user
pertanyaan = st.text_input("Tanya Apa  Saja!")

if st.button("Kirim ke MasterAI 🚀"):
    if pertanyaan:
        with st.spinner("MasterAI sedang berpikir...🦾🧠"):
            try:
                tanggapan = model.generate_content(pertanyaan)
                st.success("MasterAI:")
                st.write(tanggapan.text)
            except Exception as e:
                st.error(f"Terjadi kesalahan saat memanggil AI: {e}")
    else:
        st.warning("Ketik dulu pertanyaannya, Bro! 🗿")
