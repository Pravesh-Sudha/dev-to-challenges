# AI Agent & DevOps Portfolio 🚀

> **"New Year New You" Challenge Submission**

Welcome to my AI-focused portfolio website! This project showcases my journey bridging the gap between **DevOps Engineering** and **AI Agent Development**. It was built from scratch using Vanilla web technologies and deployed on **Google Cloud Run**.

## 🌟 Live Demo
https://portfolio-website-93951960491.us-central1.run.app/

![alt text](<assets/Screenshot 2026-01-19 at 11.28.34 PM.png>)
![alt text](<assets/Screenshot 2026-01-19 at 11.28.56 PM.png>)
![alt text](<assets/Screenshot 2026-01-19 at 11.29.07 PM.png>)

## 📂 Repository Structure
This project is part of my Dev.to Challenges repository:
- **Repo**: [https://github.com/Pravesh-Sudha/dev-to-challenges](https://github.com/Pravesh-Sudha/dev-to-challenges)
- **Directory**: `new-year-portfolio/`

## ✨ Features
- **Modern Aesthetic**: Dark theme with glassmorphism effects and neon accents.
- **2x2 Project Grid**: Showcasing projects with **YouTube Thumbnails**, hover effects, and direct links to Blogs/Demos.
- **Interactive Details**: Custom cursor, smooth scroll animations, and "floating card" hero effects.
- **Dedicated Sections**:
  - **About**: Philosophy + Tech.
  - **Skills**: Categorized into AI/Agents and DevOps/Cloud.
  - **Certifications**: Highlighting AWS Solutions Architect status.
- **Responsiveness**: Fully optimized for Mobile, Tablet, and Desktop.

## 🛠️ Tech Stack
- **Frontend**: HTML5, CSS3 (Variables, Grid, Flexbox), JavaScript (IntersectionObserver).
- **Deployment**: Google Cloud Run.
- **Containerization**: Docker, Nginx.
- **AI Assistance**: Built with the help of Google's Antigravity.

## 🚀 Getting Started

### Run Locally
Simply open `index.html` in your browser, or serve it with a lightweight server:

```bash
# Using python
python3 -m http.server 8000
```

### Run with Docker
```bash
# Build the image
docker build -t portfolio .

# Run container
docker run -p 8080:8080 portfolio
```

Visit `http://localhost:8080` to see the site.

## ☁️ Deployment (Google Cloud Run)
A helper script `deploy.sh` is included to automate deployment.

1. **Authenticate**:
   ```bash
   gcloud auth login
   gcloud config set project [YOUR_PROJECT_ID]
   ```

2. **Deploy**:
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

## 📬 Connect with Me

I love talking about Cloud, Kubernetes, and AI Agents. Feel free to reach out!

- **Email**: [programmerpravesh@gmail.com](mailto:programmerpravesh@gmail.com)
- **Dev.to**: [Pravesh Sudha](https://dev.to/pravesh_sudha_3c2b0c2b5e0)
- **GitHub**: [Pravesh-Sudha](https://github.com/Pravesh-Sudha)
- **LinkedIn**: [Pravesh Sudha](https://www.linkedin.com/in/pravesh-sudha/)
- **Twitter (X)**: [@praveshstwt](https://x.com/praveshstwt)

---
*Built with ❤️ by Pravesh Sudha*
