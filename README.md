**🧠 AI Resume Analyzer**

A simple AI-powered web app that analyzes your resume and compares it with a job description to give you a match score using natural language processing (NLP) techniques.

**🚀 Features**

- 📄 Upload Resume in PDF format
- 📝 Paste any Job Description
- 🔍 Calculates a similarity score using TF-IDF and Cosine Similarity
- ✅ Helps improve your resume by matching relevant job requirements

**📂 Project Structure**

Resume_analyzer
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
└── README.md # Project documentation

**🛠️ Tech Stack**

- Frontend/UI: Streamlit
- Backend/NLP: Python, NLTK, Scikit-learn
- PDF Parsing: PDFPlumber

**▶️ Getting Started
1. Clone the Repository**

```bash
git clone https://github.com/TaufiqueSana/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer

**2. Install Dependencies**

Make sure Python is installed, then install required packages:

```bash
pip install -r requirements.txt

**3. Run the App**

```bash
streamlit run app.py

**❓ How It Works**

The app extracts text from your uploaded resume (PDF).
It uses TF-IDF vectorization to understand the context.
Cosine Similarity measures how closely your resume matches the job description.

**🧑‍💻 Author**

  **Name**: Taufique Sana
  **Email**: taufiquesana171@gmail.com
  b: TaufiqueSana
