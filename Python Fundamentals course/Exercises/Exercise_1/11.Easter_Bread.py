budget = float(input())
price_one_kg_flour = float(input())
price_one_pack_of_eggs = (75/100) * price_one_kg_flour
price_for_one_milk = ((25/100) * price_one_kg_flour) + price_one_kg_flour

price_for_milk = (price_for_one_milk / 1000) * 250

price_per_one_bread = price_one_pack_of_eggs + price_one_kg_flour + price_for_milk
count_colored_egs = 0
count_bread = 0

while budget >= price_per_one_bread:
    budget -= price_per_one_bread
    count_colored_egs += 3
    count_bread += 1
    if count_bread % 3 == 0:
        count_colored_egs -= (count_bread - 2)

print(f"You made {count_bread} loaves of Easter bread! Now you have {count_colored_egs} eggs and {budget:.2f}BGN left.")