from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import jsonify

from database import criar_tabela
from models import Tarefa

app = Flask(__name__)

criar_tabela()


@app.route("/")
def index():
    tarefas = Tarefa.listar()
    stats = Tarefa.obter_estatisticas()
    return render_template("index.html", tarefas=tarefas, stats=stats)


@app.route("/nova")
def nova():
    return render_template("cadastrar.html")


@app.route("/salvar", methods=["POST"])
def salvar():
    titulo = request.form["titulo"]
    descricao = request.form["descricao"]
    prioridade = request.form["prioridade"]
    status = request.form["status"]
    
    Tarefa.adicionar(titulo, descricao, prioridade, status)
    return redirect(url_for("index"))


@app.route("/editar/<int:id>")
def editar(id):
    tarefa = Tarefa.buscar(id)
    return render_template("editar.html", tarefa=tarefa)


@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar(id):
    Tarefa.atualizar(
        id,
        request.form["titulo"],
        request.form["descricao"],
        request.form["prioridade"],
        request.form["status"]
    )
    return redirect(url_for("index"))


@app.route("/excluir/<int:id>")
def excluir(id):
    Tarefa.excluir(id)
    return redirect(url_for("index"))


@app.route("/status/<int:id>/<novo_status>", methods=["POST"])
def mudar_status(id, novo_status):
    Tarefa.mudar_status(id, novo_status)
    return redirect(url_for("index"))


@app.route("/filtro/<status_filtro>")
def filtro_status(status_filtro):
    tarefas = Tarefa.listar_por_status(status_filtro)
    stats = Tarefa.obter_estatisticas()
    return render_template("index.html", tarefas=tarefas, stats=stats, filtro_ativo=status_filtro)


@app.route("/api/stats")
def api_stats():
    stats = Tarefa.obter_estatisticas()
    return jsonify(stats)


if __name__ == "__main__":
    app.run(debug=True)