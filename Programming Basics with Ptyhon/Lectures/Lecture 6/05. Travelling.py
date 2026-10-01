destination = ""
min_budget = 0
full_sum = 0
sum = 0

while True:
    destination = input()
    if destination == "End":
        break
    min_budget = float(input())


    while True:
        sum = float(input())
        full_sum += sum
        if full_sum >= min_budget:
            print(f"Going to {destination}!")
            full_sum = 0
            break


