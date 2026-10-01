n = int(input())
sum1 = 0
sum2 = 0

for i in range(n):
    number = int(input())
    sum1 += number

print()

for i in range(n):
    number = int(input())
    sum2 += number
if sum1 == sum2:
    print(f"Yes, sum = {sum1}")
else:
    if sum1 > sum2:
        print(f"No, diff = {(sum1 - sum2)}")
    else:
        print(f"No, diff = {(sum2 - sum1)}")