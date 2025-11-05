from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    usuario = "Ana"
    lista_de_tarefas = ["Comprar pão", "Estudar Flask", "Passear com o cachorro"]

    return render_template(
        'index.html', 
        nome=usuario, 
        tarefas=lista_de_tarefas
    )

if __name__ == '__main__':
    app.run(debug=True)