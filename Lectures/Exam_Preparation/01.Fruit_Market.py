price_strawberry = float(input())
kg_bananas = float(input())
kg_oranges = float(input())
kg_raspberrys = float(input())
kg_strawberrys = float(input())

sum = 0

price_raspberry = price_strawberry / 2
price_oranges = price_raspberry - ((40/100)*price_raspberry)
price_bananas = price_raspberry - ((80/100)*price_raspberry)

sum = price_strawberry * kg_strawberrys + kg_bananas * price_bananas + kg_oranges * price_oranges + kg_raspberrys * price_raspberry

print(f"{(sum):.2f}")
