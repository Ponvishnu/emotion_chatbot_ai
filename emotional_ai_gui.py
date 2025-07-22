import os
import sys
import torch
import google.generativeai as genai
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton,
    QHBoxLayout, QListWidget, QListWidgetItem
)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from langdetect import detect, DetectorFactory
from sklearn.preprocessing import MultiLabelBinarizer

# ---------------- CONFIGURE GEMINI API ----------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise EnvironmentError("\n[❌] Please set your Gemini API Key in the environment variable 'GEMINI_API_KEY'.")

# ---------------- CONFIGURE GEMINI ----------------
genai.configure(api_key=GEMINI_API_KEY)

# ---------------- LOAD ADVANCED EMOTION MODEL ----------------
emo_tokenizer = AutoTokenizer.from_pretrained("SamLowe/roberta-base-go_emotions")
emo_model = AutoModelForSequenceClassification.from_pretrained("SamLowe/roberta-base-go_emotions")
emo_labels = emo_model.config.id2label

DetectorFactory.seed = 0
SUPPORTED_LANGS = {
    "en": "English", "hi": "Hindi", "ta": "Tamil",
    "te": "Telugu", "kn": "Kannada", "ml": "Malayalam"
}

# ---------------- EMOTION + LANG DETECTION ----------------
def detect_language(text):
    try:
        lang = detect(text)
        return lang if lang in SUPPORTED_LANGS else "en"
    except:
        return "en"

def detect_emotions_advanced(text, top_k=2):
    inputs = emo_tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        logits = emo_model(**inputs).logits
        probs = torch.sigmoid(logits)[0]
        top_indices = torch.topk(probs, k=top_k).indices.tolist()
        return [f"{emo_labels[i]} ({round(float(probs[i]) * 100)}%)" for i in top_indices]

# ---------------- GEMINI GENERATION ----------------
def generate_response(user_text, emotions, lang):
    prompt = (
        f"The user is feeling: {', '.join(emotions)}.\n"
        f"Respond empathetically and culturally sensitively in {SUPPORTED_LANGS.get(lang, 'English')} with an emoji.\n"
        f"User: \"{user_text}\"\nAI:"
    )
    try:
        gmodel = genai.GenerativeModel("gemini-1.5-flash")
        response = gmodel.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Gemini error: {str(e)}"

# ---------------- GUI APP ----------------
class ChatBotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🤗 Multilingual Emotional AI Chatbot")
        self.setGeometry(400, 150, 700, 600)
        self.setStyleSheet("background-color: #f0f8ff;")

        layout = QVBoxLayout()

        self.title = QLabel("🤗 Multilingual Emotional AI Chatbot")
        self.title.setFont(QFont("Arial", 20))
        self.title.setStyleSheet("color: #333;")
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)

        self.chat_history = QListWidget()
        self.chat_history.setStyleSheet("background: white; border: 1px solid #ccc;")
        layout.addWidget(self.chat_history)

        input_layout = QHBoxLayout()
        self.user_input = QTextEdit()
        self.user_input.setPlaceholderText("Type how you feel in any supported language...")
        self.user_input.setFixedHeight(60)
        self.user_input.setStyleSheet("font-size: 14px;")
        input_layout.addWidget(self.user_input)

        self.send_btn = QPushButton("Send")
        self.send_btn.setStyleSheet("background-color: #00aaff; color: white; font-weight: bold; padding: 10px;")
        self.send_btn.clicked.connect(self.process_input)
        input_layout.addWidget(self.send_btn)

        layout.addLayout(input_layout)
        self.setLayout(layout)

    def add_message(self, text, sender):
        item = QListWidgetItem()
        if sender == "user":
            item.setText(f"You: {text}")
            item.setTextAlignment(Qt.AlignRight)
            item.setForeground(QColor("blue"))
        else:
            item.setText(f"AI: {text}")
            item.setTextAlignment(Qt.AlignLeft)
            item.setForeground(QColor("green"))
        self.chat_history.addItem(item)
        self.chat_history.scrollToBottom()

    def process_input(self):
        text = self.user_input.toPlainText().strip()
        if not text:
            return

        self.add_message(text, "user")
        self.user_input.clear()

        lang = detect_language(text)
        emotions = detect_emotions_advanced(text, top_k=2)
        ai_reply = generate_response(text, emotions, lang)

        self.add_message(f"{ai_reply} ({', '.join(emotions)})", "bot")

# ---------------- RUN APP ----------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChatBotApp()
    window.show()
    sys.exit(app.exec_())
