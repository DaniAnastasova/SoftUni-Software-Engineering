import math

name = input()
duration_episode = int(input())
duration_break = int(input())

break_to_lunch = (1/8) * duration_break
break_to_recreation = (1/4) * duration_break

sum_time = break_to_lunch + break_to_recreation + duration_episode

if sum_time <= duration_break:
    print(f"You have enough time to watch {name} and left with {math.ceil(duration_break - sum_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(sum_time - duration_break)} more minutes.")