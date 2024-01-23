# -*- coding: utf-8 -*-
""" Created by Bhakti Chotalia """

from nltk.corpus import wordnet
synonyms = []
antonyms = []
  
for syn in wordnet.synsets("active"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
  
print("\nSysnet Synonyms : ",set(synonyms))
print("\nSysnet Antonyms : ",set(antonyms))
