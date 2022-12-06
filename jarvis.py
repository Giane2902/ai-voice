import speech_recognition as sr
import pyttsx3
import pywhatkit
import urllib.request
import json
import datetime

name = 'alexa'
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    rec = ''
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()  # type: ignore
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
    except:
        pass
    return rec

def run():
    rec = listen()
    if 'play' in rec:
        music = rec.replace('play','')  # type: ignore
        talk('Playing ' + music)
        pywhatkit.playonyt(music)  # type: ignore
    if 'cuantos suscriptores tiene' in rec:
        name_subs = rec.replace('cuantos suscriptores tiene', '')  # type: ignore
        data = urllib.request.urlopen('')
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        talk(name_subs + "tiene {:,d}".format(int(subs)) + " suscriptores!")
    if 'hour' in rec:
        hour = datetime.datetime.now().strftime('%I:%M %p')  # type: ignore
        talk("Son las "+hour)


run()