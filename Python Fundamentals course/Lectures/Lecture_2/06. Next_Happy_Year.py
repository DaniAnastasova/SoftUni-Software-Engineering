year = int(input())

while True:
    year += 1
    set_year = set(str(year))
    if len(set_year) == len(str(year)):
        print(year)
        break
