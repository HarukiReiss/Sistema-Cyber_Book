import sqlite3
from model import database
from model.cliente import Cliente

lc = []

def add(cliente):
    lc.append(cliente)
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Cliente (nome, tel, endereco, cpf) VALUES (?, ?, ?, ?)"""
        cursor.execute(sql, cliente.getData())
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def edit(cliente):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """UPDATE Cliente SET nome=?, tel=?, endereco=?, cpf=? WHERE id=?"""
        l = cliente.getData()
        l.append(cliente.id)
        cursor.execute(sql, l)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def remove(id):
    try:
        conn = database.connect()
        cursor = conn.cursor() 
        sql = """DELETE FROM Cliente WHERE id=?"""
        cursor.execute(sql, [id])
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def selectAll():
    li = []
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Cliente ORDER BY id ASC"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for cliente in result:
            new = Cliente(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4])
            li.append(new)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return li