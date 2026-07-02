from database import conectar


class Tarefa:

    @staticmethod
    def listar():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefas ORDER BY id DESC")
        tarefas = cursor.fetchall()
        conn.close()
        return tarefas

    @staticmethod
    def adicionar(titulo, descricao, prioridade, status):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tarefas (titulo, descricao, prioridade, status) VALUES(?, ?, ?, ?)",
            (titulo, descricao, prioridade, status)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def buscar(id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefas WHERE id=?", (id,))
        tarefa = cursor.fetchone()
        conn.close()
        return tarefa

    @staticmethod
    def atualizar(id, titulo, descricao, prioridade, status):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tarefas SET titulo=?, descricao=?, prioridade=?, status=? WHERE id=?",
            (titulo, descricao, prioridade, status, id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def excluir(id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tarefas WHERE id=?", (id,))
        conn.commit()
        conn.close()

    @staticmethod
    def mudar_status(id, novo_status):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE tarefas SET status=? WHERE id=?", (novo_status, id))
        conn.commit()
        conn.close()

    @staticmethod
    def listar_por_status(status):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefas WHERE status=? ORDER BY id DESC", (status,))
        tarefas = cursor.fetchall()
        conn.close()
        return tarefas

    @staticmethod
    def obter_estatisticas():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM tarefas")
        total = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM tarefas WHERE status='Pendente'")
        pendentes = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM tarefas WHERE status='Em andamento'")
        andamento = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM tarefas WHERE status='Concluída'")
        concluidas = cursor.fetchone()[0]
        conn.close()
        return {
            'total': total,
            'pendentes': pendentes,
            'andamento': andamento,
            'concluidas': concluidas
        }