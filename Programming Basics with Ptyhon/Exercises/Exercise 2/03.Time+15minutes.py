hour = int(input())
minutes = int(input())

result = minutes + 15

if hour != 23 and result > 59:
    hour+=1
    minutes = result - 60
    if minutes < 10:
        print(f"{hour}:0{minutes}")
    else:
        print(f"{hour}:{minutes}")

elif hour == 23 and result > 59:
    hour = 0
    minutes = result - 60
    if minutes == 0:
        print(f"{hour}:{minutes}0")
    elif minutes < 10:
        print(f"{hour}:0{minutes}")
    else:
        print(f"{hour}:{minutes}")

else:
    print(f"{hour}:{minutes+15}")
