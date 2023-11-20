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


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening for trigger word...')
            listener.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print('Recognized:', command)  # Print the recognized command for debugging
            return command
    except:
        pass


def run_alexa():
    command = take_command()
    if ((command is not None) and ('Alexa' in command)):
        talk('How can I assist you?')
        if 'play' in command:
            # Extract the song name from the command
            song = command.replace('play', '')
            talk('Playing ' + song)
            
            # Use pywhatkit to play the song on YouTube
            pywhatkit.playonyt(song)
            
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('The current time is ' + time)
        elif "message" in command:
            pywhatkit.sendwhatmsg("+91xyz", "Test message", 16, 23)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            talk(info)
        elif "search" in command:
            search("Google")
        elif 'date' in command:
            talk('Sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        else:
            talk('Please say the command again.')


while True:
    run_alexa()
