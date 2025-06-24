# AI-CHATBOT-WITH-NLP

***COMPANY*** : CODTECH IT SOLUTION

***NAME*** : SYED ARMANUL HAQUE

***INTERN ID*** : CT04DN1420

***DOMAIN*** : PYTHON PROGRAMMIN

***DURATION*** : 4 WEEKS 

***MENTOR*** : NEELA SANTOSH

****This Python script implements a simple AI chatbot using the Natural Language Toolkit (NLTK), specifically leveraging the Chat and reflections utilities from the nltk.chat.util module. The chatbot is rule-based and uses pattern-matching to respond to user inputs. It simulates a conversational assistant capable of answering basic questions and chatting in natural language.The chatbot class, AIPrefixedChat, extends NLTK's built-in Chat class. It overrides the converse() method to improve user interaction. This method continuously prompts the user for input until the keyword 'bye' is entered, signaling the end of the conversation. If the input is empty, the bot politely asks the user to type something. Otherwise, it searches for a matching pattern in the predefined pairs list and responds accordingly. If no match is found, the chatbot returns a fallback message: “I didn’t understand that. Can you rephrase?”.The core of the chatbot’s logic lies in the pairs list, which contains regular expression patterns and their associated responses. Each pattern is matched against the user’s input. For example:Inputs like “hi”, “hello”, or “hey” are met with greetings.
Questions like “what is your name?” or “who are you?” trigger appropriate introductions.
If the user asks “tell me a joke”, the bot responds with a developer-themed pun.
Questions about NLTK or the bot's creator are also handled with predefined answers.
The reflections dictionary provided by NLTK handles basic pronoun transformations (like changing “I am” to “you are”), adding a touch of naturalism to the responses.
The program starts with a friendly greeting asking the user’s name. Based on the response, it customizes its reply and opens up the conversation. The user can interact freely and exit anytime by typing “bye”.

**Output**

![Image](https://github.com/user-attachments/assets/533e3785-9426-421d-9b7e-bf09026710f4)
