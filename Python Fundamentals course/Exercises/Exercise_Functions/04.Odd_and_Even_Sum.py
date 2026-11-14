def odd_and_even_sum(number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    for i in number:
        if (int(i)%2==0):
            sum_of_even_digits += int(i)
        else:
            sum_of_odd_digits += int(i)

    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"

num = input()

print(odd_and_even_sum(num))