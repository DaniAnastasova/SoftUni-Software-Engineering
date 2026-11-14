heroes = {}

while True:
    command = input().split()
    if command[0] == "End":
        print("Heroes:")
        for hero, spell in heroes.items():
            spells = ", ".join(spell)
            print(f"== {hero}: {spells}")

        break

    command_type = command[0]
    hero_name = command[1]

    if command_type == "Enroll":
        if hero_name in heroes:
            print(f"{hero_name} is already enrolled.")
        else:
            heroes[hero_name] = []

    elif command_type == "Learn":
        spell_name = command[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        else:
            if spell_name in heroes[hero_name]:
                print(f"{hero_name} has already learnt {spell_name}.")
            else:
                heroes[hero_name].append(spell_name)

    elif command_type == "Unlearn":
        spell_name = command[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in heroes[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes[hero_name].remove(spell_name)
