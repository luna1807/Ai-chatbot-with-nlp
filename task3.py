import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize


greetings = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]
greeting_responses = ["Hello!", "Hi there!", "Hey!", "Greetings!", "Good day!"]

keywords = {
    "place": "London, paris,Mumbai",
    "time": "I'm not able to provide real time time, you can check online.",
    "how are you": "I'm doing well, thank you!",
    "bye": "Goodbye!See you soon",
    "thank you": "You're welcome!",
}

def respond(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)

    for token in tokens:
        if token in greetings:
            return greeting_responses[greetings.index(token)]

    for keyword, response in keywords.items():
        if keyword in user_input:
            return response

    return "I'm not sure how to respond to that."

print("Bot: Hello! I'm a simple AI bot. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = respond(user_input)
    print("Bot: " + response)

    if user_input.lower() == "bye":
        break
