from model import database
from model.item import Livro

def add(livro):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO SaleBook (book_nome, qtd, book_valor) VALUES (?, ?, ?)"""
        cursor.execute(sql, livro.getLivro())
        conn.commit()
    except Exception as r:
        print(r)
    finally:
        conn.close()
    
def remove(id):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM SaleBook WHERE id=?"""
        cursor.execute(sql, [id])
        conn.commit()
    except Exception as o:
        print(o)
    finally:
        conn.close()

def selectHistoric():
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """SELECT MAX(id) FROM SaleBook"""
        cursor.execute(sql)
        result = cursor.fetchall()
    except Exception as u:
        print(u)
    finally:
        conn.close()
    return result

def selectAll():
    lb = []
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM SaleBook ORDER BY id ASC"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for livro in result:
            item = Livro(livro[0], livro[1], livro[2], livro[3])
            lb.append(item)
    except Exception as i:
        print(i)
    finally:
        conn.close()
    return lb