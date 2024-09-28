import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_URL = os.getenv('API_URL')
MODEL_NAME = os.getenv('MODEL_NAME')

def ask_bot(messages):
    try:
        # Send the POST request to the chat endpoint with streaming enabled
        response = requests.post(API_URL, json={
            "model": MODEL_NAME,
            "messages": messages,
            "stream": True  # Enable streaming
        }, stream=True)

        # Check for a successful response
        if response.status_code == 200:
            full_response = ""

            # Stream response line by line
            print("Bot: ", end='', flush=True)  # Print "Bot: " only once
            for line in response.iter_lines():
                if line:
                    line_data = line.decode('utf-8').strip()
                    try:
                        json_data = requests.Response()
                        json_data._content = line_data.encode('utf-8')
                        message_content = json_data.json().get('message', {}).get('content', '')

                        if message_content:
                            full_response += message_content
                            print(message_content, end='', flush=True)

                    except ValueError as e:
                        print(f"\nError parsing JSON: {e}")

            print()
            return {"status": True, "data": {"answer": full_response.strip()}, "message": ''}
        else:
            return {
                "status": False,
                "data": {},
                "message": f"Error: {response.status_code}"
            }

    except Exception as e:
        return {
            "status": False,
            "data": {},
            "message": f"An error occurred: {str(e)}"
        }

if __name__ == "__main__":
    print("Chatbot (type 'exit' to end the conversation)")
    messages = []

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Ending chat. Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})
        result = ask_bot(messages)

        if result['status']:
            messages.append({"role": "assistant", "content": result['data']['answer']})
        else:
            print(f"Bot: {result['message']}")
