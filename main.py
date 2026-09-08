import google.generativeai as genai
import streamlit as st

# Mengambil API Key langsung dari kotak Secrets Streamlit Cloud yang sudah kamu isi
try:
    API_KEY = st.secrets["KUNCI_API_GOOGLE"]
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error("Waduh, Kunci API Google belum terpasang di Secrets! 🗿")

# Inisialisasi model resmi yang stabil dan cepat
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("MasterAI 🤖")
st.write("PC ASUS TUF FA506NC MODE ON 💻🔥")

# Input pertanyaan dari user
pertanyaan = st.text_input("Masukan (Kamu):")

if st.button("Kirim ke MasterAI 🚀"):
    if pertanyaan:
        with st.spinner("MasterAI sedang berpikir..."):
            try:
                tanggapan = model.generate_content(pertanyaan)
                st.success("MasterAI:")
                st.write(tanggapan.text)
            except Exception as e:
                st.error(f"Terjadi kesalahan saat memanggil AI: {e}")
    else:
        st.warning("Ketik dulu pertanyaannya, Bro! 🗿")
