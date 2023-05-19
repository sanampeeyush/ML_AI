import pyttsx3
import speech_recognition as sr
import nltk

spEng = pyttsx3.init()
spEng.setProperty('rate',120)

spEng.say('Hi')
spEng.runAndWait()
