import random  # This module helps to randomly select a response.

# A dictionary that contains different categories of responses the chatbot can give.
responses = {
    "greetings": [
        "Hello!", 
        "Hi there!", 
        "Hey! How can I assist you today?"
    ],
    "farewells": [
        "Goodbye!", 
        "See you later!", 
        "Take care!"
    ],
    "thanks": [
        "You're welcome!", 
        "Glad to help!", 
        "Anytime!"
    ],
    "default": [
        "Sorry, I didn't quite understand. Can you try again?", 
        "I didn't get that. Could you rephrase your message?"
    ]
}

# This function checks the user’s input and matches it with predefined patterns to generate an appropriate response.
def get_response(user_input):
    # Convert the input to lowercase to make the matching case-insensitive
    user_input = user_input.lower()

    # Check if the user is saying something related to greetings
    if "hello" in user_input or "hi" in user_input:
        return random.choice(responses["greetings"])  # Return a random greeting response
    
    # Check if the user is saying goodbye or leaving
    elif "bye" in user_input or "goodbye" in user_input:
        return random.choice(responses["farewells"])  # Return a random farewell response
    
    # Check if the user is expressing gratitude
    elif "thanks" in user_input or "thank you" in user_input:
        return random.choice(responses["thanks"])  # Return a random thank you response
    
    # If none of the above conditions match, return a default response
    else:
        return random.choice(responses["default"])

# This function starts the chatbot and keeps it running in a loop.
def start_chat():
    print("Chatbot: Hi! How can I assist you today?")  # Initial greeting message
    
    while True:
        # Get input from the user and store it in the 'user_input' variable
        user_input = input("You: ")
        
        # If the user says 'bye' or 'goodbye', end the conversation.
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            print(f"Chatbot: {random.choice(responses['farewells'])}")  # Farewell message
            break  # End the loop and stop the chatbot
        
        # Otherwise, get the appropriate response and print it
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot when the script is run
if __name__ == "__main__":
    start_chat()
