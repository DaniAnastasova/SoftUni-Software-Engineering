num_1 = int(input())
num_2 = int(input())
sum_even = 0
sum_odd = 0

for i in range(num_1, num_2 + 1):
    for index, j in enumerate(str(i)):
        if index % 2 == 0:
            sum_even += int(j)
        else:
            sum_odd += int(j)

    if sum_even == sum_odd:
        print(i, end= ' ')
        sum_even = 0
        sum_odd = 0
    else:
        sum_even = 0
        sum_odd = 0






