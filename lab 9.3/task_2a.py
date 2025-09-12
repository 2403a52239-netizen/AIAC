class sru_student:
    def __init__(self, name, roll_no, hostel_status):
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee_paid = False
    
    def fee_update(self, fee_status):
        self.fee_paid = fee_status
        if fee_status:
            print(f"Fee payment confirmed for {self.name}")
        else:
            print(f"Fee payment pending for {self.name}")
    
    def display_details(self):
        print("=" * 40)
        print("SRU STUDENT DETAILS")
        print("=" * 40)
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Hostel Status: {'Yes' if self.hostel_status else 'No'}")
        print(f"Fee Status: {'Paid' if self.fee_paid else 'Pending'}")
        print("=" * 40)

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
hostel_input = input("Does student live in hostel? (yes/no): ")
hostel_status = hostel_input.lower() == 'yes'

student = sru_student(name, roll_no, hostel_status)

fee_input = input("Is fee paid? (yes/no): ")
fee_status = fee_input.lower() == 'yes'
student.fee_update(fee_status)

student.display_details()