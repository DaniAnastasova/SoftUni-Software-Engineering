time_1 = int(input())
time_2 = int(input())
time_3 = int(input())

total = time_1 + time_2 + time_3

minutes = total // 60
seconds = total % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
