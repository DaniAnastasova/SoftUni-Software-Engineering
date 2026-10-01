paket_pencils = 5.80
paket_mrkers = 7.20
preparat_per_liter = 1.20

count_pakets_penclis = int(input())
count_pakets_markers = int(input())
liters_preparat = int(input())
discount = int(input())

sum = count_pakets_penclis * paket_pencils + count_pakets_markers * paket_mrkers + preparat_per_liter * liters_preparat
sum = sum - ((discount/100) * sum)
print(sum)
