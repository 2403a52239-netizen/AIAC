def score_applicant(education_level, years_experience, gender, age):
    """
    Scores a job applicant based on input features.
    education_level: str, one of ['high_school', 'bachelor', 'master', 'phd']
    years_experience: int
    gender: str, e.g. 'male', 'female', 'other'
    age: int

    Returns: float, applicant score
    """
    # Education score
    education_scores = {
        'high_school': 1,
        'bachelor': 2,
        'master': 3,
        'phd': 4
    }
    edu_score = education_scores.get(education_level.lower(), 0)

    # Experience score
    exp_score = min(years_experience, 20) * 0.5  # cap at 20 years

    # Gender score (neutral)
    gender_score = 0  # No bias

    # Age score (prefer 22-60)
    if 22 <= age <= 60:
        age_score = 2
    else:
        age_score = 0

    total_score = edu_score * 2 + exp_score + gender_score + age_score
    return total_score

if __name__ == "__main__":
    education_level = input("Enter education level (high_school, bachelor, master, phd): ")
    years_experience = int(input("Enter years of experience: "))
    gender = input("Enter gender: ")
    age = int(input("Enter age: "))

    score = score_applicant(education_level, years_experience, gender, age)
    print(f"Applicant score: {score}")