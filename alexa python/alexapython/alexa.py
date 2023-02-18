from multiprocessing.connection import Listener
import speech_recognition as sr
import pyttsx3 
import pywhatkit
import urllib.request
import json
import datetime
import wikipedia

name = 'alexa'
key = 'AIzaSyB5qTLBfjlFZxBw-ijwvHW-ZZuunP26JBE'
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language="es-MX")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')
                print(rec)
    except:
        pass
    return rec

def Run_alexa():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', "")
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)
    
    elif 'hora' in rec:
        hora=datetime.datetime.now().strftime('%H:%M:%S')
    talk ("la hora es" +hora)

    if 'busca' in rec:
     buscador = rec.replace('busca', '')
     wikipedia.set_lang("es")
     wiki = wikipedia.summary(buscador, 2)
     print(buscador + ": " + wiki)
     (wiki)
   
   
Run_alexa()