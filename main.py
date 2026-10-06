from flask import Flask

app_Amizael = Flask(__name__)


@app_Amizael.route("/")
def inicio():
    return "Olá, Turma!"


@app_Amizael.route("/saudacao/<nome>")
def saudacao(nome):
    return f"Olá, {nome}!"


if __name__ == "__main__":
    app_Amizael.run(debug=True)