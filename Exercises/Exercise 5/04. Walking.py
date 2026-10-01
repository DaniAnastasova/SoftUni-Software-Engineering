steps = ""
full_steps = 0
steps_to_home = 0

while True:
    steps = input()
    if steps != "Going home":
        steps = int(steps)
        full_steps += steps

    elif steps == "Going home":
        steps_to_home = int(input())
        full_steps += steps_to_home
        if full_steps >= 10000:
            print("Goal reached! Good job!")
            print(f"{full_steps - 10000} steps over the goal!")
            break
        else:
            print(f"{(10000 - full_steps)} more steps to reach goal.")
            break

    if full_steps >= 10000:
        print("Goal reached! Good job!")
        print(f"{full_steps - 10000} steps over the goal!")
        break
