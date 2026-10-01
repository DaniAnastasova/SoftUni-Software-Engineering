text = input()

a = 1
e = 2
i = 3
o = 4
u = 5

sum = 0
for char in text:
    if char == "a":
        sum += a
    elif char == "e":
        sum += e
    elif char == "i":
        sum += i
    elif char == "o":
        sum += o
    elif char == "u":
        sum += u

print(sum)