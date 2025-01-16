### ReQruit: AI-Powered Resume Chatbot
ReQruit is an AI-powered chatbot designed to help recruiters interactively explore a candidate's resume. With natural language processing (NLP) capabilities, ReQruit answers questions about your skills, experience, and projects, making it easier for recruiters to evaluate your profile.

Key Features
Interactive Chatbot:

Recruiters can ask questions like, "Why should we hire you?" or "Tell me about your projects," and receive detailed responses.
Customizable Context:

Answers are strictly based on the content of your resume, ensuring relevant and accurate responses.
Log Management:

Records recruiter queries (answered and unanswered) for future analysis and improvements.
Email Integration:

Automatically emails session logs for documentation and review.
How It Works
Resume Parsing:

ReQruit extracts and processes information from your resume files (.docx and .pdf).
Question-Answering:

Using OpenAI's GPT model, the chatbot generates precise answers based on the parsed resume content.
Logs and Reporting:

Recruiter queries and responses are logged in separate files (answered_questions.txt and unanswered_queries.txt).
Logs are sent to the candidate via email at the end of each session.
Tech Stack
Backend: Python
Frontend: Streamlit
AI Models: OpenAI GPT-4
Email Integration: Yagmail
Resume Processing: python-docx, PyPDF2
Setup Instructions
Prerequisites
Python 3.8 or higher
OpenAI API Key
Google App Password for email integration
Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/AgentMJ5/ReQruit.git
cd ReQruit
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file for environment variables:

plaintext
Copy
Edit
OPENAI_API_KEY=your_openai_api_key
SENDER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_google_app_password
RECEIVER_EMAIL=your_email@gmail.com
Add your resume files (.docx or .pdf) to the data/ directory.

Usage
Run the application:

bash
Copy
Edit
streamlit run chatbot_app.py
Open the app in your browser (default: http://localhost:8501).

Enter your organization name and start asking questions about your resume.

End the session to receive an email with the consolidated session logs.

Example Questions
Why should we hire you?
Tell me about your projects.
What skills do you bring to the table?
Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch:
bash
Copy
Edit
git checkout -b feature-name
Commit your changes:
bash
Copy
Edit
git commit -m "Add feature-name"
Push to the branch:
bash
Copy
Edit
git push origin feature-name
Open a pull request.

Contact
For questions or suggestions, contact me via LinkedIn or email at jatinvarma708@gmail.com.

