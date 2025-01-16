from openai import OpenAI
from config import OPENAI_API_KEY

# Set the OpenAI API key
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=OPENAI_API_KEY,
)

# Function to generate GPT response
def generate_response(question: str, context: str) -> str:
    """
    Generate a response using the Chat Completions API.

    Args:
        question (str): The user's question.
        context (str): The context retrieved from documents.

    Returns:
        str: The generated response.
    """
    try:
        # Construct the messages for Chat Completions
        messages = [
            {"role": "system", "content": "You are a highly detailed and thorough assistant. Always provide complete and coherent answers to questions. Always end with a (.) after an alphabet "},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
        ]
        
        # Call the Chat Completions API
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Use 'gpt-4' for better responses if available
            messages=messages,
            max_tokens=400,
            temperature=0.5,
            stop=["EOF"]
        )

        # Extract and return the response text
        generated_text = response.choices[0].message.content.strip()

        if not generated_text.endswith((".", "?", "!", "\n")):
            follow_up_prompt = f"{generated_text} Can you continue the explanation?"
            follow_up_response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": follow_up_prompt}],
                max_tokens=200
            )
            generated_text += follow_up_response.choices[0].message.content.strip()

        return generated_text

    except Exception as e:
        return f"An error occurred while generating the response: {e}"
