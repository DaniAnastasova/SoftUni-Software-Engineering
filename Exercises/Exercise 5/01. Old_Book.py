book_name = input()
search_book_name = ""
count_books = 0
found = False

while(search_book_name != "No More Books"):
    search_book_name= input()
    count_books += 1
    if search_book_name == book_name:
        print(f"You checked {count_books-1} books and found it.")
        found = True
        break


if found == False:
    print("The book you search is not here!")
    print(f"You checked {count_books - 1} books.")


