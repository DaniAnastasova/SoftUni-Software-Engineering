all_Tickets_for_all_film = 0
all_students_ticket = 0
all_kids_ticket = 0
all_standard_ticket = 0

while True:
    film_name = input()
    if film_name == "Finish":
        print(f"Total tickets: {all_Tickets_for_all_film}")

        end_percent_students_ticket = (all_students_ticket / all_Tickets_for_all_film) * 100
        end_percent_standard_ticket = (all_standard_ticket / all_Tickets_for_all_film) * 100
        end_percent_kids_ticket = (all_kids_ticket / all_Tickets_for_all_film) * 100

        print(f"{end_percent_students_ticket:.2f}% student tickets.")
        print(f"{end_percent_standard_ticket:.2f}% standard tickets.")
        print(f"{end_percent_kids_ticket:.2f}% kids tickets.")
        break

    seats_in_salon = int(input())

    all_ticket_count = 0
    while all_ticket_count < seats_in_salon:
        bilet_type = input()

        if bilet_type == "End":
            break

        all_ticket_count += 1
        all_Tickets_for_all_film += 1

        if bilet_type == "student":
            all_students_ticket += 1
        elif bilet_type == "kid":
            all_kids_ticket += 1
        elif bilet_type == "standard":
            all_standard_ticket += 1

    percent = (all_ticket_count / seats_in_salon) * 100
    print(f"{film_name} - {percent:.2f}% full.")