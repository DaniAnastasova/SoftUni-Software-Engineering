days = int(input())
room_type = input()
feedback = input()

nights = days - 1
total_price = 0.0

if room_type == "room for one person":
    total_price = nights * 18.00


elif room_type == "apartment":
    total_price = nights * 25.00

    if days < 10:
        total_price *= 0.70
    elif 10 <= days <= 15:
        total_price *= 0.65
    elif days > 15:
        total_price *= 0.50

elif room_type == "president apartment":
    total_price = nights * 35.00
    if days < 10:
        total_price *= 0.90
    elif 10 <= days <= 15:
        total_price *= 0.85
    elif days > 15:
        total_price *= 0.80


if feedback == "positive":
    total_price *= 1.25
elif feedback == "negative":
    total_price *= 0.90


print(f"{total_price:.2f}")