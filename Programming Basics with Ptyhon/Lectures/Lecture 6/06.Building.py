count_floors = int(input())
count_rooms = int(input())


for i in range(count_floors,0, -1):
    for j in range(count_rooms):
        if i == count_floors:
            print(f"L{i}{j}", end=" ")

        elif i % 2 == 0:
            print(f"O{i}{j}", end=" ")

        else:
            print(f"A{i}{j}", end=" ")

    print()