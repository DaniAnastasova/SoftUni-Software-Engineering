points = int(input())
bonus = 0

if points <= 100:
    bonus = 5
    if points % 2 == 0:
        bonus += 1
    if points % 10 == 5:
        bonus += 2
    print(bonus)
    print(bonus+points)
elif points > 100 and points <= 1000:
    bonus = (20/100) * points
    if points % 2 == 0:
        bonus += 1
    if points % 10 == 5:
        bonus += 2
    print(bonus)
    print(bonus+points)
elif points > 1000:
    bonus = (10 / 100) * points
    if points % 2 == 0:
        bonus += 1
    if points % 10 == 5:
        bonus += 2
    print(bonus)
    print(bonus + points)



