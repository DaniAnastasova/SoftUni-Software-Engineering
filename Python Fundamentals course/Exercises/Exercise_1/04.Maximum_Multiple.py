divisor = int(input())
boundary = int(input())

largest_num = 0

for i in range(boundary, divisor+1, -1):
    if i % divisor == 0:
        largest_num = i
        print(largest_num)
        break

