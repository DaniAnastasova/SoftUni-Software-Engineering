n = int(input())

numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

command = input()

filtered_lst = []

if command == "even":
    for num in numbers:
        if num % 2 == 0:
            filtered_lst.append(num)

elif command == "odd":
    for num in numbers:
        if num % 2 != 0:
            filtered_lst.append(num)

elif command == "positive":
    for num in numbers:
        if num >= 0:
            filtered_lst.append(num)

elif command == "negative":
    for num in numbers:
        if num < 0:
            filtered_lst.append(num)

print(filtered_lst)