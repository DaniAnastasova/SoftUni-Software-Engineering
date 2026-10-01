import math

days = int(input())
all_food = float(input())

dog_food = 0
cat_food = 0

buscuit_quantity = 0
all_food_for_day = 0
all_dog_food = 0
all_cat_food = 0

percent_eat_food = 0
percent_eat_food_for_dog = 0
percent_eat_food_for_cat = 0

for i in range(1,days+1):
    dog_food = int(input())
    all_dog_food += dog_food
    cat_food = int(input())
    all_cat_food += cat_food
    all_eat_food_for_day = all_dog_food + all_cat_food
    if i % 3 == 0:
        all_food_for_thirtd_fay = dog_food + cat_food
        buscuit_quantity  +=  (10/100) * all_food_for_thirtd_fay


print(f"Total eaten biscuits: {round(buscuit_quantity)}gr.")
percent_eat_food = (all_eat_food_for_day / all_food) * 100
print(f"{(percent_eat_food):.2f}% of the food has been eaten.")
percent_eat_food_for_dog = (all_dog_food / all_eat_food_for_day) * 100
print(f"{(percent_eat_food_for_dog):.2f}% eaten from the dog.")
percent_eat_food_for_cat = (all_cat_food / all_eat_food_for_day) * 100
print(f"{(percent_eat_food_for_cat):.2f}% eaten from the cat.")