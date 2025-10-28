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


@app.route('/distancia', methods=['GET', 'POST'])
def distancia():
    resultado = None
    if request.method == 'POST':
        try:
            x1 = float(request.form.get("X1"))
            x2 = float(request.form.get("X2"))
            y1 = float(request.form.get("Y1"))
            y2 = float(request.form.get("Y2"))

            resultado = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)
        except (ValueError, TypeError):
            resultado = "Error: verifica tus valores."

    return render_template('distancia.html', resultado=resultado)


@app.route('/figuras', methods=['GET', 'POST'])
def figuras():
    area = None
    figura = None

    if request.method == 'POST':
        figura = request.form.get('figura')
        valor1 = request.form.get('valor1', type=float)
        valor2 = request.form.get('valor2', type=float)

        if figura == 'rectangulo' and valor1 and valor2:
            area = valor1 * valor2
        elif figura == 'triangulo' and valor1 and valor2:
            area = (valor1 * valor2) / 2
        elif figura == 'circulo' and valor1:
            area = math.pi * (valor1 ** 2)
        elif figura == 'pentagono' and valor1 and valor2:
            perimetro = 5 * valor1
            area = (perimetro * valor2) / 2

    return render_template('figuras.html', area=area, figura=figura)


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