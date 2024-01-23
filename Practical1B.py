# -*- coding: utf-8 -*-
""" Created by Bhakti Chotalia """

from gtts import gTTS

# This module is imported so that we can play the converted audio
import os

# The text that you want to convert to audio
mytext = 'Mumbai News Updates: City reports 1,815 new Covid-19 cases, 10 deaths'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,here we have marked slow=False. Which tells the module that the converted audio should have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named Prac1b
myobj.save("Prac1b.wav")

# Playing the converted file
os.system("Prac1b.wav")
