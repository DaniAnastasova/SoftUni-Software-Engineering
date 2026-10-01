num = int(input())

digit_1 = num // 100
digit_2 = (num // 10) % 10
digit_3 = num % 10

for i in range(1, digit_3 + 1):
    for j in range(1, digit_2 + 1):
        for k in range(1, digit_1 + 1):
            print(f"{i} * {j} * {k} = {(i*j*k)};")