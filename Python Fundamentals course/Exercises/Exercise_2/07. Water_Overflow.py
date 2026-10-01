number_of_lines = int(input())
capacity = 255

for i in range(number_of_lines):
    liters_of_water = int(input())
    if capacity < liters_of_water:
        print("Insufficient capacity!")
        continue
    capacity -= liters_of_water


print(255 - capacity)


