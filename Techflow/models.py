from database import conectar


class Tarefa:

    @staticmethod
    def listar():

        conn = conectar()

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tarefas")

        tarefas = cursor.fetchall()

        conn.close()

        return tarefas

    @staticmethod
    def adicionar(titulo, descricao, prioridade, status):

        conn = conectar()

        cursor = conn.cursor()

        cursor.execute("""

        INSERT INTO tarefas

        (titulo,descricao,prioridade,status)

        VALUES(?,?,?,?)

        """,

        (titulo, descricao, prioridade, status)

        )

        conn.commit()

        conn.close()

    @staticmethod
    def buscar(id):

        conn = conectar()

        cursor = conn.cursor()

        cursor.execute(

            "SELECT * FROM tarefas WHERE id=?",

            (id,)

        )

        tarefa = cursor.fetchone()

        conn.close()

        return tarefa

    @staticmethod
    def atualizar(id, titulo, descricao, prioridade, status):

        conn = conectar()

        cursor = conn.cursor()

        cursor.execute("""

        UPDATE tarefas

        SET

        titulo=?,

        descricao=?,

        prioridade=?,

        status=?

        WHERE id=?

        """,

        (titulo,

        descricao,

        prioridade,

        status,

        id)

        )

        conn.commit()

        conn.close()

    @staticmethod
    def excluir(id):

        conn = conectar()

        cursor = conn.cursor()

        cursor.execute(

            "DELETE FROM tarefas WHERE id=?",

            (id,)

        )

        conn.commit()

        conn.close()