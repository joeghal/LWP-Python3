class Student:
    total_students = 0
    def __init__(self, first, last, email, phone):
        self.first = first
        self.last = last
        self.email = email
        self.phone = phone
        Student.total_students += 1


    def printFullName(self):
        print(self.first + " " + self.last)

    def changePhone(self, newPhone):
        self.phone = newPhone



student1 = Student("John", "Doe", "john.doe@school.edu", 122354385)

# student1.first = 'John'
# student1.last = 'Doe'
# student1.email = 'john.doe@school.edu'
# student1.phone = 122354385


print(student1)
student2 = Student("Steve", "Fisherman", "steve.fisherman@school.edu", 489578948)

# student2 = Student()
# student2.first = 'Steve'
# student2.last = 'Fisherman'
# student2.email = 'steve.fisherman@school.edu'
# student2.phone =489578948

# print(student1.first + " " + student1.last)
# print(student2.first + " " + student2.last)

student1.printFullName()
student2.printFullName()

print(student2)

student1.changePhone(8080808080)
print(student1.phone)

print(Student.total_students)