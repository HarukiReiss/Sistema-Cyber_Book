import sqlite3

def connect():
    conn = sqlite3.connect('database/cyber_book.sqlite')
    return conn

