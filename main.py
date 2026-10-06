from flask import Flask, render_template

app_Amizael = Flask(__name__)


@app_Amizael.route("/")
def inicio():
    return render_template("homepage.html")


@app_Amizael.route("/saudacao/<nome>")
def saudacao(nome):
    return f"Olá, {nome}!"


@app_Amizael.route("/homepage")
def homepage():
    return render_template("homepage.html")


@app_Amizael.route("/contato")
def contato():
    return render_template("contato.html")


@app_Amizael.route("/index")
def index():
    return render_template("index.html")


@app_Amizael.route("/usuario")
def usuario():
    return render_template(
        "usuario.html",
        nome="Amizael",
        profissao="Estudante TSI",
        disciplina="Desenvolvimento Web III",
    )


if __name__ == "__main__":
    app_Amizael.run(debug=True)