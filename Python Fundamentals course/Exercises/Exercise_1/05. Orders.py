number_of_order = int(input())
total_price = 0

for i in range(number_of_order):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsules_for_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
       continue
    elif days < 1 or days > 31:
        continue
    elif needed_capsules_for_day < 1 or needed_capsules_for_day > 2000:
        continue

    full_price_per_day = price_per_capsule * days * needed_capsules_for_day
    print(f"The price for the coffee is: ${full_price_per_day:.2f}")
    total_price += full_price_per_day

print(f"Total: ${total_price:.2f}")