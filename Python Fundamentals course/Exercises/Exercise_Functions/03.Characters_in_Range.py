def return_chacarters(first_character, second_character):
    list_of_characters = []
    for i in range(ord(first_character)+ 1,ord(second_character)):
        list_of_characters.append(chr(i))

    return list_of_characters


first_char = input()
second_char = input()

print(" ".join(return_chacarters(first_char,second_char)))
