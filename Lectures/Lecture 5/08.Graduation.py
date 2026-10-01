name = input()
count_grade = 1
sum_grade = 0
izkluchvane = 0

while count_grade <= 12:
    grade = float(input())

    if grade < 4.00:
        izkluchvane += 1
        if izkluchvane > 1:
            print(f"{name} has been excluded at {count_grade} grade")
            break
    else:
        sum_grade += grade
        count_grade += 1

if count_grade > 12:
    average_grade = sum_grade / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")