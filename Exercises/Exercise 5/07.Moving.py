width = int(input())
length = int(input())
height = int(input())

avaible_space = width * length * height
carton_space = 1
avaiable_space_2 = width * length * height

count_cartoon = ""
full_space = 0

while True:
    count_cartoon = input()
    if count_cartoon != "Done":
        count_cartoon = int(count_cartoon)
        full_space += count_cartoon
        if full_space <= avaiable_space_2:
            avaible_space -= count_cartoon
        else:
            print(f"No more free space! You need {(full_space - avaiable_space_2)} Cubic meters more.")
            break

    elif (count_cartoon == "Done" and full_space <= avaiable_space_2) or full_space >= avaiable_space_2:
        print(f"{(avaiable_space_2 - full_space)} Cubic meters left.")
        break


