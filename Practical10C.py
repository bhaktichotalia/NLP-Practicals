# -*- coding: utf-8 -*-
""" Created by Bhakti Chotalia """

from nltk.parse import malt

mp = malt.MaltParser('C:\\Users\\HI\\AppData\\Local\\Programs\\Python\\Python310\\maltparser-1.9.2', 'C:\\Users\\HI\\AppData\\Local\\Programs\\Python\\Python310\\engmalt.linear-1.7.mco')#file	
t = mp.parse_one('I shot an elephant in my pajamas .'.split()).tree()
print(t)
print(t.draw())

