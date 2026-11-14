def even_num(num):
    if num % 2 == 0:
        return True
    else:
        return False

numbers = input().split()
number_as_didgit = []

for num in numbers:
    number_as_didgit.append(int(num))

result = list(filter(even_num, number_as_didgit))

print(result)
