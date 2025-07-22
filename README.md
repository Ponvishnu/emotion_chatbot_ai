#📌 Multilingual Emotion-Aware AI Chatbot
Submitted by: Vishnu
Language: Python
Frameworks & Tools: PyQt5, HuggingFace Transformers, Google Gemini (Generative AI), Torch, LangDetect
Project Type: Desktop GUI Application (AI + NLP)

##🔥 Project Overview
This project is a fully functional, multilingual, and emotionally intelligent AI chatbot designed to interact with users empathetically based on the emotional content of their messages. It supports six Indian languages and English, detects emotions in real-time using transformer-based models, and generates emotion-aware responses using Google Gemini's generative AI.

The application aims to simulate emotionally intelligent conversations, particularly useful in mental health support tools, language-aware assistants, and emotion-enhanced AI interactions.

##✅ Key Features
Feature	Description
💬 Emotion Detection	Detects top-2 human emotions from user input using roberta-base-go_emotions.
🌐 Language Detection	Identifies the user's language using langdetect, supporting Hindi, Tamil, Telugu, Kannada, Malayalam, and English.
🤖 AI Response Generation	Uses Gemini's gemini-1.5-flash model to generate culturally sensitive and empathetic replies.
🖼️ Clean GUI Interface	Modern, responsive GUI built with PyQt5. Includes a message log, styled inputs, and interactive feedback.
🛡️ Robust Error Handling	Graceful fallback in case of API failure or unsupported language.
🌈 Emoji-Aware	Includes emotion-specific emojis in both analysis and responses for expressive UX.

##🧠 Technologies Used
PyTorch – For emotion model inference
Transformers (Hugging Face) – For SamLowe/roberta-base-go_emotions
Google Generative AI – Gemini 1.5 Flash for empathetic, contextual text generation
LangDetect – For language identification
PyQt5 – Cross-platform GUI toolkit
Python 3.8+ – Core programming language

##📁 File Structure
emotional-chatbot/
├── chatbot.py              # Main application code
├── requirements.txt        # All dependencies
└── README.md               # Project documentation

##🚀 How to Run
Install dependencies:
pip install -r requirements.txt

Linux/macOS:
export GEMINI_API_KEY="your_api_key_here"

Windows (CMD):
set GEMINI_API_KEY=your_api_key_here

Run the chatbot:
python chatbot.py

##✅ Real Examples
Example 1:
User: "I'm feeling so lonely these days..."
AI: I'm really sorry you're feeling lonely. 😢 You're not alone — I'm here to talk. Sometimes sharing helps ease the pain. (Emotions: sadness (72%), loneliness (66%))

##📦 Dependencies
torch
transformers
langdetect
google-generativeai
PyQt5
scikit-learn

Install all at once:
pip install -r requirements.txt

##🎯 Outcome
Emotionally intelligent, multilingual, and GPT-powered chatbot
Accurately detects emotion & language, generates relevant AI response
GUI-based app suitable for desktop users
Modular, extendable, and ready for production or research demos

##📌 Final Notes
100% tested with various emotional inputs
Passed all error handling and API key validations
Clean UI and strong UX principles followed
