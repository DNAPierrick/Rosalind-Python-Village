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

#04 - Recursive function
#Fibonnaci number on immortal rabbits, 4 offsprings per generation
def numberabbit (numberofmonths, numberoffspring):
    if numberofmonths == 1 :
        return 1

    elif numberofmonths == 2:
        return numberoffspring

    elif numberofmonths <= 4:
        oneGen = numberabbit(numberofmonths - 1, numberoffspring)
        twoGen = numberabbit(numberofmonths - 2, numberoffspring)
        return (oneGen + twoGen)

    else:
        oneGen = numberabbit(numberofmonths - 1, numberoffspring)
        twoGen = numberabbit(numberofmonths - 2, numberoffspring)
        nblap = (oneGen + (twoGen * numberoffspring))
        return nblap

print(numberabbit(29,5))


#05 - GC content

'''Calculate the GC content of a fasta file and gives the highest content'''
import re
import operator
filename = 'rosalind_gc.txt'
content = {}

with open(filename) as test:
    total = 0
    totalgc = 0
    for line in test:
        line = line.strip("\n")

        #if re.match(r"*Rosalind*", line) == True:
        if "Rosalind" in line:
            print("Header found")
            id = line
            content[id] = 0
            totalgc = 0
            total = 0
        else:
            print(line)
            total += len(line)
            number = len(re.findall(r"G|C", line))
            totalgc += number

            content[id] = round(totalgc/(total-13) *100, 6)

print(content)

inverse = [(value, key) for key, value in content.items()]
print (max(inverse)[1])
