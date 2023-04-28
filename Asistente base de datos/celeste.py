import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import sys
import time
import subprocess
import pyjokes
import webbrowser
from conexion import *
from Reproductor_de_musica import *


name = 'celeste'

listener = sr.Recognizer()

engine = pyttsx3.init()



voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("escuchando..")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name,"")
                print(rec)
                rec = listener.recognize_google(voice, language='es')
            """else:
                talk("Lo siento, no entendi lo que me dijiste")
                """
    except:
        pass
    return rec



def run():
    rec = listen()
    if 'hora' in rec:
        hora = datetime.datetime.now().strftime('%H:%M')
        talk("son las " + hora)

    elif 'escribe' in rec:
       file = open("newfile.txt","w")
       file.write(rec)
       file.close()
       talk("tu archivo a sido escrito,correctamente")

    elif 'repite' in rec:
        file = open("newfile.txt")
        talk(file.read())
        file.close()

    elif 'ola' in rec:
        talk("hola como estas, que necesitas estoy aqui para ayudarte")

    elif 'busca' in rec:
        order = rec.replace('busca','')
        wikipedia.set_lang("es")
        info = wikipedia.summary(order, 1)
        talk(info)

    elif 'apagate' in rec:
        talk("Apagando en 3... 2... 1 ....")
        sys.exit()
    elif 'open youtube' in rec:
       webbrowser.open_new_tab("https://www.youtube.com")
       talk("youtube esta abierto ahora")
       time.sleep(5)

    elif 'open gmail' in rec:
        webbrowser.open_new_tab("gmail.com")
        talk("Google Mail esta abierto ahora")
        time.sleep(5)

    elif 'open google' in rec:
        webbrowser.open_new_tab("https://www.google.com")
        talk("Google chrome esta abierto ahora")
        time.sleep(5)

    elif 'sierra session'  in rec or 'sign out' in rec:
        talk("Ok , tu pc cerrara session en 10 segundos se cerraran todas las aplicaciones ")
        subprocess.call(["shutdown", "/l"])
        time.sleep(3)

    elif 'joke' in rec:
        joke = pyjokes.get_jokes(language='es')
        talk(joke)

    """elif 'musica' in rec:
        autor = "Eladio"
        song  = "Triste verano"
        print(poner_musica("Eladio",song.upper))
"""

while True:
    run()



