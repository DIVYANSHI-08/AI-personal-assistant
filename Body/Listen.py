#Hindi to English
#library 
#pip install googletrans==3.1.0a0
#pip install speechrecognition


import speech_recognition as sr
from googletrans import Translator
import time
def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.energy_threshold = 4000
        r.pause_threshold = 0.8
        try:
            audio = r.listen(source,timeout=0,phrase_time_limit=8)
        except sr.WaitTimeoutError:
            print("Timeout occurred. Please try speaking again.")
            return ""
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="hi")
    except:
        return ""
    query = str(query).lower()
    return query

def TranslationHinditoEnglish(Text,s="default"):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"{s}: {data}.")
    return data

def MicExecution(s):
    query = Listen()
    data = TranslationHinditoEnglish(query,s)
    return data

MicExecution(s="You")