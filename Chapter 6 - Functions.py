from math import *

def calculateArea(radius):
    area = pi * pow(radius,2)

    return area

r = 2
x = calculateArea(r)
print(x)
u = 5
j = calculateArea(u)
print(j)

print(len("Hello World"))

def customLen(s):
    count = 0
    for ch in s:
        count += 1
    return count

simpleString = "Hello World"
y = customLen(simpleString)
print(y)