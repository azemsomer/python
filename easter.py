#!/usr/bin/python3
#
#Program to calculate Easter date using math
#Meeus/Jones/Butcher algorithm, see:
#https://en.wikipedia.org/wiki/Computus#Anonymous_Gregorian_algorithm

year = int(input("Please enter year: "))

#Calculate date with MJB
a = year % 19
b = year // 100 #floor division required!!
c = year % 100
d = b // 4
e = b % 4
f = (b + 8) // 25
g = (b - f + 1) // 3
h = (19 * a + b - d - g + 15) % 30
i = c // 4
k = c % 4
l = (32 + 2*e + 2*i - h - k) % 7
m = (a + 11*h + 22 * l) // 451
month = (h + l - 7*m + 114) // 31
day = ((h + l - 7*m + 114) % 31) + 1


if ( month == 3):
    print ("Easter falls at ", day," March")
else:
    print ("Easter falls at ", day," April")
