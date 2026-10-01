current_count_bad_grade = int(input())
name_exercise = ""
grade = 0
bad_grades = 0
sum_grade = 0
count_grade = 0
is_Enought = False
last_problem = " "

while (name_exercise != "Enough"):
    name_exercise = input()
    if name_exercise == "Enough":
        is_Enought = False
        break
    grade = int(input())
    last_problem = name_exercise
    if name_exercise != "Enough":
        sum_grade += grade
        count_grade += 1
        is_Enought = True

    if grade <= 4:
        bad_grades += 1
        if bad_grades == current_count_bad_grade:
            print(f"You need a break, {bad_grades} poor grades.")
            break

average_grade = 0
if count_grade > 0:
    average_grade = sum_grade / count_grade

if is_Enought == False:
    print(f"Average score: {(average_grade):.2f}")
    print(f"Number of problems: {count_grade}")
    print(f"Last problem: {last_problem}")

