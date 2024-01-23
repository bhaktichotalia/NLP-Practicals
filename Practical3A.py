# -*- coding: utf-8 -*-
""" Created by Bhakti Chotalia """

from nltk.corpus import wordnet
syn = wordnet.synsets('hello')[0]
  
print ("Synset name :  ", syn.name())
  
# Defining the word
print ("\nSynset Definition : ", syn.definition())
  
# list of phrases that use the word in context
print ("\nSynset example : ", syn.examples())

synonyms = []
antonyms = []
  
for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
  
print("\nSysnet Synonyms : ",set(synonyms))
print("\nSysnet Antonyms : ",set(antonyms))
