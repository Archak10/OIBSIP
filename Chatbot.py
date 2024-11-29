from tkinter import *
import random

# Function to handle user input and generate bot response
def respond():
    user_input = user_input_field.get()
    user_input = user_input.lower()

    # Enhanced predefined responses
    responses = {
        "hello": "Hey there! How can I assist you today?",
        "hi": "Greetings! How can I help you?",
        "how are you": "I'm doing well, thank you for asking! How about you?",
        "i'm fine": "Thats awesome! I'm happy to hear you're doing well!",
        "bye": "Farewell! Wishing you a wonderful day ahead!",
        "your name": "I am an AI created to assist you in whatever way I can!",
        "what is your purpose": "I was designed to answer your questions and assist with any information you need",
        "what can you do": "I can chat with you,provide information and help you solve problems!",
        "who created you": "A talented team of developers bought me to life to help you out!",
        "what is the weather": "Sorry, I am unable to check the weather at the moment.You can use an app or website to get the latest update",
        "tell me a joke": "Why don’t eggs tell jokes? They might crack up!",
        "what is your favorite color": "I don't have a favorite color, but I think each one is beautiful and unique in its own way!",
        "what is the time": "I can't have access to time, but you can check your device for the curent time!.",
        "do you like music": "Music is amazing! It has the power to bring people together and evoke deep emotions.",
        "what is the capital of france": "The capital of France is Paris,the City of Lights!.",
        "what is 2+2": "10+10 is 20.",
        "what is the meaning of life": "The meaning of life is a big question!Some think it's about finding love, others about seeking happiness and purpose.",
        "what is your favorite food": "I don't eat, but many people love a good slice of pizza!",
        "how old are you": "I don't have an age like humans, but I’m constantly learning and evolving!",
        "tell me something interesting": "Did you know that octopuses have three hearts? One pumps blood to their body, and the other two pump it to their gills!",
        "can you help me": "Absolutely! I'm here to assist with anything you need. Just let me know!",
        "how do you work": "I use artificial intelligence to understand and respond to your questions based on patterns and data.",
        "tell me a story": "Once upon a time, a curious fox wandered into a magical forest, where every tree could talk and share ancient stories. One tree told him of a treasure hidden deep within the forest."
    }

    # If the user's input matches a predefined response, return that response
    for key in responses:
        if key in user_input:
            bot_response = responses[key]
            break
    else:
        # If no match is found, return a random response
        bot_response = random.choice([
            "Sorry, I didn't understand that.",
            "Can you please rephrase your question?",
            "I'm not sure about that. Can you ask something else?",
            "I am still learning, so I might not know the answer to that."
        ])
    
    # Display the response in the chat box
    chat_box.insert(END, "You: " + user_input + "\n")
    chat_box.insert(END, "Bot: " + bot_response + "\n")
    chat_box.yview(END)  # Scroll to the bottom to show the latest conversation

    # Clear the input field
    user_input_field.delete(0, END)

# Setting up the Tkinter window
root = Tk()
root.title("Chatbot")
root.geometry("400x500")

# Creating the chat box to display conversation
chat_box = Text(root, height=20, width=50, bd=2, font=("Arial", 12))
chat_box.pack(padx=10, pady=10)

# Creating the user input field
user_input_field = Entry(root, width=50, font=("Arial", 12))
user_input_field.pack(padx=10, pady=10)

# Creating the send button
send_button = Button(root, text="Send", font=("Arial", 12), command=respond)
send_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()