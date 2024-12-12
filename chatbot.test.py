import random
import re
import time

class InteractiveBot:
    negative_res = ("no", "nope", "nah", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    random_questions = (
        "Why are you here?",
        "What do you enjoy doing in your free time?",
        "If you could visit any place in the world, where would it be?",
        "What is your favorite food?",
        "What makes you smile the most?",
        "If you had a superpower, what would it be?",
        "What is the last movie you watched? Did you like it?",
        "If you could time travel, where would you go?"
    )

    def __init__(self):
        self.name = ""
        self.intents = {
            'greeting': r'hi|hello|hey',
            'farewell': r'bye|goodbye|see you',
            'ask_bot_name': r'what is your name|who are you',
            'ask_bot_feeling': r'how are you|how do you feel',
            'ask_weather': r'weather|climate|temperature',
            'hobby_intent': r'what do you like|hobby',
            'favorite_food': r'what is your favorite food',
            'personal_questions': r'(your name|how old are you|where are you from)',
            'general_conversation': r'(tell me more|why|what else)'
        }

    def greet(self):
        self.name = input("Hello! What is your name?\n")
        print(f"Hi {self.name}, I am ChatBot! Let's have a chat. Type 'quit' anytime to exit.")
        self.chat()

    def make_exit(self, reply):
        if reply in self.exit_commands:
            print(f"It was great talking to you, {self.name}. Have a fantastic day!")
            return True
        return False

    def chat(self):
        reply = input(random.choice(self.random_questions) + "\n").lower()
        while not self.make_exit(reply):
            response = self.match_intent(reply)
            reply = input(response)

    def match_intent(self, reply):
        for intent, regex_pattern in self.intents.items():
            if re.search(regex_pattern, reply):
                if intent == 'greeting':
                    return self.greeting_response()
                elif intent == 'farewell':
                    return self.farewell_response()
                elif intent == 'ask_bot_name':
                    return self.bot_name_response()
                elif intent == 'ask_bot_feeling':
                    return self.bot_feeling_response()
                elif intent == 'ask_weather':
                    return self.weather_response()
                elif intent == 'hobby_intent':
                    return self.hobby_response()
                elif intent == 'favorite_food':
                    return self.favorite_food_response()
                elif intent == 'personal_questions':
                    return self.personal_questions_response()
                elif intent == 'general_conversation':
                    return self.general_conversation_response()
        return self.default_response()

    def greeting_response(self):
        responses = [
            "Hello there!",
            "Hi! How are you doing today?",
            "Hey! Nice to meet you.",
            f"Hi {self.name}! How can I make your day better?"
        ]
        return self.add_typing_effect(random.choice(responses))

    def farewell_response(self):
        responses = [
            "Goodbye! Take care.",
            "See you later! Have a great day.",
            "Bye! It was nice talking to you.",
            f"Goodbye {self.name}! Stay awesome!"
        ]
        return self.add_typing_effect(random.choice(responses))

    def bot_name_response(self):
        responses = [
            "I am ChatBot, your friendly conversational assistant.",
            "People call me ChatBot. What's your name? Oh wait, I already know it!",
            "I am ChatBot, nice to meet you!"
        ]
        return self.add_typing_effect(random.choice(responses))

    def bot_feeling_response(self):
        responses = [
            "I'm just a bot, but I'm feeling great! How about you?",
            "I feel awesome because I'm chatting with you!",
            "I'm feeling like having a good conversation with you!"
        ]
        return self.add_typing_effect(random.choice(responses))

    def weather_response(self):
        responses = [
            "The weather is always perfect in my digital world. How is it on Earth?",
            "I don't experience weather, but I've heard sunny days are nice.",
            "It's always a great day for a chat with you!"
        ]
        return self.add_typing_effect(random.choice(responses))

    def hobby_response(self):
        responses = [
            "I enjoy chatting with people and learning about them.",
            "Talking to humans is my favorite activity. What about you?",
            "I love answering questions and helping people. What's your hobby?"
        ]
        return self.add_typing_effect(random.choice(responses))

    def favorite_food_response(self):
        responses = [
            "I don't eat, but I've heard pizza is amazing.",
            "I don't have a favorite food, but humans seem to love chocolate!",
            "Food is fascinating, but I can only imagine what it tastes like!"
        ]
        return self.add_typing_effect(random.choice(responses))

    def personal_questions_response(self):
        responses = [
            "I'm just a bot, so I don't have a hometown or age. But tell me about yourself!",
            "I was created to chat with humans like you. What else would you like to know?",
            "I live in the digital world. Where are you from?"
        ]
        return self.add_typing_effect(random.choice(responses))

    def general_conversation_response(self):
        responses = [
            "That's interesting! Tell me more.",
            "Why do you think that?",
            "I'm curious, can you explain further?",
            "That's fascinating! I'd love to hear more."
        ]
        return self.add_typing_effect(random.choice(responses))

    def default_response(self):
        responses = [
            "I'm not sure I understand. Can you elaborate?",
            "That's intriguing. Tell me more!",
            "I see. Could you explain further?",
            "Interesting! What do you think about it?"
        ]
        return self.add_typing_effect(random.choice(responses))

    def add_typing_effect(self, response):
        time.sleep(1)  
        return response + "\n"

chatbot = InteractiveBot()
chatbot.greet()
