start_num = int(input())
end_num = int(input())
magic_num = int(input())
combination = 0
current_cobination = 0

for i in range(start_num,end_num+1):
    for j in range(start_num,end_num+1):
        combination += 1
        if (i + j == magic_num):
            current_cobination = combination
            print(f"Combination N:{current_cobination} ({i} + {j} = {magic_num})")
            break
    if current_cobination != 0:
        break


if current_cobination == 0:
    print(f"{combination} combinations - neither equals {magic_num}")