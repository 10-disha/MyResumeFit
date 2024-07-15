# 📄 MyResumeFit

**MyResumeFit** is a web application that helps improve your resume for Applicant Tracking Systems (ATS). The application extracts text from your resume, compares it with a job description, and provides feedback on how well your resume matches the job description.

## ✨ Features

- 📄 Extracts text from PDF resumes.
- 🤖 Uses Google Generative AI to analyze resume and job description.
- 📊 Provides a structured response including JD match percentage, missing keywords, and a profile summary.

## 🛠 Prerequisites

Before you begin, ensure you have met the following requirements:

- 🐍 Python 3.7+ installed on your machine.
- 📦 `pip` (Python package installer) installed.
- ☁️ Google Cloud account with the Generative Language API enabled.
- 🔑 API key for the Generative Language API.

## 🚀 Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/myresumefit.git
   cd myresumefit
   ```

2. **Set Up a Virtual Environment**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. **Install the Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory of the project and add your Google API key:

   ```plaintext
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

## 📈 Usage

1. **Run the Streamlit Application**

   ```sh
   streamlit run app.py
   ```

2. **Open Your Browser**

   Open your web browser and go to `http://localhost:8501` to view the application.

3. **Use the Application**

   - Paste the job description in the provided text area.
   - Upload your resume in PDF format.
   - Click the "Submit" button to get feedback on your resume.

## 📂 Project Structure

myresumefit/
├── .env
├── .gitignore
├── app.py
├── requirements.txt
└── README.md

## 📋 Example

Below is an example of how to use the application:

1. **Paste Job Description:**

   ```plaintext
   We are looking for a skilled software engineer with experience in Python, machine learning, and cloud technologies.
   ```

2. **Upload Resume:**

   Upload your resume in PDF format.

3. **Get Feedback:**

   The application will analyze your resume and provide a structured response including JD match percentage, missing keywords, and a profile summary.

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [Google Generative AI](https://cloud.google.com/ai-platform)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)
