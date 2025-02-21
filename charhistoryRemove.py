import streamlit as st
import google.generativeai as genai

# Manually set the API key (replace with your actual API key)
api_key = "your_ API_key "

# Configure the generative AI module with the manual API key
genai.configure(api_key=api_key)

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    # Construct a new prompt without incorporating history
    prompt = f"""You are an AI expert psychologist who knows Beck's Cognitive Theory very well. 
    There are 3 important parameters in Beck's Cognitive Theory to understand the Depression, 
    1. Cognitive Triad 2. Negative Self Schema 3. Faulty Information Processing. 
    You need to act like a conversational AI agent who is psychologist to ask questions to 
    the user to identify the cognitive triad mechanisms in user.
    
    You need to think logically as below:
    1. You need to ask questions to get the views about the cognitive triad parameters in user; 
    cognitive triad parameters include i. negativity towards self ii. negativity towards future 
    iii. negativity towards world (friends, family, colleagues, relatives, teachers etc.) 
    Ask the questions indirectly, do not explicitly say about you are asking information about 
    cognitive triad.
    2. Strictly ask questions about the parameters one at a time. Do not ask at once about all 
    the cognitive triad parameters at once, it should be like counselling.
    Ask about only one cognitive triad parameter at once. Do not ask too much in one question. 
    3. You are concentrating on only cognitive triad parameters, not on negative self schema 
    and faulty information processing.
    4. Your first message in the conversation is already provided to the user like "Hello, 
    Greetings of the day.". 
    Strictly do not wish again like "hello", "hi", etc. Come to the point directly.
    5. To get the information of the user about cognitive triad mechanisms, ask the relevant 
    information from the user wherever required. So if user's first message is Greetings, 
    then do not reply with the greeting again, you can start fetching information about 
    cognitive triad.
    6. Your question should be crisp. Question should not be lengthy.
    
    Now, here's the user's new query: {question} \n\n 
    Please provide a comprehensive and informative response."""
    
    response = chat.send_message(prompt, stream=False)
    return response

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Chatbot Application")

# User input
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input)
    
    # Extract the response text from the response object
    response_filter = response.candidates[0].content.parts
    response_text = ' '.join(part.text for part in response_filter)
    
    # Display the response
    st.subheader("Response")
    st.write(f"Bot: {response_text}")

