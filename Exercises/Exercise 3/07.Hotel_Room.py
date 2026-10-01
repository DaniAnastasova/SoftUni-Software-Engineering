month = input()
count_nights = int(input())
price_for_studio = 0
price_for_apartament = 0
discount = 0

if month == "May" or month == "October":
    price_for_studio = count_nights * 50
    price_for_apartament = count_nights * 65
    if count_nights > 14:
        discount = (30 / 100) * price_for_studio
        price_for_studio = price_for_studio - discount
        price_for_apartament = price_for_apartament - ((10 / 100) * price_for_apartament)
        print(f"Apartment: {price_for_apartament:.2f} lv.")
        print(f"Studio: {price_for_studio:.2f} lv.")

    elif count_nights > 7:
        discount = (5 / 100) * price_for_studio
        price_for_studio = price_for_studio - discount
        print(f"Apartment: {price_for_apartament:.2f} lv.")
        print(f"Studio: {price_for_studio:.2f} lv.")

    else:
        print(f"Apartment: {price_for_apartament:.2f} lv.")
        print(f"Studio: {price_for_studio:.2f} lv.")

elif month == "June" or month == "September":
    price_for_studio = count_nights * 75.20
    price_for_apartament = count_nights * 68.70
    if count_nights <= 14:
        print(f"Apartment: {price_for_apartament:.2f} lv.")
        print(f"Studio: {price_for_studio:.2f} lv.")
    else:
        price_for_studio = price_for_studio - ((20 / 100) * price_for_studio)
        price_for_apartament = price_for_apartament - ((10 / 100) * price_for_apartament)
        print(f"Apartment: {price_for_apartament:.2f} lv.")
        print(f"Studio: {price_for_studio:.2f} lv.")


elif month == "July" or month == "August":
    price_for_studio = count_nights * 76
    price_for_apartament = count_nights * 77
    if count_nights <= 14:
        print(f"Apartment: {price_for_apartament:.2f} lv.")
        print(f"Studio: {price_for_studio:.2f} lv.")
    else:
        price_for_apartament = price_for_apartament - ((10 / 100) * price_for_apartament)
        print(f"Apartment: {price_for_apartament:.2f} lv.")
        print(f"Studio: {price_for_studio:.2f} lv.")

