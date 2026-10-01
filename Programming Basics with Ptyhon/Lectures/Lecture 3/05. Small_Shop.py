product = input()
town = input()
quantity = float(input())
price = 0

if product == 'coffee':
    if town == 'Sofia':
        price = quantity * 0.50
        print(price)
    elif town == 'Plovdiv':
        price = quantity * 0.40
        print(price)
    elif town == 'Varna':
        price = quantity * 0.45
        print(price)

elif product == 'water':
    if town == 'Sofia':
        price = quantity * 0.80
        print(price)
    elif town == 'Plovdiv':
        price = quantity * 0.70
        print(price)
    elif town == 'Varna':
        price = quantity * 0.70
        print(price)

elif product == 'beer':
    if town == 'Sofia':
        price = quantity * 1.20
        print(price)
    elif town == 'Plovdiv':
        price = quantity * 1.15
        print(price)
    elif town == 'Varna':
        price = quantity * 1.10
        print(price)

elif product == 'sweets':
    if town == 'Sofia':
        price = quantity * 1.45
        print(price)
    elif town == 'Plovdiv':
        price = quantity * 1.30
        print(price)
    elif town == 'Varna':
        price = quantity * 1.35
        print(price)

elif product == 'peanuts':
    if town == 'Sofia':
        price = quantity * 1.60
        print(price)
    elif town == 'Plovdiv':
        price = quantity * 1.50
        print(price)
    elif town == 'Varna':
        price = quantity * 1.55
        print(price)
