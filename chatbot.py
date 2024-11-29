import nltk
import spacy
import random
import requests
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

nlp = spacy.load("en_core_web_sm")

patterns = [
    (r'hi|hello|hey|whats up', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing great, thank you!', 'I am fine, how about you?']),
    (r'what is your name?', ['I am your friendly chatbot!', 'I am a chatbot created to help you.']),
    (r'bye', ['Goodbye!', 'See you later!', 'Take care!']),
]

# Weather API patterns
weather_patterns = [
    (r'what is the weather like today?', ['Let me check the weather for you...']),
]

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

def extract_city_from_input(user_input):
    doc = nlp(user_input)
    for ent in doc.ents:
        if ent.label_ == "GPE":  
            return ent.text
    return None 

def chatbot_response(user_input):
    user_input = user_input.lower()  
    
    # Check if user is asking about the weather
    if "weather" in user_input:
        city = extract_city_from_input(user_input)
        if city:
            return get_weather(city)
        return get_weather()
    
    # Default chatbot response using NLTK patterns
    chatbot = Chat(patterns, reflections)
    return chatbot.respond(user_input)

def start_chat():
    print("Hello! I am your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        
if __name__ == "__main__":
    start_chat()
