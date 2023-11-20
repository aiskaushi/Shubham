import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from googlesearch import search

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text, rate=200, volume=1.0):
    try:
        engine.setProperty('rate', rate)     # Adjust the speech rate (words per minute)
        engine.setProperty('volume', volume) # Adjust the volume (0.0 to 1.0)

        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        raise Exception("Error in talk function:", str(e))

# Example usage:
try:
    talk("Hello, how can I help you?")
except Exception as e:
    print("An error occurred:", str(e))
