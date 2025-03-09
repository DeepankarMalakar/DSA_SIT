# Write a program to create student class with the following members:
# Data members:
# name, roll, marks
# Member functions:
# __init__(), initialize the object with name, roll
# showdata() display all the details of the student
# showmarks() display marks of the student

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def showdata(self):
        print(f"Name: {self.name}, Roll No: {self.roll}, Marks: {self.marks}")

    def showmarks(self):
        print(f"Marks: {self.marks}")


student1 = Student("Deepankar", 101, 85)
student1.showdata()  # Display all details
student1.showmarks()  # Display only marks
