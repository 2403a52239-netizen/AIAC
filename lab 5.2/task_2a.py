# Loan approval program for John

def check_loan_approval(name, income, credit_score, loan_amount):
    # Simple approval criteria
    min_income = 30000
    min_credit_score = 650
    max_loan_amount = income * 5

    if name.lower() != "john":
        return f"Loan application is only for John."

    if income < min_income:
        return "Loan Denied: Income too low."
    if credit_score < min_credit_score:
        return "Loan Denied: Credit score too low."
    if loan_amount > max_loan_amount:
        return "Loan Denied: Requested amount exceeds limit."

    return "Loan Approved!"

# Example usage for John
john_income = 45000
john_credit_score = 700
john_loan_amount = 100000

result = check_loan_approval("John", john_income, john_credit_score, john_loan_amount)
print(result)