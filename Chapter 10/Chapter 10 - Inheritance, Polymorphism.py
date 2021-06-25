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

class gradStudent(Student):
    total_grad_students = 0
    def __init__(self, first, last, email, phone, degree):
        super().__init__(first,last,email,phone)
        self.degree = degree
        gradStudent.total_grad_students += 1

    def printDegInfo(self):
        print("{} is pursuing {} degree".format(self.first, self.degree))


s1 = Student('John', 'Doe', 'john.doe@email.com', 1243645)
s2 = Student('Jack', 'Stiller', 'jack.stiller@email.com', 3897498)
gs1 = gradStudent('Mike', 'Scott', 'mike.scott@emial.com', 236567, 'PHD')

gs1.printFullName()
print(gs1.total_students)
print(gs1.total_grad_students)
gs1.printDegInfo()

# print(issubclass(gradStudent,Student))
# print(issubclass(Student,gradStudent))

class Employee:
    def __init__(self, fname, lname, address, age):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.age = age

    def printFullName(self):
        print("Employee full name is {} {}".format(self.fname, self.lname))

emp1 = Employee('Steve', 'Johnson', 'Main St', 30)
lst = [emp1, s1, gs1]
for i in lst:
    i.printFullName()

