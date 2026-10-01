from math import pi

type = input()
a = 0
result = 0
if type == "square":
    a = float(input())
    result = a * a
    print(f"{result:.3f}")
elif type == "rectangle":
    a = float(input())
    b = float(input())
    result = a * b
    print(f"{result:.3f}")
elif type == "circle":
    a = float(input())
    result = pi * a * a
    print(f"{result:.3f}")
elif type == "triangle":
    a = float(input())
    b = float(input())
    result = (a * b) /2
    print(f"{result:.3f}")
