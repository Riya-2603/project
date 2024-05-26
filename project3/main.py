import pyttsx3 as p
import speech_recognition as sr
import tkinter as tk
from selenium_web import InfoScraper
from YT_auto import YouTubePlayer
from index import VoiceAssistant
import threading

# Initialize Text-to-Speech Engine
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen_and_recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            return text
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak("Could not request results; check your network connection.")
            return None


# Function to handle the initial greeting and listening
def initial_greeting():
    speak("Hello. I'm your voice assistant. How are you?")
    response = listen_and_recognize()
    if response and "what" in response and "about" in response and "you" in response:
        speak("I'm having a good day.")
    speak("What can I do for you?")
    return listen_and_recognize()


# Function to handle information requests
def handle_information_request():
    speak("You need information related to which topic?")
    topic = listen_and_recognize()
    if topic:
        assistant = InfoScraper()
        assistant.get_info(topic)


# Function to handle video playing requests
def handle_video_request():
    speak("You want me to play which video?")
    video = listen_and_recognize()
    if video:
        assistant = YouTubePlayer()
        assistant.play(video)


def process_command(command):
    if "information" in command:
        handle_information_request()
    elif "play" in command and "video" in command:
        handle_video_request()


def start_voice_assistant():
    main_command = initial_greeting()
    if main_command:
        process_command(main_command)


# Main function to integrate GUI and voice assistant
def main():
    root = tk.Tk()
    assistant = VoiceAssistant(root)

    # Start voice assistant in a separate thread
    threading.Thread(target=start_voice_assistant).start()

    root.mainloop()


if __name__ == "__main__":
    main()

