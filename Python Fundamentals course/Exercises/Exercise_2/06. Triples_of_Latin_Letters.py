number = int(input())

for first_char in range(97, 97 + number):
    for second_char in range(97, 97 + number):
        for third_char in range(97, 97 + number):
            print(f"{chr(first_char)}{chr(second_char)}{chr(third_char)}")

