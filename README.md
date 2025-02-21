# chatbot
LLM Chatbot with Streamlit, Google Generative AI, and Python Dotenv
Overview

This project demonstrates how to create a simple chatbot application using Streamlit and Google Generative AI APIs. The chatbot will leverage Google’s powerful language models to generate responses based on user input. Additionally, the Python dotenv package is used to securely manage environment variables, such as API keys, for seamless integration.

Features

    Chat Interface: Users can interact with the chatbot through a simple web-based interface built using Streamlit.
    Generative AI: The chatbot uses Google Generative AI to produce natural language responses.
    Environment Variables: Sensitive information like API keys is stored securely using Python's dotenv.

Prerequisites

    Python 3.7 or higher
    A Google Cloud account with access to the Generative AI API
    Required API keys for Google Cloud services
    A virtual environment (optional but recommended)

Installation

Follow these steps to get the chatbot running locally.
1. Clone the repository

git clone https://github.com/your-username/llm-chatbot.git
cd llm-chatbot

2. Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install dependencies

Install the necessary libraries using pip:

pip install -r requirements.txt

requirements.txt includes:

    streamlit: For creating the web app interface.
    google-generativeai: For interacting with Google's Generative AI.
    python-dotenv: For managing environment variables.

4. Set up environment variables

Create a .env file in the root of the project and add your Google API credentials:

GOOGLE_API_KEY=your_google_api_key_here

Make sure you have the correct API key from Google Cloud and have enabled the necessary API services.
5. Run the application

After setting everything up, you can run the app with:

streamlit run app.py

This command will start a local Streamlit server and open the chatbot interface in your browser.
