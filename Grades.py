student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
for i in student_scores:
    if student_scores[i] > 90:
        student_grades[i] = "Outstanding"
    elif student_scores[i] > 80:
        student_grades[i] = "Exceed Expection"
    elif student_scores[i] > 70:
        student_grades[i] = "Exceptable"
    else:
        student_grades[i] = "FAil"
# 🚨 Don't change the code below 👇
for i in student_grades:
    print(i, "-", student_grades[i])
