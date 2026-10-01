command = input()
needed_cofee = 0

while command != "END":
    if command.islower():
        if command.lower() == "coding" or command.lower() == "cat" or command.lower() == "dog" or command.lower() == "movie":
            needed_cofee += 1
    elif command.isupper():
        if command.lower() == "coding" or command.lower() == "cat" or command.lower() == "dog" or command.lower() == "movie":
            needed_cofee += 2

    command = input()

if needed_cofee <= 5:
    print(f"{needed_cofee}")
else:
    print("You need extra sleep")