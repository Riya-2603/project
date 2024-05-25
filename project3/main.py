import pyttsx3 as p
import speech_recognition as sr
from selenium_web import InfoScraper
from YT_auto import YouTubePlayer

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak("Hello mam. i'm your voice assistant. How are u?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source , 1.2)
    print("Listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "u" in text:
    speak("i m having a good day mam.")
speak("What can i do for u?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source , 1.2)
    print("Listening")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("You need information related to which topic ")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening")
        audio = r.listen(source)
        infor = r.recognize_google(audio)

    if __name__ == "__main__":
        assistant = InfoScraper()
        assistant.get_info(infor)

elif "play" and "video" in text2:
    speak("you want me to play which video??")


    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening")
        audio = r.listen(source)
        vid = r.recognize_google(audio)

    if __name__ == "__main__":
        assistant = YouTubePlayer()
        assistant.play(vid)

