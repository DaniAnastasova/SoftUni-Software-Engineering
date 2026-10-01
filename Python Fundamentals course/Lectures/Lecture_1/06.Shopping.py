budget = int(input())
command = ""
sum = 0

while command != "End":
    command = input()
    if command != "End":
        number = int(command)
        sum += number

    if sum > budget:
        break


if sum > budget:
    print(f"You went in overdraft!")
else:
    print("You bought everything needed.")



