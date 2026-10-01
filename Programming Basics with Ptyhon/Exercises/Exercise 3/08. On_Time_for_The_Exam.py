exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minute
arrival_time_in_minutes = arrival_hour * 60 + arrival_minute

time_diff = arrival_time_in_minutes - exam_time_in_minutes

if time_diff > 0:
    print("Late")
elif time_diff >= -30:
    print("On time")
else:
    print("Early")


if time_diff != 0:
    abs_diff = abs(time_diff)
    hours = abs_diff // 60
    minutes = abs_diff % 60


    if time_diff > 0:
        if hours > 0:
            print(f"{hours}:{minutes:02d} hours after the start")
        else:
            print(f"{minutes} minutes after the start")


    else:
        if hours > 0:
            print(f"{hours}:{minutes:02d} hours before the start")
        else:
            print(f"{minutes} minutes before the start")



