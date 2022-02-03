from model import database
from model.book import Book

def addBook(book):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Book (nome, qt, valor) VALUES (?,?,?,?)"""
        cursor.execute(sql, book.getBook())
        conn.commit()
    except Exception as i:
        print(i)
    finally:
        conn.close()

def removeBook(id):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM Book WHERE id=?"""
        cursor.execute(sql, [id])
        conn.commit()
    except Exception as q:
        print(q)
    finally:
        conn.close()
        
def editBook(book):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """UPDATE Book SET nome=?, qt=?, valor=? WHERE id=?"""
        cursor.execute(sql, book.id)
        conn.commit()
    except Exception as a:
        print(a)
    finally:
        conn.close()
    
def selectAll():
    lb = []
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Book ORDER BY id ASC"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for note in result:
            new = Book(note[0], note[1], note[2], note[3], note[4])
            lb.append(new)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return lb