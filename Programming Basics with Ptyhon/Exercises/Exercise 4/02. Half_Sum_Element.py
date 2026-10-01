n = int(input())
max_num = 0
sum = 0

for i in range(n):
    num = int(input())
    if max_num < num:
        max_num = num

    sum += num
    if i == n-1:
        sum = sum - max_num

        if sum == max_num:
            print(f"Yes")
            print(f"Sum = {sum}")
        else:
            if max_num > sum:
                print(f"No")
                print(f"Diff = {(max_num - sum)}")
            else:
                print(f"No")
                print(f"Diff = {(sum - max_num)}")




