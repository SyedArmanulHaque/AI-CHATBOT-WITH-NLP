import nltk
from nltk.chat.util import Chat, reflections

class AIPrefixedChat(Chat):
    def converse(self, quit="bye"):
        user_input = ""
        while user_input.lower() != quit:
            try:
                user_input = input("You: ")
            except EOFError:
                print()
                break
            if user_input.strip():
                response = self.respond(user_input)
                if response:
                    print("AI ChatBot:", response)
                else:
                    print("AI ChatBot: I didn’t understand that. Can you rephrase?")
            else:
                print("AI ChatBot: Please type something.")

# List of pattern-response pairs
pairs = [
    [r'hi|hello|hey', ['Hello! How can I assist you today?', 'Hi there! Need any help?']],
    [r'what is your name\??', ['I am a chatbot built with NLTK.']],
    [r'who are you\??', ['I am an AI assistant here to help you with your queries.']],
    [r'how are you\??', ['I am doing well, thanks! How about you?']],
    [r'.*your name.*', ['People call me the NLTK Chatbot.']],
    [r'help(.*)', ['I am here to help! Just ask me anything.']],
    [r'who created you\??', ['I was created by a Python programmer using the NLTK library.']],
    [r'what is nltk\??', ['NLTK stands for Natural Language Toolkit — a Python library for NLP.']],
    [r'tell me a joke', ['Why did the developer go broke? Because he used up all his cache!']],
    [r'what can you do\??', ['I can answer simple questions, chat with you, and tell jokes!']],
    [r'which language do you understand\??', ['I understand and respond in English.']],
    [r'bye|goodbye', ['Goodbye! It was nice chatting with you.', 'Nice to have a talk with you. Take care!']]
]

# Start the chatbot
print("AI ChatBot: Hello! I'm your AI assistant. What’s your name?")
user_name = input("You: ").strip()

if user_name:
    print(f"AI ChatBot: Nice to meet you, {user_name}! Ask me anything, or type 'bye' to exit.")
else:
    print("AI ChatBot: No worries, feel free to start chatting or type 'bye' to exit.")

chatbot = AIPrefixedChat(pairs, reflections)
chatbot.converse()

