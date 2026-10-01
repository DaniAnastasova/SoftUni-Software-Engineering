n = int(input())

min_num = 0
max_num = 0

for i in range(n):
    number = int(input())
    if i == 0:
        min_num = number
        max_num = number
    else:
        if number > max_num:
            max_num = number
        elif number < min_num:
            min_num = number

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")