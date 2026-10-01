command = ""
meters = 0
all_meters = 5364
days = 1

while command != "END":
    command = input()
    if command == "END":
        break
    meters = int(input())
    if command == "Yes":
        days += 1
    if days > 5:
        break
    all_meters += meters
    if all_meters >= 8848:
        print(f"Goal reached for {days} days!")
        break

if days > 5 or all_meters < 8848:
    print("Failed!")
    print(f"{all_meters}")
