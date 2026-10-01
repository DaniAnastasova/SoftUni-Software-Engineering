actor_name = input()
points = float(input())
n = int(input())

actor_points = points

name_evaluate = ""
points_from_evaluate = 0
name_lenght = 0
for i in range(n):
    name_evaluate = input()
    points_from_evaluate = float(input())
    name_lenght = len(name_evaluate)
    actor_points += (name_lenght * points_from_evaluate) /2
    if actor_points > 1250.5:
        break

if actor_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {(1250.5 - actor_points):.1f} more!")