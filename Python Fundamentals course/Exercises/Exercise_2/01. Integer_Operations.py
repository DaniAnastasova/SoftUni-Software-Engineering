from math import floor

first_integer = int(input())
second_integer = int(input())
third_integer = int(input())
fourth_integer = int(input())

result_after_divide = (first_integer + second_integer) / third_integer
result_after_divide = floor(result_after_divide)

final_result = result_after_divide * fourth_integer


print(int(final_result))