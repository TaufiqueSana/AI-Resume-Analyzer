import streamlit as st
import pdfplumber
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

st.title("AI Resume Analyzer & Job Match Score")

# Upload Resume
resume_file = st.file_uploader("Upload your Resume (PDF only)", type=['pdf'])

# Job Description Input
job_desc = st.text_area("Paste the Job Description here")

# Extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# Calculate match score between resume and job description
def get_match_score(resume_text, job_text):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform([resume_text, job_text])
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(score * 100, 2)

# Main logic
if resume_file and job_desc:
    resume_text = extract_text_from_pdf(resume_file)
    match_score = get_match_score(resume_text, job_desc)
    st.subheader(f"Match Score: {match_score}%")
