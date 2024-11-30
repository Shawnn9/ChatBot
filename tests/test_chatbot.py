import unittest
from chatbot.chatbot import chatbot_response

class TestChatBot(unittest.TestCase):

    def test_chatbot_response(self):
        # Test a basic greeting
        response = chatbot_response("Hi")
        self.assertIn("Hello", response)  # Check that the bot replies with a greeting

        # Test an unrecognized query
        response = chatbot_response("What is the meaning of life?")
        self.assertIn("meaning of life", response)  # Check that the response mentions the question

if __name__ == "__main__":
    unittest.main()
