meter = float(input())

price = 7.61 * meter
discount = (18/100) * price
total_price = price - discount

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")