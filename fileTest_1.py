#!/usr/bin/python3
#
#This is a test program to test file read

#open some file
f = open("azemsomer/python/testFile.txt")

#put file data into string
fBuffer = f.read()

#splitting file into lines
rules = fBuffer.splitlines()

#empty list of members, alt: ledenlijst = list()
ledenlijst = []

#put line elements into datastructure
for elm in range(len(rules)):
    row = rules[elm].split(', ')
    for bit in range(len(row)):
        name = rules[bit][0]
        address = rules[bit][1]
        ledenlijst.append({'name': name, 'address' : address})

#print member list
for lid in range(len(ledenlijst)):
    print('Naam: ',ledenlijst[lid]['name'])
    print('Adres: ',ledenlijst[lid]['address'])

f.close
