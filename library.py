

library = []

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    year = input("Enter year of publication: ").strip()
    book = {
        "title": title,
        "author": author,
        "year": year,
        "available": True
    }
    library.append(book)
    print("Book added successfully!\n")

def list_books():
    if not library:
        print("No books in the library.\n")
        return
    print("List of Books:")
    for idx, book in enumerate(library, 1):
        status = "Available" if book["available"] else "Borrowed"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {status}")
    print()

def search_books():
    keyword = input("Enter keyword to search by title or author: ").strip().lower()
    results = [book for book in library if keyword in book["title"].lower() or keyword in book["author"].lower()]
    if results:
        print("Search Results:")
        for idx, book in enumerate(results, 1):
            status = "Available" if book["available"] else "Borrowed"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {status}")
    else:
        print("No matching books found.")
    print()

def borrow_book():
    list_books()
    try:
        choice = int(input("Enter the number of the book to borrow: ")) - 1
        if 0 <= choice < len(library):
            if library[choice]["available"]:
                library[choice]["available"] = False
                print(f"You have borrowed '{library[choice]['title']}'.\n")
            else:
                print("Sorry, that book is already borrowed.\n")
        else:
            print("Invalid selection.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def return_book():
    list_books()
    try:
        choice = int(input("Enter the number of the book to return: ")) - 1
        if 0 <= choice < len(library):
            if not library[choice]["available"]:
                library[choice]["available"] = True
                print(f"You have returned '{library[choice]['title']}'.\n")
            else:
                print("That book was not borrowed.\n")
        else:
            print("Invalid selection.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    while True:
        print("=== Library Management CLI ===")
        print("1. Add Book")
        print("2. List All Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            add_book()
        elif choice == '2':
            list_books()
        elif choice == '3':
            search_books()
        elif choice == '4':
            borrow_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.\n")

if __name__ == "__main__":
    main()
