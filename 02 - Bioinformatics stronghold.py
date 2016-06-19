#!/usr/bin/python

#01 - Counting DNA Nucleotides

string = open('rosalind_dna.txt', 'r')
sequence = string.readline()
print sequence
print sequence.count("A"), sequence.count("C"), sequence.count("G"), sequence.count("T")

#The elegant way
'''
def qt(s):
    return s.count("A"), s.count("G"), s.count("C"), s.count("T")
'''
'''
file = open('./rosalind1.txt', 'r')
string = file.read()
freq = {'A': 0, 'C': 0, 'G': 0, 'U': 0}
for i in string:
    freq[i] = freq[i] + 1

print freq['A'], freq['C'], freq['G'], freq['U']
'''

#02 -
a = ''
b = ''

for i in range(len(a)):
    if a[i] == 'T':
        b += 'U'
    else:
        b += a[i]

print (b)


#03 - 

a = 'ATCG'
b = len(a) - 1
print(b)
c = ''

while b >= 0  :
    if a[b] == 'T':
        c += 'A'
    elif a[b] == 'A':
        c += 'T'
    elif a[b] == 'C':
        c += 'G'
    elif a[b] == 'G':
        c += 'C'
    b = b-1

print(c)

