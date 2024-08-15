import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"My name is(.*)",
        ["Hello %1,how are you today?", ]
    ],
    [
        r"Hi|Hey|Hello",
        ["Hello","Hey there",]
    ],
    [
        r"What is your name?",
        ["I am a chatbot created by you!", ]
    ],
    [
        r"How are you ?",
        ["I'm doing well, thank you!\nHow about you?", ]
    ],
    [
        r"sorry(.*)",
        ["It's alright", "No Problem", ]
    ],
    [
        r"I'm (.*) (good|well|okay|best)",
        ["Good to know that you're %1",]
    ],
    [
        r"Quit",
        ["Bye! Take care and have a Nice day.",]
    ],
]

def chatbot():
    print("Hi, I'm your chatbot! Type 'Quit' to exit. ")
    chat = Chat(pairs, reflections)
    chat.converse()
    
chatbot()
