flower_type = input()
count_flowers = int(input())
budget = int(input())

rose = 5
daliq = 3.80
lale = 2.80
narcis = 3
gladiola = 2.50
price = 0
discount = 0

if flower_type == "Roses":
    price = count_flowers * rose
    if count_flowers > 80:
        discount = (10/100) * price
        price = price - discount
        if price <= budget:
            print(f"Hey, you have a great garden with {count_flowers} {flower_type} and {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money, you need {(price - budget):.2f} leva more.")
    else:
        if price <= budget:
            print(f"Hey, you have a great garden with {count_flowers} {flower_type} and {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money, you need {(price - budget):.2f} leva more.")

elif flower_type == "Dahlias":
    price = count_flowers * daliq
    if count_flowers > 90:
        discount = (15/100) * price
        price = price - discount
        if price <= budget:
            print(f"Hey, you have a great garden with {count_flowers} {flower_type} and {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money, you need {(price - budget):.2f} leva more.")
    else:
        if price <= budget:
            print(f"Hey, you have a great garden with {count_flowers} {flower_type} and {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money, you need {(price - budget):.2f} leva more.")

elif flower_type == "Tulips":
    price = count_flowers * lale
    if count_flowers > 80:
        discount = (15/100) * price
        price = price - discount
        if price <= budget:
            print(f"Hey, you have a great garden with {count_flowers} {flower_type} and {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money, you need {(price - budget):.2f} leva more.")
    else:
        if price <= budget:
            print(f"Hey, you have a great garden with {count_flowers} {flower_type} and {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money, you need {(price - budget):.2f} leva more.")


elif flower_type == "Narcissus":
    price = count_flowers * narcis
    if count_flowers < 120:
        discount = (15/100) * price
        price = price + discount
        if price <= budget:
            print(f"Hey, you have a great garden with {count_flowers} {flower_type} and {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money, you need {(price - budget):.2f} leva more.")
    else:
        if price <= budget:
            print(f"Hey, you have a great garden with {count_flowers} {flower_type} and {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money, you need {(price - budget):.2f} leva more.")

elif flower_type == "Gladiolus":
    price = count_flowers * gladiola
    if count_flowers < 80:
        discount = (20/100) * price
        price = price + discount
        if price <= budget:
            print(f"Hey, you have a great garden with {count_flowers} {flower_type} and {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money, you need {(price - budget):.2f} leva more.")
    else:
        if price <= budget:
            print(f"Hey, you have a great garden with {count_flowers} {flower_type} and {(budget - price):.2f} leva left.")
        else:
            print(f"Not enough money, you need {(price - budget):.2f} leva more.")