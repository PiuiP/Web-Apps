n = int(input())
students = []

first_student_name = input()
first_student_score = float(input())
students.append([first_student_name, first_student_score])

lowest = first_student_score
second_lowest = float('inf')

for _ in range(n-1):
    name = input()
    score = float(input())
    students.append([name, score])
    if score < lowest:
        second_lowest = lowest
        lowest = score
    elif lowest < score < second_lowest:
        second_lowest = score


result_names = []
for name, score in students:
    if score == second_lowest:
        result_names.append(name)

for name in sorted(result_names):
    print(name)