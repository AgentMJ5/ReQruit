import streamlit as st
from embeddings import fetch_relevant_documents
from gpt_generation import generate_response

# Title and description
st.title("Resume Chatbot")
st.write("Ask me about my experience, projects, and skills.")

# Input box for the recruiter's question
question = st.text_input("Your Question", placeholder="Type your question here...")

if st.button("Ask"):
    if question:
        # Fetch relevant documents
        context = fetch_relevant_documents(question)
        # Generate GPT response
        response = generate_response(question, "\n".join(context))
        st.write("### Response:")
        st.write(response)
    else:
        st.error("Please enter a question.")
