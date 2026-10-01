spend_money = 0
total_spirit = 0

quantity_of_decoration = int(input())
days_left_until_Christmas = int(input())

price_ornament_set = 2
price_tree_skirt = 5
price_tree_garland = 3
price_tree_lights = 15

for day in range(1,days_left_until_Christmas+1):
    if day % 11 == 0:
        quantity_of_decoration += 2
    if day % 2 == 0:
      spend_money += price_ornament_set *  quantity_of_decoration
      total_spirit += 5
    if day % 3 == 0:
      spend_money += (price_tree_skirt + price_tree_garland) * quantity_of_decoration
      total_spirit += 13
    if day % 5 == 0:
        spend_money += (price_tree_lights) * quantity_of_decoration
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        spend_money += price_tree_skirt + price_tree_garland + price_tree_lights


if days_left_until_Christmas % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {spend_money}")
print(f"Total spirit: {total_spirit}")