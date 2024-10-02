## Overview
This is a local AI chatbot that leverages the Ollama & LangChain framework to utilize advanced language models. 

## Features
- **Local AI Model Usage**: Runs on your local machine using Ollama to access AI models.
- **Custom Instructions**: Set specific instructions for the chatbot’s behavior and responses.
- **Typing Animation**: Simulates a realistic typing effect for a more engaging user experience.
- **Easy Exit**: Type `/bye` to gracefully exit the conversation.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Ollama framework installed
- Llama3.1 or any model set up and running locally.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hx-01-chatbot.git
   cd hx-01-chatbot
   ```
### Install required packages:
   ```bash
   pip install langchain-ollama
   ```
### Running the ChatBot
1. Start the Ollama service to run the model locally.
2. Execute the Python script:
    ```bash
    python usage.py
### Example Interaction
    You: What is your name?
    Bot: I am HX-01, a chatbot developed by Draky using the Llama3.1 Model.
