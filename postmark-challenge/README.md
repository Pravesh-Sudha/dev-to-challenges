# 📬 Email AI Assistant 🤖

This project is an **Email-based AI Assistant** powered by **Gemini (Google AI)** and **Postmark**. Users can simply send an email, and the assistant will respond automatically using AI-generated content.

> Think ChatGPT over email — with Gemini and FastAPI under the hood.

---

## 🚀 Features

- ✉️ Receives emails via Postmark Inbound Webhook
- 🧠 Processes the content using Gemini AI (via Google Generative AI API)
- 📤 Replies to the sender with AI-generated response
- ⚡ Built with FastAPI, Python, and Postmark API

---

## 🛠️ Tech Stack

- **FastAPI** – Web framework for Python
- **Postmark** – Inbound and outbound transactional email service
- **Google Gemini API** – For generating intelligent AI responses
- **Python 3.10+**
- **Dotenv** for environment configuration

---

## 🧑‍💻 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/email-ai-assistant.git
cd email-ai-assistant
````

### 2. Install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Create a `.env` file

```ini
# .env
POSTMARK_API_TOKEN=your-postmark-server-api-token
GEMINI_API_KEY=your-google-gemini-api-key
```

### 4. Run the FastAPI app

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

## 📡 Postmark Setup

1. Go to your [Postmark](https://postmarkapp.com/) account.
2. Set up an **Inbound Webhook** pointing to your server:

   ```
   https://yourdomain.com/inbound-email
   ```
3. Make sure your domain (e.g., `codewithpravesh.tech`) is verified in Postmark.
4. All incoming emails will trigger this endpoint and get AI responses.

---

## 🧠 Gemini API Integration

* Uses `google-generativeai` Python package.
* Make sure to enable Gemini API in your [Google Cloud Console](https://aistudio.google.com/app/apikey).
* Uses the model:

  ```
  models/gemini-2.5-flash-preview-04-17-thinking
  ```

---

## 🌐 Deploy on AWS EC2

> Want to make it public? Follow the [deployment guide here](#).

Basic requirements:

* `t2.micro` or `t3.micro` instance
* Ubuntu 22.04
* UFW to allow port 8000 or reverse proxy with Nginx
* Environment variables via `.env`

---

## 📁 Project Structure

```
├── main.py              # FastAPI app
├── utils.py             # Gemini + Postmark helper functions
├── .env                 # Environment variables (not committed)
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 🛡️ Security Notes

* Keep your API keys secret!
* Secure your endpoint using a signature header (coming soon).
* You can restrict incoming emails by sender if needed.

---

## ✨ Example Email

* **To:** `assistant@codewithpravesh.tech`

* **Subject:** Greet

* **Body:**

  ```
  Can you give me a motivational quote for today?
  ```

* **Response (automated):**

  ```
  "Success is not final, failure is not fatal: It is the courage to continue that counts." – Winston Churchill
  ```

---

## 🙌 Contributing

Got ideas, improvements, or bugs? Feel free to open a pull request or an issue!

---

## 📜 License

MIT License – do what you love with it.

---

## 💡 Author

Made with ❤️ by [Pravesh Sudha](https://praveshsudha.com)
Twitter: [@praveshstwt](https://x.com/praveshstwt)
