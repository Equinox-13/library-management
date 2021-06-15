# -*- coding: utf-8 -*-

"""
Library Management System
~~~~~~~~~~~~~~~~~~~~~~~~~

Menu driven program that helps to perform
basic operations for library management.
"""

class Library:
    def __init__(self, list_of_books):
        # List of books initialized
        self.books = list_of_books

    def display_books(self):
        """
        Displays list of books available in the library
        """
        print("---------------------------------------")
        print("We have following books in our Library:")
        for book in self.books:
            print(book[0])

    def add_book(self, book_info):
        """
        Adds a book record to the list

        :param book_info : list consisting of book info

        """
        self.books.append(book_info)
        print("\nBook has been added to your list")

    def delete_book(self, book):
        """
        Deletes the book record from the list

        :param book : Name of the book to be deleted

        """
        for each in list(self.books):
            if each[0] == book:
                self.books.remove(each)
                print("\nBook is Deleted.")

    def view_book_info(self, book):
        """
        Display more information about the book

        :param book : Name of the book to get the info about

        """
        for each in self.books:
            if each[0] == book:
                print(f"\nBook Name: {each[0]}\nAuthor: {each[1]}")


class Student:
    def __init__(self):
        # dict to manage lending records
        self.lend_dict = {}

    def request_book(self, user, book):
        """
        Check book if it can be lended

        :param user: Name of the user that requests the book
        :param book: Name of the book that needs to be lended

        """
        if book not in self.lend_dict.keys():
            self.lend_dict.update({book:user})
            print("\nThe book you have requested can be borrowed.")
        else:
            print(f"\nbook is already allocated to {self.lend_dict[book]}.")

    def return_book(self, book):
        """
        Remove the book from the lend_dict

        :param book: Name of the book that needs to be returned

        """
        if book in self.lend_dict.keys():
            self.lend_dict.pop(book)
            print(f"\nBook is returned.")
        else:
            print("\nBook is not lended to anyone yet.")


if __name__ == '__main__':
    library = Library([["Python", "Guido Van Rossum"],
        ["Java", "James Gosling"],
        ["Go", "Robert Griesemer"]])

    student = Student()

    while(True):
        print("=======================xxxxxxx=====================")
        print("--Welcome to the library--")
        print("1. Display books")
        print("2. Request a book")
        print("3. Return a book")
        print("4. Add a Book")
        print("5. Delete a Book")
        print("6. View information for any book")
        print("7. Exit")
        print("=======================xxxxxxx=====================")
        print("Enter your choice to continue:")
        user_choice = int(input())

        if user_choice == 1:
            library.display_books()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: ").strip().lower()
            user = input("Enter your name: ").strip().lower()
            student.request_book(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to return: ")
            student.return_book(book)

        elif user_choice == 4:
            book_info = []
            book = input("Enter the name of the book: ").strip()
            author = input("Enter the author of the book: ").strip().strip().lower()
            book_info.extend([book, author])
            library.add_book(book_info)

        elif user_choice == 5:
            book = input("Enter the name of the book you want to delete: ").strip().title()
            library.delete_book(book)

        elif user_choice == 6:
            book = input("Enter the name of the book you want to check inforamtion about: ").strip().title()
            library.view_book_info(book)

        elif user_choice == 7:
            exit()

        else:
            print("Not a valid option")

        print("\nPress q to quit and c to continue")

        user_choice2 = ""
        while(user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            if user_choice2 == "c":
                continue
