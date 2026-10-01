username = input()
password = input()

password_2 = input()
if password == password_2:
    print(f"Welcome {username}!")
else:
    while (password != password_2):
        password_2 = input()
        if password == password_2:
            print(f"Welcome {username}!")