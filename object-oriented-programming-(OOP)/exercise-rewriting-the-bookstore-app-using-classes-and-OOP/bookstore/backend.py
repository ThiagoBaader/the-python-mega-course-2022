# library import
import sqlite3

class Database:

    # connect to a database
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()


    # create the function to insert data
    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit()


    # create the view function
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    # create the search function
    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book where title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    # create the delete function
    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()


    # create the update function
    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()


    # close the database
    def __del__(self):
        self.conn.close()

#insert("The Sun", "John Smith", 1918, 913123132)
#delete(5)
#update(2, "The Moon", "John Smooth", 1917, 923223132)
#print(view())
#print(search(author="John Smooth"))
