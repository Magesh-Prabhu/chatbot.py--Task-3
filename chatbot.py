import nltk
import random
import string

from nltk.chat.util import Chat, reflections
from nltk.corpus import stopwords

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Define some basic patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot created by Magesh.", "You can call me Chatty."]
    ],
    [
        r"how are you ?",
        ["I'm doing great, thank you!", "All good! How about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's okay!", "No problem at all."]
    ],
    [
        r"i'm (.*) doing good",
        ["Great to hear that!", "Awesome!"]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm a virtual being. I exist everywhere and nowhere."]
    ],
    [
        r"how (.*) weather (.*)",
        ["I'm not connected to the internet, but I hope it's nice!"]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I can help you. Please tell me your query."]
    ],
    [
        r"quit",
        ["Bye! Have a great day!", "Goodbye!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase?"]
    ]
]

# Create and launch the chatbot
def chatbot():
    print("Hi, I'm your chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
