n = int(input())

numbers = []

for i in range(n):
    number = int(input())
    numbers.append(number)

negative_numbers = []
positive_numbers = []

for num in numbers:
    if num >= 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum(negative_numbers)}")
