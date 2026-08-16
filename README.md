# Brief | Autonomous Academic Helping Agent 🤖

Brief is a next-generation academic workspace built for the **Google "All things agentic" Hackathon** under the **Taskmaster** category. It is designed to help university students instantly transform heavy lecture materials (PDF, PPTX, TXT) into beautifully structured visual reports and premium audio podcasts.

## 🎓 The Story & Inspiration
As an incoming IT / Computer Science student starting classes on September 1st, I wanted to build a practical, real-world solution to handle the massive volume of academic content ahead. Brief acts as an autonomous assistant that does the heavy lifting, showcasing how junior IT developers can leverage modern AI tools to build impactful workflows from day one.

## 🚀 Tech Stack & Frameworks
* **Frontend UI:** Streamlit (Custom Premium Cobalt Blue Dashboard)
* **AI Orchestration:** Official **Google GenAI SDK** (Gemini 3.5 Flash)
* **Audio Production:** gTTS (Google Text-to-Speech Engine)
* **Deployment Infrastructure:** Dockerized & Hosted on **Google Cloud Run**

## 📂 Project Structure
* `brief.py.py` - The main interactive Streamlit application with the premium UI.
* `ai_studio code` - The core backend script used to validate the Gemini API integration.
* `Dockerfile` & `requirements.txt` - Deployment recipes for production hosting.

## 📦 How to Run Locally
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Insert your Gemini API key inside `brief.py.py`.
4. Run the command: `streamlit run brief.py.py`
