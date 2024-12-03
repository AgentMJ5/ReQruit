import openai
import streamlit as st
from document_processing import load_documents
from config import OPENAI_API_KEY

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY

# Preload documents and generate embeddings
documents = load_documents()
document_embeddings = [
    {
        "text": doc,
        "embedding": openai.Embedding.create(
            input=doc,
            model="text-embedding-3-small"
        )["data"][0]["embedding"]
    }
    for doc in documents
]

# Fetch relevant documents based on query
def fetch_relevant_documents(query: str):
    # Generate query embedding
    query_embedding = openai.Embedding.create(
        input=query,
        model="text-embedding-3-small"
    )["data"][0]["embedding"]

    # Calculate similarity (placeholder logic, replace with a proper method)
    similarities = [
        {"text": doc["text"], "similarity": sum(qe * de for qe, de in zip(query_embedding, doc["embedding"]))}
        for doc in document_embeddings
    ]

    # Sort by similarity and return top documents
    sorted_docs = sorted(similarities, key=lambda x: x["similarity"], reverse=True)
    top3 = [doc["text"] for doc in sorted_docs[:3]]  # Return top 3 matches
    return top3
