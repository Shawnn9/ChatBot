import unittest
from chatbot.chatbot import chatbot_response, get_weather, extract_city_from_input

class TestChatBot(unittest.TestCase):

    def test_weather_function(self):
        # Test for a valid city
        city = "London"
        response = get_weather(city)
        self.assertIn("London", response)  # Check that the response contains the city name

        # Test for an invalid city
        city = "FakeCity"
        response = get_weather(city)
        self.assertEqual(response, "Sorry, I couldn't find the weather information.")

    def test_extract_city_from_input(self):
        # Test when the input contains a city
        user_input = "What's the weather in Paris?"
        city = extract_city_from_input(user_input)
        self.assertEqual(city, "Paris")  # Ensure the city is correctly extracted

        # Test when the input doesn't contain a city
        user_input = "Tell me a joke!"
        city = extract_city_from_input(user_input)
        self.assertIsNone(city)  # Ensure None is returned when no city is found

    def test_chatbot_response(self):
        # Test a basic greeting
        response = chatbot_response("Hi")
        self.assertIn("Hello", response)  # Check that the bot replies with a greeting

        # Test asking about the weather
        response = chatbot_response("What is the weather in London?")
        self.assertIn("London", response)  # Check that the response mentions the city name

        # Test an unrecognized query
        response = chatbot_response("What is the meaning of life?")
        self.assertIn("meaning of life", response)  # Check that the response mentions the question

if __name__ == "__main__":
    unittest.main()
