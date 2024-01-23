# -*- coding: utf-8 -*-
""" Created by Bhakti Chotalia """

from nltk.corpus import stopwords
import nltk

 
from nltk.tokenize import word_tokenize

text = "Bhakti Chotalia is a student of UPG College. She is studying MSC IT Part 2."
text_tokens = word_tokenize(text)

tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]

print(tokens_without_sw)
filtered_sentence = (" ").join(tokens_without_sw)
print("NLTK: ",filtered_sentence)

from gensim.parsing.preprocessing import remove_stopwords

filtered_sentence = remove_stopwords(text)

print("Genism:",filtered_sentence)

import spacy
sp = spacy.load('C:\\Users\\HI\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\en_core_web_sm\\en_core_web_sm-3.2.0')

all_stopwords = sp.Defaults.stop_words

text_tokens = word_tokenize(text)
tokens_without_sw= [word for word in text_tokens if not word in all_stopwords]


filtered_sentence = (" ").join(tokens_without_sw)
print("Spacy: ",filtered_sentence)
