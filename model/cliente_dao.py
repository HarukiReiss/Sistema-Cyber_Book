import sqlite3
from model import database
from model.cliente import Cliente

list = []
def add(cliente):
    list.append(cliente)
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Cliente (nome, telefone, endereco, cpf) VALUES (?, ?, ?, ?)"""
        cursor.execute(sql, cliente.getCostumer())
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def edit(cliente):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """UPDATE Cliente SET nome=?, telefone=?, endereco=?, cpf=? WHERE id=?"""
        l = cliente.getCostumer()
        l.append(cliente.id)
        cursor.execute(sql, l)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def delete(id):
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
    lis = []
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Cliente ORDER BY id ASC"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for cliente in result:
            new = Cliente(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4])
            lis.append(new)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return lis