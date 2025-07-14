# 🤖 HelpBot – Streamlit Chatbot for Customer Support

A beginner-friendly, AI-powered chatbot using **Streamlit + Dialogflow** for real-time customer support. Built as part of **Future Interns – Task 3**, this bot can answer FAQs like “Where is my order?”, “Refund policy?”, or anything you train it for!

---

## 📸 Preview

![HelpBot Screenshot](https://via.placeholder.com/800x400?text=Chatbot+Preview+Here)

---

## 🚀 Features

- ✅ Streamlit frontend chat UI  
- ✅ Dialogflow intent matching  
- ✅ Smart fallback responses  
- ✅ Secure API access via GCP service account  
- ✅ Easy to extend & deploy

---

## 🛠 Tech Stack

| Component    | Technology              |
|--------------|--------------------------|
| Frontend     | Streamlit                |
| NLP Backend  | Google Dialogflow v2     |
| Language     | Python                   |
| Deployment   | Local / Streamlit Cloud  |

---

## 📂 Project Structure

```
intern/
├── main.py                   # Streamlit chatbot code
├── helpbot-anvc-key.json     # Dialogflow service account key (keep private)
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

---

## 🧑‍💻 Setup Instructions

```bash
git clone https://github.com/yourusername/helpbot-chatbot.git
cd helpbot-chatbot
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run main.py
```

> 💡 Make sure `helpbot-anvc-key.json` is in the project folder and correctly referenced in `main.py`.

---

## 🧠 Dialogflow Setup

1. Go to [Dialogflow Console](https://dialogflow.cloud.google.com/)
2. Create or open your agent (`helpbot-anvc`)
3. Create intents like:
   - “Hi” → “Hello! How can I help you today?”
   - “Where is my order?” → “Please provide your order ID.”
   - “Refund policy?” → “Refunds take 5–7 business days.”
4. Create a service account with `Dialogflow API Admin` permission
5. Download the key as `helpbot-anvc-key.json`

---

## 🧾 requirements.txt

```text
streamlit
google-cloud-dialogflow
```

---

## 📦 .gitignore

```gitignore
*.json
__pycache__/
venv/
*.pyc
.DS_Store
```

---

## 🌍 Deployment

You can host this chatbot on:

- [Streamlit Cloud](https://streamlit.io/cloud)
- [Render](https://render.com/)
- [Heroku](https://heroku.com/)
- Google Cloud Run

---

## ⚠️ Security Note

- Do **NOT** upload `helpbot-anvc-key.json` to GitHub.
- Always add it to `.gitignore`.

---

## 🙋‍♂️ Author

**Muhamed Ibrahim**  
📧 [md.ibrahim984343@gmail.com](mailto:md.ibrahim984343@gmail.com)  
💼 Project for Future Interns – Task 3

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ⭐ Show Some Love

If this project helped you, star it on GitHub ✨
