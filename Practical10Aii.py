# -*- coding: utf-8 -*-
""" Created by Bhakti Chotalia """

import nltk
tokens=nltk.word_tokenize("Can we get information on admission for the academic year 2021")
print("Parts of speech:",nltk.pos_tag(tokens))
