import sqlite3

# Creating Cursor
db = sqlite3.connect('ebookstore.db')
cursor = db.cursor()

# Creating Table
cursor.execute('DROP TABLE IF EXISTS ebookstore')
cursor.execute('''
    CREATE TABLE ebookstore(id INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)
    ''')
db.commit()

# The defaulting books

id1 = 3001
title1 = "A Tale of Two Cities"
author1 = "Charles Dickens"
qty1 = 30

id2 = 3002
title2 = "Harry Potter and the Philosopher's Stone"
author2 = "J.K. Rowling"
qty2 = 40

id3 = 3003
title3 = "The Lion, the Witch and the Wardrobe"
author3 = "C.S. Lewis"
qty3 = 25

id4 = 3004
title4 = "The Lord of the Rings"
author4 = "J.R.R Tolkien"
qty4 = 37

id5 = 3005
title5 = "Alice in Wonderland"
author5 = "Lewis Carroll"
qty5 = 12

default_books = [(id1, title1, author1, qty1), (id2, title2, author2, qty2), (id3, title3, author3, qty3),
                 (id4, title4, author4, qty4), (id5, title5, author5, qty5)]

cursor.executemany(''' INSERT INTO ebookstore(id, title, author, qty)
               VALUES(?,?,?,?)''', default_books)

db.commit()


# Creating Functions
def add():
    new_id = int(input("Please enter book id:   "))
    new_title = input("Please enter book title:  ")
    new_author = input("Please enter book author:   ")
    new_qty = int(input("Please enter book quantity:   "))

    new_book = [(new_id, new_title, new_author, new_qty)]
    cursor.execute(''' INSERT INTO ebookstore(id, title, author, qty)
                   VALUES(?,?,?,?)''', new_book)


def update():
    book_id = input("Please input the book's Id:   ")
    update_menu = int(input("Would you like to update \n"
                            "1. Book Id \n"
                            "2. Book Title \n"
                            "3. Book Author \n"
                            "4. Book Quantity \n"
                            "   :"))
    if update_menu == 1:
        renew = int(input("Provide new ID:  "))
        cursor.execute('UPDATE ebookstore SET id = renew WHERE id =?', (book_id,))

    elif update_menu == 2:
        renew = input("Provide new Title:  ")
        cursor.execute('UPDATE ebookstore SET title = renew WHERE id =?', (book_id,))

    elif update_menu == 3:
        renew = input("Provide new Author:  ")
        cursor.execute('UPDATE ebookstore SET author = renew WHERE id =?', (book_id,))

    elif update_menu == 4:
        renew = input("Provide new Quantity:  ")
        cursor.execute('UPDATE ebookstore SET qty = renew WHERE id =?', (book_id,))

    else:
        print("Input does not exist")


def delete():
    book_id = input("Please enter book Id:   ")
    cursor.execute('DELETE FROM ebookstore WHERE id =?', (book_id,))


def search():
    book_search = int(input("1. Search book id \n"
                            "2. Search book title \n"
                            "3. Search book author \n"
                            "   :  "))

    if book_search == 1:
        book_id = input("Please enter book Id:   ")
        cursor.execute('SELECT * FROM ebookstore WHERE id =?', (book_id,))
        book = cursor.fetchall()
        print(book)

    elif book_search == 2:
        book_title = input("Please enter book title:  ")
        cursor.execute('SELECT * FROM ebookstore WHERE title =?', (book_title,))
        book = cursor.fetchall()
        print(book)

    elif book_search == 3:
        book_author = input("Please enter book author:  4")
        cursor.execute('SELECT * FROM ebookstore WHERE author =?', (book_author,))
        book = cursor.fetchall()
        print(book)


    else:
        print("There was an error in your input")


# Creating a menu
while True:
    menu = int(input("Select the following options \n"
                     "1. Enter book \n"
                     "2. Update book \n"
                     "3. Delete book \n"
                     "4. Search books \n"
                     "0. Exit \n"
                     "   :  "))

    if menu == 1:
        add()

    elif menu == 2:
        update()

    elif menu == 3:
        delete()

    elif menu == 4:
        search()

    elif menu == 0:
        print('Goodbye!!!')
        break

    else:
        print("You have made a wrong choice, Please Try again")
