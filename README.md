# AI Help Bot 🤖

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/) [![Flask](https://img.shields.io/badge/Flask-Web%20App-green?logo=flask)](https://flask.palletsprojects.com/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🌟 AI Help Bot: Next-Gen FAQ & Support Assistant

**AI Help Bot** is a next-generation assistant designed to provide instant, accurate, and context-aware answers to your help and FAQ questions. It combines the power of a **Knowledge Graph** (for structured, precise answers) with **Retrieval-Augmented Generation (RAG)** using DistilBERT (for flexible, generative responses when the KG doesn't have the answer).

> **Powered by Celestial Runtime**

---

## 🎬 Demo Video
[![Watch the demo](https://img.youtube.com/vi/DEMO_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=DEMO_VIDEO_ID)

---

## 🖼️ Screenshots
| Home & Chat | About & Features |
|:----------:|:---------------:|
| ![Home](screenshot-home.png) | ![About](screenshot-about.png) |

---

## 🚀 Features
- **Modern, responsive website UI** (Bootstrap 5, icons, gradients)
- **Knowledge Graph** for structured, fast answers
- **RAG fallback** (DistilBERT) for generative answers
- **Natural language Q&A** with fuzzy, synonym, and semantic matching
- **Health check endpoint** for easy monitoring
- **Easy to configure, extend, and deploy**
- **Runs on standard hardware** (8GB RAM, quad-core CPU)
- **All local processing** (privacy-first)

---

## 🛠️ Tech Stack
- **Python 3.8+**
- **Flask** (web app)
- **BeautifulSoup** (scraping)
- **RDFLib** (knowledge graph)
- **Transformers & Sentence Transformers** (RAG, semantic search)
- **Bootstrap 5 + Bootstrap Icons** (UI)

---

## ⚡ Quick Start
1. **Clone this repo:**
   ```bash
   git clone https://github.com/yourusername/ai-help-bot.git
   cd ai-help-bot
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure your scraping target and selectors in `config.py`**
4. **Run the demo script to scrape and build the KG:**
   ```bash
   python demo_script.py
   ```
5. **Start the web app:**
   ```bash
   python app.py
   ```
6. **Open your browser:**
   - Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 💡 Usage
- Ask any help or FAQ question in the chat box.
- If the answer is in the KG, you'll get a precise response.
- If not, the AI will generate a helpful answer from your content.
- Try greetings or random questions for a friendly fallback!

---

## 📂 Project Structure
```
ai-help-bot/
├── README.md
├── LICENSE
├── requirements.txt
├── config.py
├── sample_data/
│   └── sample_faq.html
├── app.py
├── scraper.py
├── kg_builder.py
├── chatbot.py
├── rag_model.py
├── utils.py
├── demo_script.py
├── templates/
│   └── index.html
```

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 🛡️ License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

**AI Help Bot &copy; 2024 | Powered by Knowledge Graph & RAG | Powered by Celestial Runtime** 