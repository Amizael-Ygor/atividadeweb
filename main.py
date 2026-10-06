from flask import Flask

app_Amizael = Flask(__name__)


@app_Amizael.route("/")
def inicio():
    return "Olá, Turma!"


if __name__ == "__main__":
    app_Amizael.run(debug=True)