price_TShirt = float(input())
current_sum = float(input())
all_sum = 0

price_shorts = (75/100) * price_TShirt
price_socks = (20/100) * price_shorts
price_shoes = 2 * (price_TShirt + price_shorts)

all_sum = price_TShirt + price_shorts + price_socks + price_shoes
all_sum = all_sum - ((15/100)*all_sum)

if all_sum >= current_sum:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {(all_sum):.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {(current_sum-all_sum):.2f} lv. more.")