#!/usr/bin/python3
#
#This is a test program to test file read
#with objects

class member:
    """class of library members"""
    memCount = 0
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        member.memCount += 1
        
    def printMemInfo(self):
        print( "Name: ", self.name, ", Address: ", self.address)

#open some file
f = open("azemsomer/python/testFile.txt")

#put lines into list
rules = f.readlines()

#empty datastructure
membersList = []

#fill member list
for line in range(len(rules)):
    item = rules[line].split(",")
    name = item[0].strip()
    address = item[1].strip()
    membersList.append(member(name, address))
    
#print member list
for lid in range(len(membersList)):
    membersList[lid].printMemInfo()

f.close
