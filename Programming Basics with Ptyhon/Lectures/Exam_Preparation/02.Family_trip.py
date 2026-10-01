budget = float(input())
count_night = int(input())
price_night = float(input())
percent_additional_costs = int(input())
full_sum = 0

if count_night > 7:
    price_night = price_night - ((5/100)*price_night)

additional_costs = (percent_additional_costs / 100) * budget

full_sum = additional_costs + price_night * count_night

if full_sum <= budget:
    print(f"Ivanovi will be left with {(budget - full_sum):.2f} leva after vacation.")
else:
    print(f"{(full_sum - budget):.2f} leva needed.")
