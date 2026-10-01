num = " "
num_2 = 0
min_num = 0

num = input()
if num != "Stop":
    min_num = int(num)

while num != "Stop":
    num = input()
    if num != "Stop":
        num_2 = int(num)
        if num_2 < min_num:
            min_num = num_2
    else:
        break

print(min_num)