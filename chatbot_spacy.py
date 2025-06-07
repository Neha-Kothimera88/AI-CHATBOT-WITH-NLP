import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Define intents (basic categories of user messages)
intents = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "see you", "take care", "good night"],
    "thanks": ["thanks", "thank you", "thx","you are doing great"],
    "name": ["what is your name", "who are you"],
    "age": ["how old are you"],
    "function": ["what can you do", "what are your functions"],
}

# Define responses for each intent
responses = {
    "greeting": "Hello! How can I help you today?",
    "goodbye": "Goodbye! Have a nice day!",
    "thanks": "You're welcome!",
    "name": "I'm a simple chatbot built using Python and spaCy.",
    "age": "I'm timeless. But I was created recently!",
    "function": "I can respond to simple messages using NLP.",
}

def get_intent(user_input):
    doc = nlp(user_input.lower())
    for intent, examples in intents.items():
        for example in examples:
            if nlp(example).similarity(doc) > 0.75:  # Similarity threshold
                return intent
    return None

def chat():
    print("🤖 ChatBot: Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("🤖 ChatBot: Goodbye!")
            break
        intent = get_intent(user_input)
        if intent:
            print(f"🤖 ChatBot: {responses[intent]}")
        else:
            print("🤖 ChatBot: Sorry, I didn’t understand that.")

if __name__ == "__main__":
    chat()
