import streamlit as st
import google.generativeai as genai

# Manually set the API key (replace with your actual API key)
api_key = "your_ API_key "  # Replace with your actual API key

# Configure the generative AI module with the manual API key
genai.configure(api_key=api_key)

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")

# Start a chat session
chat = model.start_chat(history=[])

def get_gemini_response(question, history):
    # Construct a new prompt incorporating relevant history
    prompt = f"""You are an AI assistant. Here's the conversation so far: \n\n 
    {''.join([f'{role}: {text} ' for role, text in history])} \n\n 
    Now, here's the user's new query: {question} \n\n 
    Please provide a comprehensive and informative response."""

    response = chat.send_message(prompt, stream=False)
    return response

# Initialize our Streamlit app
st.set_page_config(page_title="Chatbot Demo")

st.header("BGSCET LLM Chatbot Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User input
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input, st.session_state['chat_history'])
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("User ", input))
    
    # Extract the response text from the response object
    response_filter = response.candidates[0].content.parts
    response_text = ' '.join(part.text for part in response_filter)
    st.session_state['chat_history'].append(("Bot", response_text))

# Display the chat history
st.subheader("The Chat History")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
