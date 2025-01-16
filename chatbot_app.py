import streamlit as st
from embeddings import fetch_relevant_documents
from gpt_generation import generate_response
from datetime import datetime
import yagmail  # For sending emails
from dotenv import load_dotenv
import os

# Title and description
st.title("Resume Chatbot")
st.write("Ask me about my experience, projects, and skills.")

# Initialize session state for organization name and logs
if "org_name" not in st.session_state:
    st.session_state["org_name"] = None

# Email configuration (Sender details)
SENDER_EMAIL = "jatinvarma708@gmail.com"
APP_PASSWORD = os.getenv("PASSWORD")
RECEIVER_EMAIL = "jatinvarma708@gmail.com"

# Function to create a consolidated log file
def create_consolidated_log():
    org_name = st.session_state["org_name"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temp_file = f"consolidated_session_logs_{org_name}.txt"
    with open(temp_file, "w", encoding="utf-8") as temp_log:
        temp_log.write(f"Organization: {org_name}\n")
        temp_log.write(f"Session Date: {timestamp}\n\n")
        temp_log.write("Answered Questions:\n")
        if os.path.exists("answered_questions.txt"):
            with open("answered_questions.txt", "r", encoding="utf-8") as answered_file:
                temp_log.write(answered_file.read())
        else:
            temp_log.write("No answered questions logged.\n")
        temp_log.write("\nUnanswered Questions:\n")
        if os.path.exists("unanswered_queries.txt"):
            with open("unanswered_queries.txt", "r", encoding="utf-8") as unanswered_file:
                temp_log.write(unanswered_file.read())
        else:
            temp_log.write("No unanswered questions logged.\n")
    return temp_file

# Function to send logs via email
def send_logs_via_email():
    try:
        log_file = create_consolidated_log()
        yag = yagmail.SMTP(SENDER_EMAIL, APP_PASSWORD)

        # Include organization name in the email body
        org_name = st.session_state.get("org_name", "Unknown Organization")
        email_body = (
            f"Find the consolidated session logs attached.\n\n"
            f"Organization: {org_name}\n"
        )

        yag.send(
            to=RECEIVER_EMAIL,
            subject="Session Logs: Resume Chatbot",
            contents=email_body,  # Add organization name in the body
            attachments=[log_file]
        )

        os.remove(log_file)  # Clean up temporary file
        st.success("Session logs have been sent to your email.")

        st.session_state.clear()
    except Exception as e:
        st.error(f"Failed to send logs: {str(e)}")


# Step 1: Input Organization Name (only if not already set)
if not st.session_state["org_name"]:
    org_name = st.text_input("Enter your organization's name", placeholder="Type your organization name here...")
    if st.button("Submit Organization Name"):
        if org_name:
            st.session_state["org_name"] = org_name  # Save to session state
            st.success(f"Organization name set to: {org_name}")
        else:
            st.error("Please enter your organization's name to proceed.")
else:
    # Use the stored organization name
    org_name = st.session_state["org_name"]
    st.write(f"**Welcome, {org_name}! Feel free to ask questions about my resume.**")
    
    # Step 2: Chatbot Interaction
    question = st.text_input("Your Question", placeholder="Type your question here...")
    
    if st.button("Ask"):
        if question:
            # Fetch relevant documents
            context = fetch_relevant_documents(question)
            
            # Generate GPT response
            response = generate_response(question, "\n".join(context))
            
            # Log to answered or unanswered based on response length or condition
            if len(response) >= 150:  # Condition for an answered question
                with open("answered_questions.txt", "a", encoding="utf-8") as log_file:
                    log_file.write(
                        f"{datetime.now()} | Organization: {org_name} | Query: {question} | Response: {response}\n"
                    )
            else:  # Log unanswered or vague questions
                with open("unanswered_queries.txt", "a", encoding="utf-8") as log_file:
                    log_file.write(
                        f"{datetime.now()} | Organization: {org_name} | Query: {question} | Response: {response}\n"
                    )
            
            # Display response
            st.write("### Response:")
            st.write(response)
        else:
            st.error("Please enter a question.")
    
    # Step 3: Send logs after session ends
    if st.button("End Session"):
        send_logs_via_email()
        st.info("Session ended. Logs have been sent to your email.")
