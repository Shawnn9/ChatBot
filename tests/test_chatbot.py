import unittest
from chatbot.chatbot import chatbot_response

class TestChatBot(unittest.TestCase):

    def test_chatbot_response(self):
        response = chatbot_response("Hi")
        self.assertTrue(any(greeting in response for greeting in ["Hello", "Hi there", "Hey!"]))  # Check for any greeting in the response
        
        # Test an unrecognized query
        response = chatbot_response("What is the meaning of life?")
        self.assertIn("meaning of life", response)  # Check that the response mentions the question

if __name__ == "__main__":
    unittest.main()
