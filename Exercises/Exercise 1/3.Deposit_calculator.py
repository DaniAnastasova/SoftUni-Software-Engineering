deposit = float(input())
deposit_months = int(input())
year_procent= float(input())

sum = deposit + deposit_months * ((deposit * (year_procent/100)) / 12)
print(sum)