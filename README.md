# AI-CHATBOT-WITH-NLP

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: KOTHIMERA NEHA

*INTERN ID*: CT06DL1449

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTOSH

*TASK DESCRIPTION*: 

Objective:
The objective was to develop a simple AI-based chatbot using Natural Language Processing (NLP) techniques. The aim was to enable a chatbot to interpret user input and respond accordingly using the spaCy library, one of the most powerful and efficient NLP tools in Python. The chatbot is expected to handle basic user queries like greetings, farewells, and questions about its identity and capabilities.

Tools and Technologies Used:
Programming Language: Python

NLP Library: spaCy (en_core_web_sm model)

IDE/Editor: Visual Studio Code

Version Control & Hosting: GitHub

Environment: Command Line Interface (CLI)

Development Process:
The development began by setting up the environment. spaCy was installed using pip, and its small English language model (en_core_web_sm) was downloaded to enable the processing of English text. After setting up the NLP environment, a Python script named chatbot_spacy.py was created to serve as the chatbot engine.

The core structure of the chatbot was built around a dictionary of "intents" and corresponding "responses." Each intent represented a category of user input such as greetings, thanks, goodbyes, etc. For example, inputs like "hi", "hello", and "good morning" fall under the "greeting" intent. Responses were mapped to these intents so that the chatbot could deliver an appropriate message based on the user’s query.

spaCy was then used to tokenize and process each user input. The similarity() method was employed to compare user input with predefined examples of each intent. If the similarity score exceeded a certain threshold (in this case, 0.75), the chatbot would recognize the intent and respond accordingly. This method made the chatbot more flexible, allowing it to respond to variations in user phrasing instead of relying on exact keyword matches.

The script also included a conversation loop, which continuously accepted user input and provided responses until the user typed "exit." This interactive command-line interface allowed for real-time testing and provided a seamless user experience.

Applications and Relevance:
This task introduces a basic implementation of conversational AI, a technology that is increasingly being integrated into websites, apps, customer service, and personal assistant platforms. While the chatbot built in this task is a simple example, the underlying principle—processing and interpreting natural language using NLP—can be expanded into more complex systems capable of handling context, emotion, and even multilingual conversations.

The project also reinforced important software development concepts such as text preprocessing, intent classification, semantic similarity, and response generation. It demonstrated how even a lightweight model like en_core_web_sm in spaCy can deliver efficient results for simple chatbot functionalities.

*Output*:

![Image](https://github.com/user-attachments/assets/b4882476-930c-4ff9-818e-d0257a9ff0f8)

The final deliverable was a fully functional AI chatbot written in Python, which responds to user input using semantic similarity analysis via spaCy. The project was uploaded to GitHub as required, and the repository contains all necessary files including the script and a sample README. This task helped bridge the gap between theory and practical application in the field of NLP and conversational AI.


