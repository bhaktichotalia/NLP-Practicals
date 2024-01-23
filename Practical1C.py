# -*- coding: utf-8 -*-
""" Created by Bhakti Chotalia """

import speech_recognition as sr

filename="Audio.wav"

# initialize the recognizer
r = sr.Recognizer()

# open the file
with sr.AudioFile(filename) as source:
    audio = r.record(source)# listen for the data (load audio to memory)

try:
    s = r.recognize_google(audio)
    print("Text: "+s)# recognize (convert from speech to text)
except Exception as e:
    print("Exception: "+str(e))
