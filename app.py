import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf

from dotenv import load_dotenv

load_dotenv() ## load all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Gemini Pro Response
def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += str(page.extract_text())
    return text

## Prompt Template
input_prompt="""
ATS
resume:{text}
description:{jd}

I want the response
{{"JD Match":"%", "MissingKeywords:[]","Profile Summary":""}}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please upload the pdf")
submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_response(input_prompt)
        st.subheader(response)















# import streamlit as st
# import os
# import PyPDF2 as pdf
# from dotenv import load_dotenv
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure Generative AI with the API key
# api_key = os.getenv("GOOGLE_API_KEY")
# if api_key is None:
#     st.error("API key is not set. Please set the API key in the .env file.")
#     st.stop()

# # Verify the loaded API key (for debugging purposes)
# st.write(f"Loaded API Key: {api_key}")

# genai.configure(api_key=api_key)

# # Function to get response from the generative AI model
# def get_gemini_response(input_text):
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate(input_text=input_text)
#     return response.output_text

# # Function to extract text from PDF
# def input_pdf_text(uploaded_file):
#     reader = pdf.PdfReader(uploaded_file)
#     text = ""
#     for page_num in range(len(reader.pages)):
#         page = reader.pages[page_num]
#         text += str(page.extract_text())
#     return text

# # Prompt Template
# input_prompt_template = """
# Hey Act like a skilled or very experienced professional.
# resume: {text}
# description: {jd}

# I want the response in one single string having the structure:
# {{"JD Match":"%", "MissingKeywords:[], "Profile Summary":""}}
# """

# # Streamlit app
# st.title("Smart ATS")
# st.text("Improve your resume ATS")
# jd = st.text_area("Paste the job Description")
# uploaded_file = st.file_uploader("Upload your resume", type="pdf", help="Please upload the PDF")

# submit = st.button("Submit")

# if submit:
#     if uploaded_file is not None:
#         text = input_pdf_text(uploaded_file)
#         input_prompt = input_prompt_template.format(text=text, jd=jd)
#         response = get_gemini_response(input_prompt)
#         st.subheader(response)














# import streamlit as st
# import os
# import PyPDF2 as pdf
# from dotenv import load_dotenv
# # Placeholder for google.generativeai import - replace with actual import if available
# # import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure Generative AI with the API key
# api_key = os.getenv("GOOGLE_API_KEY")
# if api_key is None:
#     st.error("API key is not set. Please set the API key in the .env file.")
#     st.stop()

# # Verify the loaded API key (for debugging purposes)
# st.write(f"Loaded API Key: {api_key}")

# # Placeholder for API key configuration
# # genai.configure(api_key=api_key)

# # Function to get response from the generative AI model
# def get_gemini_response(input_text):
#     # Placeholder for model creation and response generation
#     # Replace with actual method if available
#     # model = genai.GenerativeModel('gemini-pro')
#     # response = model.generate(input_text=input_text)
#     # return response.output_text
#     # Fallback response for demonstration purposes
#     return "This is a placeholder response."

# # Function to extract text from PDF
# def input_pdf_text(uploaded_file):
#     reader = pdf.PdfReader(uploaded_file)
#     text = ""
#     for page_num in range(len(reader.pages)):
#         page = reader.pages[page_num]
#         text += str(page.extract_text())
#     return text

# # Prompt Template
# input_prompt_template = """
# Hey Act like a skilled or very experienced professional.
# resume: {text}
# description: {jd}

# I want the response in one single string having the structure:
# {{"JD Match":"%", "MissingKeywords:[], "Profile Summary":""}}
# """

# # Streamlit app
# st.title("Smart ATS")
# st.text("Improve your resume ATS")
# jd = st.text_area("Paste the job Description")
# uploaded_file = st.file_uploader("Upload your resume", type="pdf", help="Please upload the PDF")

# submit = st.button("Submit")

# if submit:
#     if uploaded_file is not None:
#         text = input_pdf_text(uploaded_file)
#         input_prompt = input_prompt_template.format(text=text, jd=jd)
#         response = get_gemini_response(input_prompt)
#         st.subheader(response)
