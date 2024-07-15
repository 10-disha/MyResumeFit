import streamlit as st  # For creating the web app interface
import google.generativeai as genai  # For using Google Generative AI
import os  # For handling environment variables
import PyPDF2 as pdf  # For reading PDF files
from dotenv import load_dotenv  # For loading environment variables from a .env file

# Load environment variables from .env file
load_dotenv()

# Configure Google Generative AI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from the Generative AI model
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

# Function to extract text from an uploaded PDF file
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += str(page.extract_text())
    return text

# Prompt template for the Generative AI model
input_prompt = """
ATS Resume Evaluation
Resume: {text}
Description: {jd}

I want the response in one single string having the structure
{{"JD Match":"%", "MissingKeywords:[]", "Profile Summary":""}}
"""

# Streamlit app interface
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")
submit = st.button("Submit")

# Action on form submission
if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        input_prompt_formatted = input_prompt.format(text=text, jd=jd)
        response = get_gemini_response(input_prompt_formatted)
        st.subheader(response)
