from flask import Flask, render_template, request, redirect
from flask import make_response, jsonify
import json
from forms import PizzeriaForm
import math
from datetime import datetime 
import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta'

@app.route('/')
def home():
    return "Hello, world!"

@app.route("/pizzeria", methods=["GET", "POST"])
def pizzeria():
    form = PizzeriaForm(request.form)
    pedidos = []
    ventas = []
    total_dia = 0

    data_pedidos = request.cookies.get("pedidos")
    if data_pedidos:
        pedidos = json.loads(data_pedidos)
    data_ventas = request.cookies.get("ventas")
    if data_ventas:
        ventas = json.loads(data_ventas)

    if request.method == "POST" and form.validate():
        accion = request.form.get("btnAccion")

        if accion == "agregar":
            tamano = form.tamano.data
            ingredientes = form.ingredientes.data
            num_pizzas = form.num_pizzas.data

            precios = {"Chica": 40, "Mediana": 80, "Grande": 120}
            subtotal = precios[tamano] * num_pizzas + (10 * len(ingredientes) * num_pizzas)

            nuevo_pedido = {
                "tamano": tamano,
                "ingredientes": ", ".join(ingredientes),
                "num_pizzas": num_pizzas,
                "subtotal": subtotal
            }
            pedidos.append(nuevo_pedido)

        elif accion == "quitar":
            if pedidos:
                pedidos.pop() 

        elif accion == "terminar":
            if pedidos:
                total = sum(p["subtotal"] for p in pedidos)
                nombre = form.nombre.data
                direccion = form.direccion.data
                telefono = form.telefono.data
                fecha = datetime.now().strftime("%d-%m-%Y")

                nueva_venta = {
                    "nombre": nombre,
                    "direccion": direccion,
                    "telefono": telefono,
                    "fecha": fecha,
                    "total": total
                }
                ventas.append(nueva_venta)

                pedidos = [] 

        total_dia = sum(v["total"] for v in ventas)

        response = make_response(render_template("pizzeria.html", form=form, pedidos=pedidos, ventas=ventas, total_dia=total_dia))
        response.set_cookie("pedidos", json.dumps(pedidos))
        response.set_cookie("ventas", json.dumps(ventas))
        return response

    total_dia = sum(v["total"] for v in ventas)
    return render_template("pizzeria.html", form=form, pedidos=pedidos, ventas=ventas, total_dia=total_dia)


@app.route("/get_ventas")
def get_ventas():
    data_ventas = request.cookies.get("ventas")
    if not data_ventas:
        return "No hay ventas registradas", 404
    ventas = json.loads(data_ventas)
    return jsonify(ventas)


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


""" @app.route('/distancia01', methods=['GET', 'POST'])
def distancia1():
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

    return render_template('distancia.html', resultado=resultado) """


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


@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    mat=0
    nom=''
    apell=''
    email=''
    estudiantes=[]
    datos={}
    
    alumno_class=forms.UserForm(request.form)
    if request.method=='POST' and alumno_class.validate():
        
        if request.form.get("btnElimina")=='eliminar':
            response = make_response(render_template('Alumnos.html',))
            response.delete_cookie('usuario')
            
        
        mat=alumno_class.matricula.data
        nom=alumno_class.nombre.data
        apell=alumno_class.apellido.data
        email=alumno_class.email.data
        datos={'matricula':mat,'nombre':nom.rstrip(), 'apellido':apell.rstrip(),'email':email.rstrip()}
        
        data_str = request.cookies.get("usuario")
        if not data_str:
            return "No hay cookies guardadas", 404
        
        estudiantes= json.loads(data_str)
        
        estudiantes.append(datos)
        
    response=make_response(render_template('Alumnos.html',form=alumno_class, mat=mat, nom=nom, apell=apell, email=email))
        
    if request.method!='GET':
        response.set_cookie('usuario', json.dumps(estudiantes))
            
    return response
    
@app.route("/get_cookie")
def get_cookie():
    
    data_str = request.cookies.get("usuario")
    if not data_str:
        return "No hay cookie guardada", 404
    
    estudiantes = json.loads(data_str)
    
    return jsonify(estudiantes)
    
@app.route("/distancia", methods=['GET', 'POST'])
def distancia():
    resultado = None
    form = forms.DistanciaForm(request.form)

    if request.method == 'POST' and form.validate():
        x1 = form.x1.data
        x2 = form.x2.data
        y1 = form.y1.data
        y2 = form.y2.data
        
        resultado = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    return render_template('distancia.html', form=form, resultado=resultado)


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