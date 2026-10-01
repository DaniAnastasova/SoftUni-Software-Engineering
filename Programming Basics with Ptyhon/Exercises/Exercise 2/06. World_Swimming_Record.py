import math

record_in_seconds = float(input())
meter = float(input())
seconds_for_1_meter = float(input())

times = math.floor(meter / 15)

result = (meter * seconds_for_1_meter) + (times * 12.5)

if result < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {result:.2f} seconds.")
else:
    print(f"No, he failed! He was {(result - record_in_seconds):.2f} seconds slower.")