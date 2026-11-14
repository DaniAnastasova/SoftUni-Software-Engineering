price_ratings = [int(x) for x in input().split(", ")]
entry_point = int(input())
type_of_object = input()

price_entry_point = price_ratings[entry_point]
left_sum = 0
right_sum = 0

for i in range(0, entry_point):
    current_price = price_ratings[i]
    if type_of_object == "cheap":
        if current_price < price_entry_point:
            left_sum += current_price

    elif type_of_object == "expensive":
        if current_price >= price_entry_point:
            left_sum += current_price


for i in range(entry_point + 1, len(price_ratings)):
    current_price = price_ratings[i]
    if type_of_object == "cheap":
        if current_price < price_entry_point:
            right_sum += current_price
    elif type_of_object == "expensive":
        if current_price >= price_entry_point:
            right_sum += current_price


if right_sum > left_sum:
    print(f"Right - {right_sum}")
elif left_sum > right_sum:
    print(f"Left - {left_sum}")
elif right_sum == left_sum:
    print(f"Left - {left_sum}")
