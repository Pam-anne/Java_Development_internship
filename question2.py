
exam1 = int(input("Enter marks for Exam 1: "))
exam2 = int(input("Enter marks for Exam 2: "))
exam3 = int(input("Enter marks for Exam 3: "))

average_marks = (exam1 + exam2 + exam3) / 3

if average_marks >= 90:
    grade = "A"
elif average_marks >= 80:
    grade = "B"
elif average_marks >= 70:
    grade = "C"
elif average_marks >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Average Marks: {average_marks:.2f}")
print(f"Your Grade is : {grade}")
