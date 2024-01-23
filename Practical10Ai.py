# -*- coding: utf-8 -*-
""" Created by Bhakti Chotalia """

import spacy
sp = spacy.load('C:\\Users\\HI\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\en_core_web_sm\\en_core_web_sm-3.2.0')
sen = sp(u"I like to play football. I hated it in my childhood though")
print(sen.text)
print(sen[7].pos_)
print(sen[7].tag_)
print(spacy.explain(sen[7].tag_))
for word in sen:
    print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')
