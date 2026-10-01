import math

str_in_book = int(input())
str_per_one_hour = int(input())
count_days = int(input())

hours =  math.floor(str_in_book / str_per_one_hour)

final_result = math.floor(hours / count_days)

print(final_result)

