budget = float(input())
count_videocard = int(input())
count_processor = int(input())
count_ram = int(input())

price_per_1_videocard = 250
price_videocards = price_per_1_videocard * count_videocard
price_per_1_processor = (35/100) * price_videocards
price_per_1_ram = (10/100) * price_videocards

sum = price_videocards + (count_processor * price_per_1_processor) + (count_ram * price_per_1_ram)

if count_videocard > count_processor:
    sum = sum - ((15/100)*sum)

if budget >= sum:
    print(f"You have {(budget - sum):.2f} leva left!")
else:
    print(f"Not enough money! You need {(sum - budget):.2f} leva more!")