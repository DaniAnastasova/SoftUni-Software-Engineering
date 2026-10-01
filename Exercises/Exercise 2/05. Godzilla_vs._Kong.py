budget_for_film = float(input())
count_statists = int(input())
price_for_clothes_for_1_statist = float(input())

price_for_dekor = (10/100) * budget_for_film

price_for_clothes = count_statists * price_for_clothes_for_1_statist

if count_statists > 150:
    discout = (10/100) * price_for_clothes
    price_for_clothes = price_for_clothes - discout

if (price_for_clothes + price_for_dekor) > budget_for_film:
    print("Not enough money!")
    print(f"Wingard needs {((price_for_clothes + price_for_dekor) - budget_for_film):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(budget_for_film - (price_for_clothes + price_for_dekor)):.2f} leva left.")