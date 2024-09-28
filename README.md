# Minimal AI Chatbot Solution using the Ollama Service

## Project Overview
This project demonstrates a minimal AI chatbot solution that interacts with users in real time using the Ollama service. The chatbot is implemented in Python and can handle basic conversational capabilities with a large language model.

## Features
- **Real-time interaction**: The chatbot responds to user inputs in real-time.
- **Streaming responses**: The bot outputs responses progressively, enhancing user experience.
- **Environment configuration**: Uses a `.env` file for API configurations.

## Technology Stack
- **Programming Language**: Python
- **Libraries**: 
  - `requests` for HTTP requests
  - `dotenv` for environment variable management

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/adhishpathak/OllamaChatBot.git
   cd OllamaChatBot
2. Install the required packages:
    ``` bash
    pip install requests python-dotenv

3. Create a .env file in the root directory and set the following variables:

    ```plaintext
    API_URL=http://localhost:11434/api/chat
    MODEL_NAME=llama3.2

4. Run the chatbot:

    ```bash
    python chat.py

Usage
Type your message in the console and press Enter. To exit the chat, type 'exit'.

Future Enhancements
Implement user interface improvements.
Add context-based memory for better conversations.
Integrate with messaging platforms like Slack or WhatsApp.
License
This project is licensed under the MIT License.

markdown
Copy code

### Notes
- Adjust `<repository-url>` and `<repository-name>` in the README to reflect your actual GitHub repository.
- Feel free to add or modify any sections in the README to better fit your project's needs.





