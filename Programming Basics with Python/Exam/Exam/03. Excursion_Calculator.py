people_count = int(input())
season = input()
sum = 0

if season == "spring":
    if people_count <= 5:
        sum = people_count * 50
    elif people_count > 5:
        sum = people_count * 48

    print(f"{(sum):.2f} leva.")

elif season == "summer":
    if people_count <= 5:
        sum = people_count * 48.50
    elif people_count > 5:
        sum = people_count * 45
    sum = sum - ((15/100)*sum)
    print(f"{(sum):.2f} leva.")

elif season == "autumn":
    if people_count <= 5:
        sum = people_count * 60
    elif people_count > 5:
        sum = people_count * 49.50

    print(f"{(sum):.2f} leva.")

elif season == "winter":
    if people_count <= 5:
        sum = people_count * 86
    elif people_count > 5:
        sum = people_count * 85
    sum = sum + ((8/100)*sum)
    print(f"{(sum):.2f} leva.")