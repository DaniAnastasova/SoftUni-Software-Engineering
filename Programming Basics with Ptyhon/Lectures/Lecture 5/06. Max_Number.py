num = " "
num_2 = 0
max_num = 0

num = input()
if num != "Stop":
    max_num = int(num)

while num != "Stop":
    num = input()
    if num != "Stop":
        num_2 = int(num)
        if num_2 > max_num:
            max_num = num_2
    else:
        break

print(max_num)

