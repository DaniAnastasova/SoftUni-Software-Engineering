chicken_menu = 10.35
menu_with_fish = 12.40
vegetarian_menu = 8.15
delivery_price = 2.50

count_chicken_menu = int(input())
count_menu_with_fish = int(input())
count_vegetarian_menu = int(input())

sum = count_chicken_menu * chicken_menu + count_menu_with_fish * menu_with_fish + count_vegetarian_menu * vegetarian_menu
desert_pirce = (20/100) * sum
sum = sum + desert_pirce + delivery_price

print(f"{sum}")