num_1 = int(input())
num_2 = int(input())

first_digit = num_1 // 1000
second_digit = (num_1 // 100) % 10
third_digit = (num_1 // 10) % 10
fourth_digit = num_1  % 10

first_digit_2 = num_2 // 1000
second_digit_2 = (num_2 // 100) % 10
third_digit_2 = (num_2 // 10) % 10
fourth_digit_2 = num_2  % 10

for i in range(first_digit, first_digit_2+1):
    if i % 2 !=  0:
        for j in range(second_digit, second_digit_2 + 1):
            if j % 2 != 0:
                for k in range(third_digit, third_digit_2 + 1):
                    if k % 2 != 0:
                        for l in range(fourth_digit, fourth_digit_2 + 1):
                            if l % 2 != 0:
                                print(f"{i}{j}{k}{l}", end=' ')
