# TapGuide AI 🎯

## 📌 Basic Details

**Team Name:** AVENGERS  
**College:** Saintgits College of Engineering  
**Cluster:** A  

---

## 👥 Team Members

- **Steny Thankkam Raju** – Saintgits College of Engineering  
- **Krishnapriya** – Saintgits College of Engineering  

---

## 🔗 Hosted Project Link

https://github.com/krishnapriya-03/TapGuide

---

# 🧠 Project Description

TapGuide is an offline Windows AI assistant that captures system popups using a global hotkey, extracts text via OCR, and explains them in simple language using a local AI model. It also supports contextual follow-up questions and text-to-speech for accessibility.

---

# ❗ Problem Statement

Many non-technical and elderly users struggle to understand system popups, permission dialogs, and security warnings. This often leads to blindly clicking “Allow” or “OK,” increasing security risks. Most AI assistants require internet access, raising privacy concerns.

---

# ✅ The Solution

TapGuide captures the screen in real time, extracts popup text using OCR, and explains it clearly using a local offline AI model. It includes contextual follow-up support and automatic voice guidance to improve digital safety and accessibility.

---

# 🛠 Technical Details

## 🔹 Technologies/Components Used

### 💻 Software

**Languages Used:**
- Python

**Frameworks Used:**
- Tkinter (Desktop UI)

**Libraries Used:**
- pytesseract (OCR)
- Pillow
- mss (Screenshot capture)
- pyttsx3 (Offline Text-to-Speech)
- subprocess (Ollama integration)
- threading (Non-blocking UI)

**Tools Used:**
- VS Code
- Git & GitHub
- PyInstaller (Windows Executable)
- Inno Setup (Installer creation)
- Ollama (Local LLM engine)
- Tesseract OCR

---

# 🚀 Features

- **Global Hotkey Trigger**  
  Press `Ctrl + Shift + Space` to analyze the current screen instantly.

- **Offline AI Explanation**  
  Uses a local AI model (phi3:mini via Ollama) — no internet required.

- **Contextual Follow-Up Questions**  
  Users can ask additional questions about the same popup.

- **Automatic Text-to-Speech**  
  Speaks the most important safety warning for elderly and visually impaired users.

- **Fully Offline Mode**  
  No cloud calls — privacy-preserving and secure.

---

# ⚙ Implementation

## 🔹 Installation: 
Inno Setup (Installer creation)
https://drive.google.com/drive/folders/1NNngCgsVMJQznpF2GpR0Q844d4kQtaw7

```bash
git clone https://github.com/krishnapriya-03/TapGuide.git
cd TapGuide
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
