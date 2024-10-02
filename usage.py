import time
from langchain_ollama.llms import OllamaLLM

# Initialize LLM
ollama = OllamaLLM(base_url='http://localhost:11434', model='llama3.1')

# Custom instructions for the bot
instructions = '''
        You are a ChatBot named HX-01 developed by Draky using the Llama3.1 Model. 
        If asked about on how many parameters you are trained of you can say 8B.
        Your goal is to provide correct and accurate information to the user.

    '''

# Store conversation
conversation_history = [instructions]

# Typing effect
def typing_animation(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # New line

for x in range(10):
    inp = input("You: ")
    
    # Exit condition
    if inp.lower() == '/bye':
        print("Bot: Goodbye!")
        break
    
    # Add user input
    conversation_history.append(f"You: {inp}")
    
    # Combine conversation
    full_conversation = "\n".join(conversation_history)
    
    # Get bot response
    bot_response = ollama.invoke(full_conversation)
    
    # Show bot typing
    print("Bot: ", end='')
    typing_animation(bot_response)
    
    # Add bot response
    conversation_history.append(f"Bot: {bot_response}")
