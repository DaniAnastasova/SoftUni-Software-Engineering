first_string = input()
second_string = input()
new_string = ""

for i in range(len(first_string)):
    left_part = second_string[:i+1]
    right_part = first_string[i+1:]
    new_string += left_part + right_part
    if first_string[i] != second_string[i]:
        print(new_string)
    new_string = ""
