n = int(input())
quantity_alcoloh = 0
gradus = 0
all_quantity = 0
all_gradus = 0
full_gradus = 0
average_gradus = 0

for i in range(n):
    quantity_alcoloh  = float(input())
    gradus = float(input())

    all_quantity += quantity_alcoloh
    all_gradus = quantity_alcoloh * gradus
    full_gradus += all_gradus

average_gradus = full_gradus / all_quantity

print(f"Liter: {(all_quantity):.2f}")
print(f"Degrees: {(average_gradus):.2f}")

if average_gradus < 38:
    print("Not good, you should baking!")
elif average_gradus >= 38 and average_gradus <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")


