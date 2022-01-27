import sqlite3
from model import database
from model.funcionario import Funcionario

def reg(funcionario):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Funcionario (nome, senha, email) 
                VALUES (?, ?, ?)"""
        cursor.execute(sql, funcionario.getWorker())
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def log(user, key):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Funcionario WHERE nome= '{}' AND senha= '{}';""".format(user, key)
        cursor.execute(sql)
        result = cursor.fetchone()
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return result

