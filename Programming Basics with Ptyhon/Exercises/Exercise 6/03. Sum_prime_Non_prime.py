import math

num = ""
sum_prime = 0
sum_non_prime = 0

while True:
    num = input()
    if num == "stop":
        print(f"Sum of all prime numbers is: {sum_prime}")
        print(f"Sum of all non prime numbers is: {sum_non_prime}")
        break
    num = int(num)
    if num < 0:
        print("Number is negative.")
        continue

    if num == 0 or num == 1:
        sum_non_prime += num

    is_prime = True

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime and num > 1:
        sum_prime += num
    elif not is_prime and num > 1:
        sum_non_prime += num
