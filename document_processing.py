import os
from typing import List
from docx import Document
import PyPDF2

# Extract text from DOCX files
def extract_text_from_docx(file_path: str) -> str:
    doc = Document(file_path)
    return "\n".join([paragraph.text for paragraph in doc.paragraphs])

# Extract text from PDF files
def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Process all files in the data directory
def load_documents(directory: str = "data/") -> List[str]:
    texts = []
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if file_name.endswith(".docx"):
            texts.append(extract_text_from_docx(file_path))
        elif file_name.endswith(".pdf"):
            texts.append(extract_text_from_pdf(file_path))
        else:
            print(f"Unsupported file format: {file_name}")
    return texts
