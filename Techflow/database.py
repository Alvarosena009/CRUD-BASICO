import sqlite3

DATABASE = "database/tarefas.db"


def conectar():
    return sqlite3.connect(DATABASE)


def criar_tabela():

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        titulo TEXT NOT NULL,

        descricao TEXT,

        prioridade TEXT,

        status TEXT

    )
    """)

    conn.commit()

    conn.close()