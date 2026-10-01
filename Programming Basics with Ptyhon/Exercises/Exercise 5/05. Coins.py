resto = float(input())
moneti = 0

while resto > 0:
    while resto >= 2:
        moneti += 1
        resto = round(resto - 2, 2)

    while resto >= 1:
        moneti += 1
        resto = round(resto - 1, 2)

    while resto >= 0.50:
        moneti += 1
        resto = round(resto - 0.50, 2)

    while resto >= 0.20:
        moneti += 1
        resto = round(resto - 0.20, 2)

    while resto >= 0.10:
        moneti += 1
        resto = round(resto - 0.10, 2)

    while resto >= 0.05:
        moneti += 1
        resto = round(resto - 0.05, 2)

    while resto >= 0.02:
        moneti += 1
        resto = round(resto - 0.02, 2)

    while resto >= 0.01:
        moneti += 1
        resto = round(resto - 0.01, 2)


print(moneti)