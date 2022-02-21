from model import database
from model.sale import Sale

def add(sale):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Sale (cliente, funcionario, valor, data) VALUES (?, ?, ?, ?)"""
        cursor.execute(sql, sale.getSale())
        conn.commit()
    except Exception as p:
        print(p)
    finally:
        conn.close()
    
def selectHistoric():
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """SELECT MAX(id) FROM Sale"""
        cursor.execute(sql)
        result = cursor.fetchone()
    except Exception as g:
        print(g)
    finally:
        conn.close()
    return result

def selectAll():
    list = []
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Sale ORDER BY id DESC"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for s in result:
            new = Sale(s[0], s[1], s[2], s[3], s[4])
            list.append(new)
    except Exception as l:
        print(l)
    finally:
        conn.close()
    return list