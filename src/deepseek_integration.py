

# Version 2.0.0 



# Version 2.0.0 (DeepSeek Edition)
import os
from dotenv import load_dotenv
import openai

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")

# Configure DeepSeek API
client = openai.OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com/v1"
)


def get_explanation(transaction):
    """
    Send a transaction row to Gemini 1.5 Flash and get an explanation.
    """
    prompt = f"""
    You are a financial fraud detection expert. Analyze the following transaction and explain in a clear and concise manner whether it could be fraudulent.

    Transaction Details:
    {transaction.to_string()}

    Provide your response in bullet points if necessary.
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating explanation: {str(e)}"
