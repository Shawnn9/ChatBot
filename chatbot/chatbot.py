import nltk
import random
import requests
import time
from nltk.chat.util import Chat, reflections
from textblob import TextBlob
from googlesearch import search
import json
from cryptography.fernet import Fernet  # Add this import

# Download the required NLTK datasets
nltk.download('punkt')

# The encryption key (ensure this is correct)
key = b'VeszHauMVwweVvYTD9slfzhai9rvuKbVAH16LEw7_ts='  # Encryption key
cipher_suite = Fernet(key)

# Read and decrypt the encrypted file containing questions and answers
with open("chatbot/questions_encrypted.json", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

# Decrypt the data
decrypted_data = cipher_suite.decrypt(encrypted_data)

# Convert the decrypted data back to JSON format
questions_data = json.loads(decrypted_data.decode("utf-8"))

# Define patterns from the decrypted data
patterns = [(r'{}'.format(q['question']), q['answer']) for q in questions_data]

# Function to analyze sentiment
def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "You seem happy!"
    elif sentiment < 0:
        return "You seem sad, is everything okay?"
    else:
        return "You seem neutral."

# Function to perform a Google search
def google_search(query):
    results = search(query, num_results=1)
    return f"I found this for you: {results[0]}"

# Main function to generate chatbot responses
def chatbot_response(user_input):
    user_input = user_input.lower()  

    # Check if user wants sentiment analysis
    if "how do i feel" in user_input:
        return get_sentiment(user_input)
    
    # Check if user wants to search something on Google
    if "search" in user_input or "google" in user_input:
        return google_search(user_input)

    # Default chatbot response using NLTK patterns
    chatbot = Chat(patterns, reflections)
    return chatbot.respond(user_input)

# Function to start the chatbot conversation
def start_chat():
    print("Hello! I am your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot_response(user_input)
        print("Chatbot:", response)

# Main entry point
if __name__ == "__main__":
    start_chat()
