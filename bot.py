import random
intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey"],
        "responses": ["Hello! How can I assist you?", "Hi there! What can i do for you?"]
    },
    "farewell":{
        "patterns": ["bye", "goodbye", "see you!"],
        "responses": ["Goodbye! It was nice chatting with you!", "See you later!"]
    },
    "ask_name": {
        "patterns": ["what is your name", "what should I call you", "whats your name"],
        "responses": ["I am pyChat, you virtual assistant", "My name is pyChat"]
    }
}

def identify_intent(user_input):
    for intent, intent_data in intents.items():
        for pattern in intent_data["patterns"]:
            if pattern in user_input:
                return random.choice(intent_data["responses"])
    return "Sorry, I don't understand that."


while True:
    user_input = input("You:  ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye")
        break
    else:
        print("Bot:", identify_intent(user_input))