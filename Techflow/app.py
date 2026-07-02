from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

from database import criar_tabela
from models import Tarefa

app = Flask(__name__)

criar_tabela()


@app.route("/")
def index():

    tarefas = Tarefa.listar()

    return render_template(

        "index.html",

        tarefas=tarefas

    )


@app.route("/nova")

def nova():

    return render_template(

        "cadastrar.html"

    )


@app.route("/salvar", methods=["POST"])

def salvar():

    titulo = request.form["titulo"]

    descricao = request.form["descricao"]

    prioridade = request.form["prioridade"]

    status = request.form["status"]

    Tarefa.adicionar(

        titulo,

        descricao,

        prioridade,

        status

    )

    return redirect(url_for("index"))


@app.route("/editar/<int:id>")

def editar(id):

    tarefa = Tarefa.buscar(id)

    return render_template(

        "editar.html",

        tarefa=tarefa

    )


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


if __name__ == "__main__":

    app.run(debug=True)