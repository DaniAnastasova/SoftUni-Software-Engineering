def sum_numbers(first_number,second_number):
    list_of_numbers = [first_number,second_number]
    return sum(list_of_numbers)

def subtract(result_from_function ,third_number):
    result = result_from_function - third_number
    return result

def add_and_subtract(first_number,second_number, third_number):
    result_from_sum = sum_numbers(first_number,second_number)
    result_from_sub = subtract(result_from_sum,third_number)
    return result_from_sub

first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num,second_num,third_num))

