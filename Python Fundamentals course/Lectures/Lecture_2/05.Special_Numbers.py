n = int(input())
result = 0

for i in range(1, n+1):
    if i < 10:
        if i == 5 or i == 7 or i == 11:
            print(f"{i} -> True")
        else:
            print(f"{i} -> False")
    if i >= 10:
        left_part = i // 10
        right_part = i % 10
        result += left_part + right_part
        if result == 5 or result == 7 or result == 11:
            print(f"{i} -> True")
        else:
            print(f"{i} -> False")

        left_part = 0
        right_part = 0
        result = 0