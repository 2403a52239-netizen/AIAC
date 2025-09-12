class sru_student:  # Define a class to represent an SRU student
    def __init__(self, name, roll_no, hostel_status):  # Constructor to initialize attributes
        self.name = name  # Store student name
        self.roll_no = roll_no  # Store roll number
        self.hostel_status = hostel_status  # Store hostel residency as True/False
        self.fee_paid = False  # Initialize fee status as unpaid
    
    def fee_update(self, fee_status):  # Method to update fee payment status
        self.fee_paid = fee_status  # Set internal fee status
        if fee_status:  # If fee is paid
            print(f"Fee payment confirmed for {self.name}")  # Confirm payment message
        else:  # If fee is not paid
            print(f"Fee payment pending for {self.name}")  # Pending payment message
    
    def display_details(self):  # Method to print student details
        print("=" * 40)  # Separator line
        print("SRU STUDENT DETAILS")  # Section header
        print("=" * 40)  # Separator line
        print(f"Name: {self.name}")  # Show student name
        print(f"Roll Number: {self.roll_no}")  # Show roll number
        print(f"Hostel Status: {'Yes' if self.hostel_status else 'No'}")  # Yes/No hostel status
        print(f"Fee Status: {'Paid' if self.fee_paid else 'Pending'}")  # Paid/Pending fee status
        print("=" * 40)  # Closing separator

name = input("Enter student name: ")  # Get name from user
roll_no = input("Enter roll number: ")  # Get roll number from user
hostel_input = input("Does student live in hostel? (yes/no): ")  # Ask hostel residency
hostel_status = hostel_input.lower() == 'yes'  # Convert response to boolean

student = sru_student(name, roll_no, hostel_status)  # Create a student object

fee_input = input("Is fee paid? (yes/no): ")  # Ask fee payment status
fee_status = fee_input.lower() == 'yes'  # Convert response to boolean
student.fee_update(fee_status)  # Update student's fee status and print message

student.display_details()  # Display all collected details