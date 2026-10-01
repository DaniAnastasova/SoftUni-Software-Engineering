number_of_snowball = int(input())
snowball_value = 0
max_value = 0

weight_of_the_highest_snowball = 0
time_of_the_highest_snowball = 0
quality_of_the_highest_snowball = 0

for i in range(number_of_snowball):
    weight_of_the_snowball = int(input())
    time_needed = int(input())
    quality = int(input())

    snowball_value = (weight_of_the_snowball // time_needed) ** quality
    if snowball_value > max_value:
        max_value = snowball_value
        weight_of_the_highest_snowball = weight_of_the_snowball
        time_of_the_highest_snowball = time_needed
        quality_of_the_highest_snowball = quality

print(f"{weight_of_the_highest_snowball} : {time_of_the_highest_snowball} = {max_value} ({quality_of_the_highest_snowball})")



