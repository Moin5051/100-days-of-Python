student_score = {
    "Harry": 88,
    "Ron":78,
    "Hermoine":95,
    "Draco":75,
    "Neville":60
}

student_grades = {}

for score in student_score:
    if student_score[score] <=100 and student_score[score]>91:
        student_grades[score] = "Outstanding"
    elif student_score[score] <=90 and student_score[score]>81:
        student_grades[score] = "Exceeding Expectations"
    elif student_score[score] <=80 and student_score[score]>71:
        student_grades[score] = "Acceptable"
    else: 
        student_grades[score] = "Failed!!!"
    
print(student_grades)