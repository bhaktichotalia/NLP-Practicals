# -*- coding: utf-8 -*-
""" Created by Bhakti Chotalia """

from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
import spacy
from keras.preprocessing.text import text_to_word_sequence
from gensim.utils import tokenize

text = """Founded in 2002, SpaceX’s mission is to enable humans to become a spacefaring civilization and a multi-planet 
species by building a self-sustaining city on Mars. In 2008, SpaceX’s Falcon 1 became the first privately developed 
liquid-fuel launch vehicle to orbit the Earth."""

# Splits at space 
split_token=text.split() 
print("Tokenization using split function: ",split_token)

    
# Create a reference variable for Class RegexpTokenizer
tk = RegexpTokenizer('\s+', gaps = True)

# Use tokenize method
regex_token = tk.tokenize(text)
    
print("\n\nRegular expression tokenizer: ",regex_token)

print("\n\nNLTK tokenization: ",word_tokenize(text))


sp = spacy.load('C:\\Users\\HI\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\en_core_web_sm\\en_core_web_sm-3.2.0')
spacy_token=sp(text)
spacyToken=[]
for word in spacy_token:
    spacyToken.append(word.text)

print("\n\nSpacy tokenization: ",spacyToken)

keras_token = text_to_word_sequence(text)
print("\n\nKeras Tokenization:",keras_token)

print("\n\nGenism Tokenization:",list(tokenize(text)))
