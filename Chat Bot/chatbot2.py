# # Import the packages
# import streamlit as st
# import google.generativeai as genai
# from streamlit_chat import message

# # Provide the API key and configure the Generative AI model
# api_key = "AIzaSyDMDsDDs5aHpJ69pBKedgzK3_EpAIcmyfQ"
# genai.configure(api_key=api_key)
# model = genai.GenerativeModel("gemini-1.5-flash-latest")

# # Streamlit UI Parameters
# st.title("Chatbot Via Streamlit")

# # Initialize the chat history
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# if 'bot_history' not in st.session_state:
#     st.session_state['bot_history'] = []

# def generate_response(prompt):
#     # Start a chat and get the response
#     chat = model.start_chat(history=[])
#     response = chat.send_message(prompt)
#     return response.text

# # Capture user input and display bot response
# user_input = st.text_input("You: ", key="input")

# if user_input:
#     response = generate_response(user_input)
#     st.session_state['chat_history'].append(user_input)
#     st.session_state['bot_history'].append(response)
#     st.experimental_rerun()

# # Display chat history
# num_messages = min(len(st.session_state['chat_history']), len(st.session_state['bot_history']))
# for i in range(num_messages):
#     message(st.session_state['chat_history'][i], is_user=True, key=f'{i}_user', avatar_style="initials", seed="Me")
#     message(st.session_state['bot_history'][i], key=f'{i}_bot', avatar_style="initials", seed="AI")



# # Import the packages
# import streamlit as st
# import google.generativeai as genai
# from streamlit_chat import message

# # Provide the API key and configure the Generative AI model
# api_key = "AIzaSyDMDsDDs5aHpJ69pBKedgzK3_EpAIcmyfQ"
# genai.configure(api_key=api_key)
# model = genai.GenerativeModel("gemini-1.5-flash-latest")

# # Streamlit UI Parameters
# st.title("Chatbot Via Streamlit")

# # Initialize the chat history and first run flag
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []
# if 'bot_history' not in st.session_state:
#     st.session_state['bot_history'] = []
# if 'first_run' not in st.session_state:
#     st.session_state['first_run'] = True

# def generate_response(prompt):
#     # Start a chat and get the response
#     chat = model.start_chat(history=[])
#     response = chat.send_message(prompt)
#     return response.text

# # Check if it's the first run and send the default prompt
# if st.session_state['first_run']:
#     default_prompt = """I have an interview i want you act as my interviewer for 'data science' role take my mock interview follow the instructions. 
#     1. ask me atleast 10 questions one by one after asking one question give me time to response for that question.
#     2. after my response do not elobrate or explain the answer just ask the next question.
#     3. at last after all question you asked then give me the number assume that each question have 1 mark if i give right answer give me 1 mark otherwise 0.
#     if you understand that drill just type "OK" and start asking me questions  """
#     response = generate_response(default_prompt)
#     st.session_state['chat_history'].append(default_prompt)
#     st.session_state['bot_history'].append(response)
#     st.session_state['first_run'] = False
#     st.experimental_rerun()

# # Capture user input and display bot response
# user_input = st.text_input("You: ", key="input")

# if user_input:
#     response = generate_response(user_input)
#     st.session_state['chat_history'].append(user_input)
#     st.session_state['bot_history'].append(response)
#     st.experimental_rerun()

# # Display chat history
# num_messages = min(len(st.session_state['chat_history']), len(st.session_state['bot_history']))
# for i in range(num_messages):
#     message(st.session_state['chat_history'][i], is_user=True, key=f'{i}_user', avatar_style="initials", seed="Me")
#     message(st.session_state['bot_history'][i], key=f'{i}_bot', avatar_style="initials", seed="AI")




# 33333

# # Import the packages
# import streamlit as st
# import google.generativeai as genai
# from streamlit_chat import message

# # Provide the API key and configure the Generative AI model
# api_key = "AIzaSyDMDsDDs5aHpJ69pBKedgzK3_EpAIcmyfQ"
# genai.configure(api_key=api_key)
# model = genai.GenerativeModel("gemini-1.5-flash-latest")

# # Streamlit UI Parameters
# st.title("Data Science Mock Interview")

# # Initialize session state
# if 'questions' not in st.session_state:
#     st.session_state['questions'] = [
#         "What is the difference between supervised and unsupervised learning?",
#         "Can you explain what a neural network is?",
#         "What is overfitting and how can you prevent it?",
#         "Explain the concept of cross-validation.",
#         "What is a confusion matrix?",
#         "How do you handle missing data in a dataset?",
#         "What is the bias-variance tradeoff?",
#         "Explain the difference between classification and regression.",
#         "What is a ROC curve?",
#         "Can you describe a time when you had to use data science to solve a business problem?"
#     ]
#     st.session_state['current_question'] = 0
#     st.session_state['responses'] = []
#     st.session_state['scores'] = []
#     st.session_state['interview_started'] = False

# def generate_response(prompt):
#     chat = model.start_chat(history=[])
#     response = chat.send_message(prompt)
#     return response.text

# # Function to ask the next question
# def ask_next_question():
#     if st.session_state['current_question'] < len(st.session_state['questions']):
#         question = st.session_state['questions'][st.session_state['current_question']]
#         st.session_state['current_question'] += 1
#         return question
#     else:
#         return None

# # Start the interview
# if not st.session_state['interview_started']:
#     initial_prompt = "I have an interview i want you act as my interviewer for 'data science' role take my mock interview follow the instructions. \n\
#     1. ask me atleast 10 questions one by one after asking one question give me time to response for that question. \n\
#     2. after my response do not elobrate or explain the answer just ask the next question. \n\
#     3. at last after all question you asked then give me the number assume that each question have 1 mark if i give right answer give me 1 mark otherwise 0. \n\
#     if you understand that drill just type 'OK' and start asking me questions"
#     response = generate_response(initial_prompt)
#     st.session_state['bot_history'].append(response)
#     st.session_state['interview_started'] = True
#     st.experimental_rerun()

# # Display the initial prompt response
# if st.session_state['bot_history']:
#     message(st.session_state['bot_history'][-1], key='initial_response')

# # Capture user input and display the next question
# user_input = st.text_input("You: ", key="input")

# if user_input:
#     st.session_state['responses'].append(user_input)
#     next_question = ask_next_question()
#     if next_question:
#         message(next_question, key=f'question_{st.session_state["current_question"]}')
#     else:
#         # Interview finished, calculate the score
#         score = sum(1 for response in st.session_state['responses'] if response.lower() == "ok")
#         st.session_state['scores'].append(score)
#         st.write(f"Interview finished. Your score is: {score}/{len(st.session_state['questions'])}")
#     st.experimental_rerun()

# # Display chat history
# for i, response in enumerate(st.session_state['responses']):
#     message(response, is_user=True, key=f'{i}_user', avatar_style="initials", seed="Me")
#     if i < len(st.session_state['questions']):
#         message(st.session_state['questions'][i], key=f'question_{i}', avatar_style="initials", seed="AI")



# 444444



# Import the packages
import streamlit as st
import google.generativeai as genai
from streamlit_chat import message

# Provide the API key and configure the Generative AI model
api_key = "AIzaSyDMDsDDs5aHpJ69pBKedgzK3_EpAIcmyfQ"
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# Streamlit UI Parameters
st.title("Data Science Mock Interview")

# Initialize session state
if 'questions' not in st.session_state:
    st.session_state['questions'] = [
        "What is the difference between supervised and unsupervised learning?",
        "Can you explain what a neural network is?",
        "What is overfitting and how can you prevent it?",
        "Explain the concept of cross-validation.",
        "What is a confusion matrix?",
        "How do you handle missing data in a dataset?",
        "What is the bias-variance tradeoff?",
        "Explain the difference between classification and regression.",
        "What is a ROC curve?",
        "Can you describe a time when you had to use data science to solve a business problem?"
    ]
    st.session_state['current_question'] = 0
    st.session_state['responses'] = []
    st.session_state['bot_history'] = []
    st.session_state['interview_started'] = False

def generate_response(prompt):
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)
    return response.text

# Function to ask the next question
def ask_next_question():
    if st.session_state['current_question'] < len(st.session_state['questions']):
        question = st.session_state['questions'][st.session_state['current_question']]
        st.session_state['current_question'] += 1
        return question
    else:
        return None

# Start the interview
if not st.session_state['interview_started']:
    initial_prompt = "I have an interview i want you act as my interviewer for 'data science' role take my mock interview follow the instructions. \n\
    1. ask me at least 10 questions one by one after asking one question give me time to respond to that question. \n\
    2. after my response do not elaborate or explain the answer just ask the next question. \n\
    3. at last after all questions you asked then give me the number assume that each question has 1 mark if I give the right answer give me 1 mark otherwise 0. \n\
    if you understand that drill just type 'OK' and start asking me questions"
    response = generate_response(initial_prompt)
    st.session_state['bot_history'].append(response)
    st.session_state['interview_started'] = True
    st.experimental_rerun()

# Display the initial prompt response
if st.session_state['bot_history'] and st.session_state['current_question'] == 0:
    message(st.session_state['bot_history'][-1], key='initial_response')

# Capture user input and display the next question
user_input = st.text_input("You: ", key="input")

if user_input:
    st.session_state['responses'].append(user_input)
    next_question = ask_next_question()
    if next_question:
        st.session_state['bot_history'].append(next_question)
        st.experimental_rerun()
    else:
        # Interview finished, calculate the score
        score = sum(1 for response in st.session_state['responses'] if response.lower() == "ok")
        st.write(f"Interview finished. Your score is: {score}/{len(st.session_state['questions'])}")
    
# Display chat history
for i in range(len(st.session_state['responses'])):
    message(st.session_state['responses'][i], is_user=True, key=f'{i}_user', avatar_style="initials", seed="Me")
    if i < len(st.session_state['questions']):
        message(st.session_state['questions'][i], key=f'question_{i}', avatar_style="initials", seed="AI")



