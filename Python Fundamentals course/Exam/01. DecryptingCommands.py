string = input()
command = input().split()

while command[0] != 'Finish':
    if command[0] == 'Replace':
        current_char = command[1]
        new_char = command[2]
        string = string.replace(current_char,new_char)
        print(string)

    elif command[0] == 'Cut':
        start_index = int(command[1])
        end_index = int(command[2])

        if start_index < 0 or end_index >= len(string) or end_index < 0 or start_index >= len(string) or start_index > end_index:
            print("Invalid indices!")
        else:
            string = string[:start_index] + string[end_index+1:]
            print(string)

    elif command[0] == 'Make':
        if command[1] == "Upper":
            string =  string.upper()
            print(string)
        elif command[1] == "Lower":
            string = string.lower()
            print(string)

    elif command[0] == 'Check':
        str_for_check = command[1]
        if str_for_check in string:
            print(f"Message contains {str_for_check}")
        else:
            print(f"Message doesn't contain {str_for_check}")

    elif command[0] == "Sum":
        start_index = int(command[1])
        end_index = int(command[2])

        if start_index >= 0 and  end_index < len(string) and start_index < len(string):
            sum = 0
            for i in string[start_index:end_index+1]:
                sum += ord(i)

            print(sum)
        else:
            print("Invalid indices!")

    command = input().split()
    if command[0] == 'Finish':
        break