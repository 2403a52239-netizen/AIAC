#refactor the code to use the get() method
student_scores = {"Alice": 85, "Bob": 90}
print(student_scores.get("Charlie", "Not Found"))
print(student_scores["Charlie"] if "Charlie" in student_scores else "Not Found")
