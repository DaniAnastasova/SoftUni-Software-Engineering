count_eggs_on_one_gamer = int(input())
count_eggs_on_two_gamer = int(input())
command = ""

while command != "End":
    if count_eggs_on_one_gamer == 0:
        print(f"Player one is out of eggs. Player two has {count_eggs_on_two_gamer} eggs left.")
        break
    elif count_eggs_on_two_gamer == 0:
        print(f"Player two is out of eggs. Player one has {count_eggs_on_one_gamer} eggs left.")
        break

    command = input()

    if command == "End":
        break

    if command == "one":
        count_eggs_on_two_gamer -= 1
    elif command == "two":
        count_eggs_on_one_gamer -= 1

if count_eggs_on_one_gamer != 0 and count_eggs_on_two_gamer != 0:
    print(f"Player one has {count_eggs_on_one_gamer} eggs left.")
    print(f"Player two has {count_eggs_on_two_gamer} eggs left.")