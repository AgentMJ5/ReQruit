import openai
from document_processing import load_documents
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Fetch and print variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Preload documents and generate embeddings
documents = load_documents()
document_embeddings = [
    {
        "text": doc,
        "embedding": openai.embeddings.create(
            input=doc,
            model="text-embedding-3-small"  # Specify your preferred model
        ).data[0].embedding
    }
    for doc in documents
]

def fetch_relevant_documents(query: str):
    """
    Fetches the top 3 documents relevant to the query by calculating embedding similarity.

    Args:
        query (str): The query text to search for relevant documents.

    Returns:
        List[str]: The top 3 relevant documents.
    """
    # Generate query embedding
    query_embedding = openai.embeddings.create(
        input=query,
        model="text-embedding-3-small"  # Use the same model as document embeddings
    ).data[0].embedding

    # Calculate similarity using dot product (adjust based on requirements)
    similarities = [
        {
            "text": doc["text"],
            "similarity": sum(qe * de for qe, de in zip(query_embedding, doc["embedding"]))
        }
        for doc in document_embeddings
    ]

    # Sort documents by similarity in descending order
    sorted_docs = sorted(similarities, key=lambda x: x["similarity"], reverse=True)

    # Return the top 3 documents
    top3 = [doc["text"] for doc in sorted_docs[:3]]
    return top3