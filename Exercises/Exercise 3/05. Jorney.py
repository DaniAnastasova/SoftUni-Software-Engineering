budget = float(input())
season = input()
price = 0

if budget <= 100:
    if season == "summer":
        price = (30/100) * budget
        print(f"Somewhere in Bulgaria")
        print(f"Camp - {price:.2f}")
    elif season == "winter":
        price = (70/100) * budget
        print(f"Somewhere in Bulgaria")
        print(f"Hotel - {price:.2f}")

elif budget <= 1000:
    if season == "summer":
        price = (40/100) * budget
        print(f"Somewhere in Balkans")
        print(f"Camp - {price:.2f}")
    elif season == "winter":
        price = (80/100) * budget
        print(f"Somewhere in Balkans")
        print(f"Hotel - {price:.2f}")

elif budget > 1000:
        price = (90/100) * budget
        print(f"Somewhere in Europe")
        print(f"Hotel - {price:.2f}")

