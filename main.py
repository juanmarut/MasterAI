import google.generativeai as genai
import os
from dotenv import load_dotenv

# Muat API Key dari file .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# PAKE YG NGEBUT BUAT PC KUAT 🔥
model = genai.GenerativeModel("gemini-2.5-flash")

print("🔥 MasterAI 2.5-FLASH SIAP! Ketik 'exit' buat keluar 🔥")
print("PC ASUS TUF FA506NCG MODE ON 💪")

while True:
    pertanyaan = input("Kamu: ")
    if pertanyaan.lower() == "exit":
        print("MasterAI: Oke sampai jumpa!")
        break
    response = model.generate_content(pertanyaan)
    print("MasterAI:", response.text)
