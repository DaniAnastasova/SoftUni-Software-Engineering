import math

w = 2000
f = 1200
sf = 720

count_tournaments = int(input())
start_points = int(input())
tournaments_status = ""
final_points = start_points
count_win_tournaments = 0

for i in range(count_tournaments):
    tournaments_status = input()
    if tournaments_status == "W":
         final_points += w
         count_win_tournaments += 1
    elif tournaments_status == "F":
        final_points += f
    elif tournaments_status == "SF":
        final_points += sf

average_points = (final_points - start_points) / count_tournaments
average_points = int(math.floor(average_points))
print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{((count_win_tournaments / count_tournaments) * 100):.2f}%")
