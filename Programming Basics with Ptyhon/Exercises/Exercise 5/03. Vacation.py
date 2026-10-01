price_for_trip = float(input())
money = float(input())
days = 0
spend_or_save = ""
money_for_spend_or_save = 0
spending_counter = 0

while(price_for_trip > money):
    spend_or_save = input()
    money_for_spend_or_save = float(input())
    days += 1
    if spend_or_save == "save":
        money += money_for_spend_or_save
        spending_counter = 0
    elif spend_or_save == "spend":
        spending_counter += 1
        if spending_counter == 5:
            print("You can't save the money.")
            print(f"{days}")
            break
        if money >= money_for_spend_or_save:
            money -= money_for_spend_or_save
        else:
            money_for_spend_or_save -= money
            money = 0

    if money >= price_for_trip:
        print(f"You saved the money for {days} days.")
        break


