import nltk
import random
import requests
import time
from nltk.chat.util import Chat, reflections
from textblob import TextBlob
from googlesearch import search
import json

# Download the required NLTK datasets
nltk.download('punkt')

# Load the decrypted questions and answers from the file
with open("questions_decrypted.json", "r") as file:
    questions_data = json.load(file)

# Define patterns from the decrypted data
patterns = [(r'{}'.format(q['question']), q['answer']) for q in questions_data]

# Function to get weather information
def get_weather(city="London"):
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if data["cod"] == "404":
        return "Sorry, I couldn't find the weather information."
    else:
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temp = main["temp"]
        return f"The current temperature in {city} is {temp}°C with {weather_desc}."

# Function to extract city name from user input using basic string matching
def extract_city_from_input(user_input):
    cities = ["London", "New York", "Paris", "Tokyo", "Berlin", "Los Angeles", "Sydney", "Moscow", "Rome"]
    for city in cities:
        if city.lower() in user_input.lower():
            return city
    return None 

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

    # Check if user is asking about the weather
    if "weather" in user_input:
        city = extract_city_from_input(user_input)
        if city:
            return get_weather(city)
        return get_weather()
    
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
