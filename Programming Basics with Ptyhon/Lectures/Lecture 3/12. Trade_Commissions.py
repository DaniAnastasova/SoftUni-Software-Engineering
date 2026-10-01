town = input()
quantity = float(input())
commission = 0

if quantity == 0 or quantity <= 500 and quantity > 0:
    if town == "Sofia":
        commission = (5/100) * quantity
        print(f"{commission:.2f}")
    elif town == "Varna":
        commission = (4.5/100) * quantity
        print(f"{commission:.2f}")
    elif town == "Plovdiv":
        commission = (5.5/100) * quantity
        print(f"{commission:.2f}")
    else:
        print("error")

elif quantity > 500 and quantity <= 1000:
    if town == "Sofia":
        commission = (7/100) * quantity
        print(f"{commission:.2f}")
    elif town == "Varna":
        commission = (7.5/100) * quantity
        print(f"{commission:.2f}")
    elif town == "Plovdiv":
        commission = (8/100) * quantity
        print(f"{commission:.2f}")
    else:
        print("error")

elif quantity > 1000 and quantity <= 10000:
    if town == "Sofia":
        commission = (8/100) * quantity
        print(f"{commission:.2f}")
    elif town == "Varna":
        commission = (10/100) * quantity
        print(f"{commission:.2f}")
    elif town == "Plovdiv":
        commission = (12/100) * quantity
        print(f"{commission:.2f}")
    else:
        print("error")

elif quantity > 10000:
    if town == "Sofia":
        commission = (12/100) * quantity
        print(f"{commission:.2f}")
    elif town == "Varna":
        commission = (13/100) * quantity
        print(f"{commission:.2f}")
    elif town == "Plovdiv":
        commission = (14.5/100) * quantity
        print(f"{commission:.2f}")
    else:
        print("error")
elif quantity < 0:
    print("error")
else:
    print("error")