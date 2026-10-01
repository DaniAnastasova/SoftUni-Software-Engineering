predpazen_nailon = 1.50
paint = 14.50
razreditel_za_boq = 5

nailon = int(input())
boq = int(input())
razreditel= int(input())
hours = int(input())

sum = ((nailon+2) * predpazen_nailon) + ((boq + ((10/100)* boq))* paint) + 0.40 + (razreditel_za_boq * razreditel)
price_for_workman = (30/100) * sum
sum = sum + (price_for_workman * hours)

print(f"{sum}")
