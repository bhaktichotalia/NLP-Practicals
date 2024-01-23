# -*- coding: utf-8 -*-
""" Created by Bhakti Chotalia """

import nltk
groucho_grammar = nltk.CFG.fromstring("""
 S -> NP VP
 PP -> P NP
 NP -> Det N | Det N PP | 'I'
 VP -> V NP | VP PP
 Det -> 'a' | 'my'
 N -> 'cake' | 'birthday'
 V -> 'baked'
 P -> 'on'
 """)
sent = ['I', 'baked', 'a', 'cake', 'on', 'my', 'birthday']
parser = nltk.ChartParser(groucho_grammar)
for tree in parser.parse(sent):
     print(tree)
