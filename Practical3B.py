# -*- coding: utf-8 -*-
""" Created by Bhakti Chotalia """

from nltk.corpus import wordnet as wn
for syn in wn.synsets("good"):
    print(syn.lemmas())

machine_that_prints = wn.synset('printer.n.03')
print("Hyponyms: ",sorted([lemma.name() for synset in machine_that_prints.hyponyms() for lemma in synset.lemmas()]))
print("Hypernyms: ",[lemma.name() for synset in  machine_that_prints.hypernyms() for lemma in synset.lemmas()])
print("Entailments: ",wn.synset('eat.v.01').entailments())
