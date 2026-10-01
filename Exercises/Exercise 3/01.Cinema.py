premier = 12
normal = 7.50
disscount = 5

type = input()
row = int(input())
col = int(input())
price = 0
places = row * col

if type == "Premiere":
    price = premier * places
    print(f"{price:.2f} leva")

elif type == "Normal":
    price = normal * places
    print(f"{price:.2f} leva")

elif type == "Discount":
    price = disscount * places
    print(f"{price:.2f} leva")


