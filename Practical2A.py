# -*- coding: utf-8 -*-
""" Created by Bhakti Chotalia """

from nltk.corpus import brown
print(brown.categories())
print(brown.words(categories='news'))
print(brown.words(fileids=['cg22']))
print(brown.sents(categories=['news', 'editorial', 'reviews']))

from nltk.corpus import inaugural
print(inaugural.fileids())
print(inaugural.words())

from nltk.corpus import reuters
print(reuters.fileids())
print(reuters.words())

from nltk.corpus import udhr
print(udhr.fileids())
print(udhr.words())
