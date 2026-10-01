n = int(input())
presentaion_name = ""
grade = 0
average_grade_for_one_presentation = 0
sum_of_grades = 0
sum_of_all_grade = 0
average_grade = 0
count = 0

while True:
    presentaion_name = input()
    if presentaion_name == "Finish":
        average_grade = sum_of_all_grade / count
        print(f"Student's final assessment is {(average_grade):.2f}.")
        break
    for i in range(0, n):
        grade = float(input())
        sum_of_grades += grade

    average_grade_for_one_presentation = sum_of_grades / n
    sum_of_all_grade += average_grade_for_one_presentation
    count += 1
    print(f"{presentaion_name} - {(average_grade_for_one_presentation):.2f}.")
    sum_of_grades = 0




