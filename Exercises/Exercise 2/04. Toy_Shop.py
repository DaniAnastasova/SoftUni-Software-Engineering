puzzle = 2.60
talking_doll = 3
teddy_bear = 4.10
minion = 8.20
truck = 2

price_trip = float(input())
count_puzzles = int(input())
count_talking_dolls = int(input())
count_teddy_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

sum = count_puzzles * puzzle + count_talking_dolls * talking_doll + count_teddy_bears * teddy_bear + count_minions * minion+ count_trucks * truck

count_toys = count_puzzles + count_talking_dolls + count_teddy_bears + count_minions + count_trucks
discount = 0

if count_toys >= 50:
    discount = (25/100) * sum
    sum = sum - discount

rent = (10/100) * sum

sum = sum - rent

if sum >= price_trip:
    print(f"Yes! {sum - price_trip:.2f} lv left.")
else:
    print(f"Not enough money! {(price_trip - sum):.2f} lv needed.")