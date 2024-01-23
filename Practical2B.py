# -*- coding: utf-8 -*-
""" Created by Bhakti Chotalia """

from nltk.corpus import PlaintextCorpusReader
corpus_root = 'NewCorpus-2B/'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
print(wordlists.fileids())
files=['file1.txt', 'file2.txt']
filename=0
for text in files:
    filename+=1
    with open(corpus_root+str(filename)+'.txt','r') as fout:
        print("\n",fout.read(), text)
