money = " "
money_2 = 0
sum = 0

while money != "NoMoreMoney":
    money = input()
    if money != "NoMoreMoney":
        money_2 = float(money)
        if money_2 < 0:
            print("Invalid operation!")
            break
        sum += money_2
        print(f"Increase: {money_2:.2f}")
    else:
        break

print(f"Total: {sum:.2f}")
