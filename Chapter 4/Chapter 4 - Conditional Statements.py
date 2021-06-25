x = 10
y = 20

print(x == y)

z = (x != y)
print(type(z))
m = (x < y)
print(m)
print(x >= y)
print(x <= y)

if x == y:
    print('x IS equal to y')
else:
    print("X is NOT equal to y")

grade = 80
letterGrade = 'A'
if grade < 60:
    letterGrade = 'F'
elif grade >= 60 and grade < 70:
    letterGrade = 'D'
elif grade >= 70 and grade < 80:
    letterGrade = 'C'
elif grade >=80 and grade < 90:
    letterGrade = 'B'
else:
    letterGrade = 'A'

print(letterGrade)






