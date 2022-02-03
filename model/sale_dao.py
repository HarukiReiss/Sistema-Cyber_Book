from model import database

def add(sale):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Sale (cliente, funcionario, valor) VALUES (?, ?, ?)"""
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