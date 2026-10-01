Facebook = 150
instagram = 100
reddit = 50

n = int(input())
salary = int(input())

platform = ""
for i in range(n):
    platform = input()
    if platform == "Facebook":
        salary = salary - Facebook
    elif platform == "Instagram":
        salary = salary - instagram
    elif platform == "Reddit":
        salary = salary - reddit
    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)

