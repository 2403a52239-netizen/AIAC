class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display_details(self):
        print("Student Details:")
        print(f"Name     : {self.name}")
        print(f"Roll No  : {self.roll_no}")
        print(f"Marks    : {self.marks}")
# Taking user input
name = input("Enter student's name: ")
roll_no = input("Enter roll number: ")
marks = float(input("Enter marks: "))
# Creating an instance of Student
student1 = Student(name, roll_no, marks)# Define a class named Student
student1.display_details()
