import sqlite3
from model import database
from model.funcionario import Funcionario

def regis(funcionario):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Funcionario (nickname, senha, email) 
                VALUES (?, ?, ?)"""
        cursor.execute(sql, funcionario.getUser())
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def logon(user, key):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Funcionario WHERE nickname= '{}' AND senha= '{}';""".format(user, key)
        cursor.execute(sql)
        result = cursor.fetchone()
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return result
