command = input()
new_string = ""

while command != "End":
    if command != "SoftUni":
        for i in command:
            new_string += i*2
        print(new_string)
        new_string = ""
    command = input()
