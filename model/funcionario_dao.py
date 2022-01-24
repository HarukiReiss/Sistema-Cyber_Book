import sqlite3
from model import database
from model.funcionario import Funcionario

def cad(funcionario):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Funcionario (nome, senha, email)
                VALUES (?, ?, ?)"""
        cursor.execute(sql, funcionario.getUser())
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def login(nome, senha):
    try:
        conn = database.connect()
        cursor = conn.cursor
        sql = """SELECT FROM Funcionario WHERE nome=?, senha=?"""
        cursor.execute(sql, nome, senha)
        result = cursor.fetchall()
    except Exception as e:
        print (e)
    finally:
        conn.close()
