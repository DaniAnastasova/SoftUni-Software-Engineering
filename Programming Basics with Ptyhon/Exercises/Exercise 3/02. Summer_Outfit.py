degrees = int(input())
time = input()


if time == "Morning":
    if degrees >= 10 and degrees <= 18:
        print(f"It's {degrees} degrees, get your Sweatshirt and Sneakers.")
    elif degrees > 18 and degrees <= 24:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif degrees >= 25:
        print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")

elif time == "Afternoon":
    if degrees >= 10 and degrees <= 18:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif degrees > 18 and degrees <= 24:
        print(f"It's {degrees} degrees, get your T-Shirt and Sandals.")
    elif degrees >= 25:
        print(f"It's {degrees} degrees, get your Swim Suit and Barefoot.")

elif time == "Evening":
    if degrees >= 10 and degrees <= 18:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif degrees > 18 and degrees <= 24:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")
    elif degrees >= 25:
        print(f"It's {degrees} degrees, get your Shirt and Moccasins.")

