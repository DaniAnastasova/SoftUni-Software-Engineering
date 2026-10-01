lenght = int(input())
high = int(input())

full_count_cake_parts = lenght * high
count_cake_parts = ""
ostanali_parcheta = 0
obshto_sotanali_parcheta = 0

while True:
    count_cake_parts = input()
    if count_cake_parts != "STOP":
        count_cake_parts = int(count_cake_parts)
        if count_cake_parts <= full_count_cake_parts:
            ostanali_parcheta = full_count_cake_parts - count_cake_parts
            full_count_cake_parts -= count_cake_parts
        else:
            print(f"No more cake left! You need {(count_cake_parts - full_count_cake_parts)} pieces more.")
            break

    elif count_cake_parts == "STOP":
        if ostanali_parcheta >= 0:
            print(f"{ostanali_parcheta} pieces are left.")
            break

