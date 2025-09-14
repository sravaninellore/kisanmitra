# 🌾 KisanMitra

KisanMitra is an AI-powered assistant designed to help farmers diagnose crop issues, get pesticide/fertilizer recommendations, and discover relevant government schemes — all in their preferred language (English, Hindi, Telugu, etc.).


## 🚀 Problem Statement
Farmers often struggle to identify plant diseases, choose the right pesticides/fertilizers, and access government support schemes. Lack of quick and reliable guidance leads to crop loss and financial hardship.

## 💡 Solution
KisanMitra provides:
- 🩺 **AI-powered crop diagnosis** – Farmers describe symptoms, and the system suggests possible causes.
- 🧴 **Recommended pesticides/fertilizers** – Get curated suggestions for safe and effective treatments.
- 🏛 **Government schemes** – Discover schemes available for financial or agricultural support.


## 🛠️ Tech Stack
- **Backend**: Python (Flask / FastAPI)
- **Frontend/UI**: Streamlit
- **AI Models**: Groq API (LLM integration)
- **Text-to-Speech**: gTTS
- **Environment Management**: `.env` for API keys
- **Version Control**: Git & GitHub


## 🔑 Features
- Diagnose crop diseases using AI
- Get pesticide/fertilizer usage instructions
- Access government schemes (e.g., PM-KISAN)
- Audio-based support (farmers can listen to diagnosis)
- Multilingual support (English, Hindi, Telugu)


## 📂 Project Structure
kisanmitra/
│── app.py # Backend API
│── ui.py # Streamlit user interface
│── requirements.txt # Python dependencies
│── .env # Environment variables (not pushed to GitHub)
│── static/ # For audio files
│── README.md # Project documentation



## ⚙️ Setup Instructions

1. Clone this repo:
   ```bash
   git clone https://github.com/sravaninellore/kisanmitra.git
   cd kisanmitra
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/Scripts/activate   # On Windows
source venv/bin/activate       # On Linux/Mac
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Create a .env file:

ini
Copy code
GROQ_API_KEY=your_api_key_here
Run the backend:

bash
Copy code
python app.py
Run the Streamlit UI:

bash
Copy code
streamlit run ui.py
