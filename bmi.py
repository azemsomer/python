#!/usr/bin/python
#
#Program to calculate one's BMI

#function to calculate BMI
def calcBMI ( weight, length): 
    bmi = weight / (length*length)
    return bmi

#ask user for his/her name

name = input("What is your name? ")

print("Hello " + name)

#querries weight and convert input to float

weight = input("Please enter your weight: ")

weight = float(weight)

if weight < 0:
	raise ValueError("Not a valid value")

#querries length and convert input to float

length = input("Plese enter your length: ")

length = float(length)

if length < 0:
	raise ValueError("Not a valid value")

#calcute BMI and print result

bmi = calcBMI(weight, length)

print("Your BMI is: " + str(bmi))

#checks whether bmi is too high, low are just fine
if ( bmi > 27.0) : print("Your weight is too high!")
elif (bmi < 18.5) : print("Your weight is too low!")
else : print("Your weight is fine!")

print("Goodbye " + name + "!")
