# Loan approval program for Priya

def check_loan_approval(applicant_name, income, credit_score, loan_amount):
    # Simple criteria for approval
    min_income = 30000
    min_credit_score = 650
    max_loan_amount = income * 5

    if applicant_name.lower() != "priya":
        return f"Loan application is only for Priya."

    if income < min_income:
        return "Loan not approved: Income too low."
    if credit_score < min_credit_score:
        return "Loan not approved: Credit score too low."
    if loan_amount > max_loan_amount:
        return "Loan not approved: Requested amount too high."

    return "Loan approved!"

# Example usage for Priya
priya_income = 50000
priya_credit_score = 700
priya_loan_amount = 200000

result = check_loan_approval("Priya", priya_income, priya_credit_score, priya_loan_amount)
print(result)