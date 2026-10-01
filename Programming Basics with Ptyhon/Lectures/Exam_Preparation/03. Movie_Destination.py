film_budget = float(input())
destination = input()
season = input()
days = int(input())
sum = 0

if season == "Winter":
    if destination == "Dubai":
        sum = days * 45000
        sum = sum - ((30/100)*sum)
    elif destination == "Sofia":
        sum = days * 17000
        sum = sum + ((25/100)*sum)
    elif destination == "London":
        sum = days * 24000

elif season == "Summer":
    if destination == "Dubai":
        sum = days * 40000
        sum = sum - ((30/100)*sum)
    elif destination == "Sofia":
        sum = days * 12500
        sum = sum + ((25/100)*sum)
    elif destination == "London":
        sum = days * 20250


if sum <= film_budget:
    print(f"The budget for the movie is enough! We have {(film_budget - sum):.2f} leva left!")

else:
    print(f"The director needs {(sum - film_budget):.2f} leva more!")