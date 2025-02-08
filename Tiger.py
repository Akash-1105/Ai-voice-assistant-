import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import requests
import json

# Initialize Text-to-Speech 
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get voice input
def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return ""

# Introduction
speak("Hello, I am Tiger, your AI assistant. How may I assist you today?")

while True:
    query = get_voice_input().lower()

    # Open Browser
    if 'open browser' in query:
        speak("Opening browser...")
        webbrowser.open("https://www.google.com")

    # Introduce itself
    elif 'introduce yourself' in query:
        speak("Hello, I am Tiger, an artificial intelligence language model Made by Akash Saxena to simulate conversation, answer questions, and perform tasks for users like you.")

    # Play Favourite Song (Local File)
    elif 'play my favourite song' in query:
        speak("Playing your favourite song...")
        pygame.mixer.init()
        pygame.mixer.music.load("song.mp3")
        pygame.mixer.music.play()

    # Play Song on YouTube
    elif 'play on youtube' in query:
        speak("Please provide the song name or artist to search on YouTube...")
        song_name = get_voice_input().replace(" ", "+")
        url = f"https://www.youtube.com/results?search_query={song_name}"
        speak(f"Searching for {song_name} on YouTube...")
        webbrowser.open(url)
    elif 'play youtube' in query:
        speak("Please provide the youtu.be link or song name to play on YouTube...")
        youtube_query = get_voice_input()
        if 'youtu.be' in youtube_query:
            speak("Playing the video on YouTube...")
            webbrowser.open(f"https://{youtube_query}")
        else:
            url = f"https://www.youtube.com/results?search_query={youtube_query.replace(' ', '+')}"
            speak(f"Searching for {youtube_query} on YouTube...")
            webbrowser.open(url)

    # Search on Google
    elif 'search on google' in query or 'google search' in query:
        speak("What would you like to search on Google?")
        google_query = get_voice_input().replace(" ", "+")
        url = f"https://www.google.com/search?q={google_query}"
        speak(f"Searching for {google_query} on Google...")
        webbrowser.open(url)
    elif 'google something' in query:
        speak("Please provide what you'd like to search on Google...")
        google_something = get_voice_input().replace(" ", "+")
        url = f"https://www.google.com/search?q={google_something}"
        speak(f"Searching for {google_something} on Google...")
        webbrowser.open(url)

    # Tell Time
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")


    # Exit
    elif 'exit' in query or 'offline' in query:
        speak("It was nice assisting you. Goodbye!")
        break

    else:
        speak("I didn't quite catch that. Could you please repeat?")
