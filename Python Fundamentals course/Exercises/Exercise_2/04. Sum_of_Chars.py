numbers_of_characters = int(input())
total_sum = 0

for i in range(numbers_of_characters):
    letter = input()
    total_sum += ord(letter)

print(f"The sum equals: {total_sum}")

