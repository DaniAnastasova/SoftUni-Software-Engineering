num = int(input())
sum  = 0
num_2 = 0
while(sum != num):
    num_2 = int(input())
    sum += num_2
    if sum > num:
        break

print(sum)
