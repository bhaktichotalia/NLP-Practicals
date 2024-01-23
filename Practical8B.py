# -*- coding: utf-8 -*-
""" Created by Bhakti Chotalia """

import nltk
from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import word_tokenize
# Init the Wordnet Lemmatizer
lemmatizer = WordNetLemmatizer()

# Lemmatize Single Word


sentence = "He makes a very delicious meal. It costs nothing to be good"
words = word_tokenize(sentence)
 
for w in words:
    print(w, " ==>: ", lemmatizer.lemmatize(w))

