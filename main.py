import header.title
from openai import OpenAI, APIError

# Enter your OpenAI API key here
API_KEY = "YOUR_API_KEY_HERE"

# Connect to OpenAI
client = OpenAI(api_key=API_KEY)

previous_response_id = None

print("=" * 40)
print("       Python ChatGPT")
print("=" * 40)
print("Type 'exit' to quit.")
print("Type 'new' to start a new conversation.")
print()

