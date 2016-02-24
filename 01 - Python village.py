#!/usr/bin/python
#-*- coding: UTF-8

import os
os.getcwd()

#05 - Working with Files

texte = open("rosalind_ini5.txt", 'r')


def lignespaires(texte):
    res = open("resultat.txt", 'w')
    i = 0
    for lines in texte:
        if i % 2 == 1:
            res.write(lines)
            i += 1
        else :
            i+=1

    res.close()

#The elegant way
'''
def lignespaires2()
    with open('rosalind_ini5.txt','r') as f:
       print ''.join(f.readlines()[1::2])
'''

#06 - Dictionaries

listemots = open('rosalind_ini6.txt', 'r')
dico = {}

def motcounter(listemots)
    for word in listemots.read().replace('\n', ' ').split(' '):
        if word not in dico.keys():
            dico[word] = 1
        else:
            dico[word] += 1
    print dico
    for keys, values in dico.items():
        print keys, values

#The elegant way
'''
from collections import Counter
for k,v in Counter(raw_input().split()).items(): print k,v

'''
'''
with open('rosalind_ini6.txt', 'r') as f:
from collections import Counter
for k, v in Counter(str(f.readlines()).split()).items(): print(k, v)
'''
'''
string = 'example text'
word_counts = {}
for s in string.split():
    word_counts[s] = word_counts.get(s,0) + 1

for w in word_counts:
    print w, word_counts[w]
'''

