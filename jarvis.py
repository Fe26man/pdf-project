import speech _recognition as sr
import openai
import pyttsx3
import webbrowser
import datetime
import os
import wikipedia

# Initialize pyttsx3 engine for voice output
engine = pyttsx3.init()

# OpenAI API key (Replace with your API key)
openai.api_key = 'your-openai-api-key'


# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to recognize speech from microphone
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Sorry, I could not understand. Please repeat.")
            return "None"
        return query


# Function to interact with OpenAI GPT
def chat_with_gpt(query):
    response = openai.Completion.create(
        model="text-davinci-003",  # Use 'gpt-4' if you have access
        prompt=query,
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']


# Main function to run the voice assistant
def voice_assistant():
    speak("Hello! welcome anurag sir    how can i help u ")

    while True:
        query = take_command().lower()

        # Exit the assistant
        if "exit" in query or "quit" in query:
            speak("Goodbye anurag sir  !")
            break

        # Open a website
        elif "open youtube" in query:
            speak("yes sir Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            speak("yes sir Opening Google.")
            webbrowser.open("https://www.google.com")

        elif "open chat gpt" in query:
            speak("yes sir Opening chat gtp.")
            webbrowser.open("https://www.chatgpt.com")

        elif "open w3school" in query:
            speak("yes sir Opening w3school.")
            webbrowser.open("https://www.w3schools.com")

        # Tell the time
        elif "time" in query:
            str_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {str_time}")

        # Reset chat history (Optional feature)
        elif "reset chat" in query:
            chat_history = ""
            speak("Chat history reset.")

        # Use OpenAI to chat
        else:
            response = chat_with_gpt(query)
            print(f"GPT-3: {response}")
            speak(response)


if __name__ == "__main__":
    voice_assistant()