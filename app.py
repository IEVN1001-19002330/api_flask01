from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, world!"


@app.route('/index')
def index():
    titulo="IEVN1001"
    listado=["Python","Flask","HTML","CSS","JavaScript"]
    return render_template('index.html', titulo=titulo, listado=listado)


@app.route('/aporb')
def aporb():
    return render_template('aporb.html')


@app.route('/distancia')
def distancia():
    return render_template('distancia.html')



@app.route("/hola")
def func():
    return "<h1>¡Hola!</h1>"


@app.route("/user/<string:user>")
def user(user):
    return "<h1>¡Hola, {}!</h1>".format(user)


@app.route("/square/<int:num>")
def square(num):
    return "<h1> The square of {} is {} </h1>".format(num, num**2)

@app.route("/repeat/<string:text>/<int:times>")
def repeat(text, times):
    return f"<h1>" + " ".join([text] * times) + "</h1>"

@app.route('/suma/<float:a>/<float:b>')
def suma(a, b):
    return "<h1> The sum of {} and {} is {}. </h1>".format(a, b, a + b)


@app.route("/prueba")
def func12():
    return """"
    <h1> Prueba de HTML </h1>
    <p> Esto es una pagina web </p>
    """




if __name__ == '__main__':
    app.run(debug=True)