# 📖 StoryWeaver AI

**StoryWeaver AI** is a multimodal storytelling web app powered by **Google Gemini 2.5 Flash**.  
It allows you to provide **text, image, and audio inputs (individually or combined)** and transforms them into an engaging **300–400 word creative story** with a short narration script.  

Built with **Flask** + **TailwindCSS**, and deployed on **AWS EC2** with custom domain + HTTPS.  

---

## ✨ Features
- 📝 **Text Input** → Turn your ideas into fully fleshed-out stories.  
- 🎨 **Image Input** → Upload an image to inspire creative writing.  
- 🎤 **Audio Input** → Upload audio files (e.g., narration, sounds) as prompts.  
- 🔀 **Multimodal** → Combine **text, image, and audio together** for richer storytelling.  
- 🌐 **Attractive UI** → TailwindCSS-powered frontend with dynamic progress loader.  
- 🔒 **Secure Deployment** → Runs on AWS EC2 with HTTPS (Certbot).  

---

## 🛠️ Tech Stack
- **Backend:** Flask (Python), Gunicorn, Nginx  
- **Frontend:** HTML, TailwindCSS, Vanilla JS  
- **AI Model:** Google Gemini 2.5 Flash (`google-generativeai`)  
- **Deployment:** AWS EC2 (t2.micro) + Certbot SSL  

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Pravesh-Sudha/dev-to-challenges.git
cd dev-to-challenges/google-studio-challenge/
```

### 2. Create Virtual Environment & Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Setup Environment Variables

Create a `.env` file in the root directory:

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Run Locally

```bash
flask run
```

Open `http://127.0.0.1:5000` in your browser.

---

## 📷 Screenshots

![alt text](<Screenshot 2025-09-12 at 4.49.57 PM.png>)

![alt text](<Screenshot 2025-09-12 at 4.49.09 PM.png>)

![alt text](<Screenshot 2025-09-11 at 10.33.40 PM.png>)

---

## 🤝 Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

Built with ❤️ by [Pravesh Sudha](https://praveshsudha.com)

* AWS Community Builder 🚀
* DevOps & Cloud Enthusiast