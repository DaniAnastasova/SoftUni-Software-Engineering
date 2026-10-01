n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

count_in_p1 = 0
count_in_p2 = 0
count_in_p3 = 0
count_in_p4 = 0
count_in_p5 = 0

for i in range(n):
    num = int(input())
    if num < 200:
        count_in_p1 += 1
    elif num >= 200 and num <= 399:
        count_in_p2 += 1
    elif num >= 400 and num <= 599:
        count_in_p3 += 1
    elif num >= 600 and num <= 799:
        count_in_p4 += 1
    elif num >= 800:
        count_in_p5 += 1

p1 = count_in_p1 / n* 100
p2 = count_in_p2 / n* 100
p3 = count_in_p3 / n* 100
p4 = count_in_p4 / n* 100
p5 = count_in_p5 / n* 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")

