rent_in_spring = 3000
rent_in_summer_and_autumn = 4200
rent_in_winter = 2600

budget = int(input())
season = input()
count = int(input())

price = 0

if season == "Spring":
    if count <= 6:
        rent_in_spring = rent_in_spring - (rent_in_spring * (10 / 100))
        price = rent_in_spring
        if count % 2 == 0:
            price = rent_in_spring - ((5 / 100) * rent_in_spring)
        else:
            price = rent_in_spring
        if budget >= price:
            print(f"Yes! You have {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(price - budget):.2f} leva.")
    elif count >= 7 and count <= 11:
        rent_in_spring = rent_in_spring - (rent_in_spring * (15 / 100))
        price = rent_in_spring
        if count % 2 == 0:
            price = rent_in_spring - ((5 / 100) * rent_in_spring)
        else:
            price = rent_in_spring
        if budget >= price:
            print(f"Yes! You have {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(price - budget):.2f} leva.")
    elif count >= 12:
        rent_in_spring = rent_in_spring - (rent_in_spring * (25 / 100))
        price = rent_in_spring
        if count % 2 == 0:
            price = rent_in_spring - ((5 / 100) * rent_in_spring)
        else:
            price = rent_in_spring
        if budget >= price:
            print(f"Yes! You have {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(price - budget):.2f} leva.")

elif season == "Summer" :
    if count <= 6:
        rent_in_summer_and_autumn = rent_in_summer_and_autumn - (rent_in_summer_and_autumn * (10 / 100))
        if count % 2 == 0:
            price = rent_in_summer_and_autumn - ((5 / 100) * rent_in_summer_and_autumn)
        else:
            price = rent_in_summer_and_autumn
        if budget >= price:
            print(f"Yes! You have {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(price - budget):.2f} leva.")
    elif count >= 7 and count <= 11:
        rent_in_summer_and_autumn = rent_in_summer_and_autumn - (rent_in_summer_and_autumn * (15 / 100))
        if count % 2 == 0:
            price = rent_in_summer_and_autumn - ((5 / 100) * rent_in_summer_and_autumn)
        else:
            price = rent_in_summer_and_autumn
        if budget >= price:
            print(f"Yes! You have {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(price - budget):.2f} leva.")
    elif count >= 12:
        rent_in_summer_and_autumn = rent_in_summer_and_autumn - (rent_in_summer_and_autumn * (25 / 100))
        if count % 2 == 0:
            price = rent_in_summer_and_autumn - ((5 / 100) * rent_in_summer_and_autumn)
        else:
            price = rent_in_summer_and_autumn
        if budget >= price:
            print(f"Yes! You have {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(price - budget):.2f} leva.")

elif season == "Autumn":
    if count <= 6:
        rent_in_summer_and_autumn = rent_in_summer_and_autumn - (rent_in_summer_and_autumn * (10 / 100))
        price = rent_in_summer_and_autumn
        if budget >= price:
            print(f"Yes! You have {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(price - budget):.2f} leva.")
    elif count >= 7 and count <= 11:
        rent_in_summer_and_autumn = rent_in_summer_and_autumn - (rent_in_summer_and_autumn * (15 / 100))
        price = rent_in_summer_and_autumn
        if budget >= price:
            print(f"Yes! You have {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(price - budget):.2f} leva.")
    elif count >= 12:
        rent_in_summer_and_autumn = rent_in_summer_and_autumn - (rent_in_summer_and_autumn * (25 / 100))
        price = rent_in_summer_and_autumn
        if budget >= price:
            print(f"Yes! You have {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(price - budget):.2f} leva.")

elif season == "Winter":
    if count <= 6:
        rent_in_winter = rent_in_winter - (rent_in_winter * (10 / 100))
        if count % 2 == 0:
            price = rent_in_winter - ((5 / 100) * rent_in_winter)
        else:
            price = rent_in_winter
        if budget >= price:
            print(f"Yes! You have {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(price - budget):.2f} leva.")
    elif count >= 7 and count <= 11:
        rent_in_winter = rent_in_winter - (rent_in_winter * (15 / 100))
        if count % 2 == 0:
            price = rent_in_winter - ((5 / 100) * rent_in_winter)
        else:
            price = rent_in_winter
        if budget >= price:
            print(f"Yes! You have {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(price - budget):.2f} leva.")
    elif count >= 12:
        rent_in_winter = rent_in_winter - (rent_in_winter * (25 / 100))
        if count % 2 == 0:
            price = rent_in_winter - ((5 / 100) * rent_in_winter)
        else:
            price = rent_in_winter
        if budget >= price:
            print(f"Yes! You have {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money! You need {(price - budget):.2f} leva.")