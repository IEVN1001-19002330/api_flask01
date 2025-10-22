from flask import Flask, render_template, request
import math

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

@app.route("/resultado", methods=['POST'])
def resultado():
    n1=request.form.get("a")
    n2=request.form.get("b")
    return "La multiplicación de {} y {} es: {} ".format(n1,n2,int(n1)*int(n2))


@app.route('/distancia')
def distancia():
    return render_template('distancia.html')

@app.route('/distancia-result', methods=['POST'])
def result():
    numeroX1= request.form.get("X1")
    numeroX2= request.form.get("X2")
    numeroY1= request.form.get("Y1")
    numeroY2= request.form.get("Y2")
    return "El resultado es: {}".format( math.sqrt(int(numeroX2) - int(numeroX1)* int(numeroX2) - int(numeroX1) + int(numeroY2) - int(numeroY1)* int(numeroY2) - int(numeroY1)))

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