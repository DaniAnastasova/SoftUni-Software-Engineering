lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_sum = 0
count_shield_breaks = 0

for i in range(1, lost_fights_count+1):
    if i % 2 == 0 and i % 3 == 0:
        total_sum += shield_price + helmet_price + sword_price
        count_shield_breaks += 1
        if count_shield_breaks % 2 == 0:
            total_sum += armor_price
        continue
    if i % 2 == 0:
        total_sum += helmet_price
    if i % 3 == 0:
        total_sum += sword_price

print(f"Gladiator expenses: {total_sum:.2f} aureus")
