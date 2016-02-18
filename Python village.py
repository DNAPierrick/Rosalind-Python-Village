#!/usr/bin/python
import os
os.getcwd()


'''
Rosalind 5
texte = open("rosalind_ini5.txt", 'r')

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
with open('rosalind_ini5.txt','r') as f:
   print ''.join(f.readlines()[1::2])
'''

texte = open("rosalind_ini5.txt", 'r')

mots = {}

for word in str.split('When youre feeling in the dumps, dont be silly, '):
   print word
   word = mots[]

   # if word in mots not '':
   # mots[key] += 1
print mots
for key, value in mots.items():
    print key
    print value