#refactor the code by using name, age and marks and add docstrings
class Student:
    """
    Represents a student with name, age, and a list of marks.
    Provides methods to display details and calculate total marks.
    """

    def __init__(self, name, age, marks):
        """
        Initializes a Student object.

        Parameters:
        name (str): The student's name.
        age (int): The student's age.
        marks (list of int): A list of marks for the student.
        """
        self.name = name
        self.age = age
        self.marks = marks

    def show_details(self):
        """Prints the student's name and age in a readable format."""
        print(f"Student Name: {self.name}\nAge: {self.age}")

    def total_marks(self):
        """Returns the total of all marks."""
        return sum(self.marks)
#example usage
student1 = Student("Alice", 20, [85, 90, 78])
student1.show_details()  # Output: Student Name: Alice, Age: 20
print("Total Marks:", student1.total_marks())  # Output: Total Marks: 253