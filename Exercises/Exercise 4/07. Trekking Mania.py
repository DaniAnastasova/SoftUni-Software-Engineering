count_group = int(input())
people_in_group = 0

count_people_for_Musala = 0
count_people_for_Monblan = 0
count_people_for_Kilimandjaro = 0
count_people_for_K2 = 0
count_people_for_Everest = 0

people_count = 0
for i in range(count_group):
    people_in_group = int(input())
    people_count += people_in_group
    if people_in_group <= 5:
        count_people_for_Musala += people_in_group
    elif people_in_group >= 6 and people_in_group <= 12:
        count_people_for_Monblan += people_in_group
    elif people_in_group >= 13 and people_in_group <= 25:
        count_people_for_Kilimandjaro += people_in_group
    elif people_in_group >= 26 and people_in_group <= 40:
        count_people_for_K2 += people_in_group
    elif people_in_group >= 41:
        count_people_for_Everest += people_in_group

print(f"{(count_people_for_Musala / people_count * 100):.2f}%")
print(f"{(count_people_for_Monblan / people_count * 100):.2f}%")
print(f"{(count_people_for_Kilimandjaro / people_count * 100):.2f}%")
print(f"{(count_people_for_K2 / people_count * 100):.2f}%")
print(f"{(count_people_for_Everest / people_count * 100):.2f}%")

