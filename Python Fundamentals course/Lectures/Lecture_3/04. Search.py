n = int(input())
special_word = input()

strings = []

for i in range(n):
    current_string = input()
    strings.append(current_string)

filtered_lst = []

for string in strings:
    if special_word in string:
        filtered_lst.append(string)

print(strings)
print(filtered_lst)