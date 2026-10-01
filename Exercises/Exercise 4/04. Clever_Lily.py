Lily_age = int(input())
price_for_washing_mashine = float(input())
price_for_toy = int(input())
count_toy = 0
money_for_birtday = 0
budget_liLy = 0
age = 1
money_for_lily_brother = 0

for age in range(1,Lily_age+1):
    if age % 2 == 0:
        money_for_birtday += ((age / 2) * 10)
        money_for_lily_brother += 1
    else:
        count_toy += 1

budget_liLy = money_for_birtday + (count_toy * price_for_toy) - money_for_lily_brother

if budget_liLy >= price_for_washing_mashine:
    print(f"Yes! {(budget_liLy - price_for_washing_mashine):.2f}")
else:
    print(f"No! {(price_for_washing_mashine - budget_liLy):.2f}")

