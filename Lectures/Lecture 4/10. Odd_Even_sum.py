n = int(input())
sum1 = 0
sum2 = 0
for i in range(n):
    num = int(input())
    if i % 2 == 0:
        sum1 += num
    else:
        sum2 += num

if sum1 == sum2:
    print(f"Yes")
    print(f"Sum = {sum1}")
else:
    if sum1 > sum2:
        print(f"No")
        print(f"Diff = {(sum1 - sum2)}")
    else:
        print(f"No")
        print(f"Diff = {(sum2 - sum1)}")
