from wtforms import EmailField, Form
from wtforms import StringField, IntegerField, BooleanField, PasswordField, FloatField, RadioField, SelectMultipleField, SubmitField, widgets
from wtforms import validators
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, NumberRange

class UserForm(Form):
    matricula=IntegerField('Matricula', [validators.DataRequired(message='El campo es requerido')])
    nombre=StringField('Nombre', [validators.DataRequired(message='El campo es requerido'), validators.Length(min=1, max=50)])
    apellido=StringField('Apellido', [validators.DataRequired(message='El campo es requerido'), validators.Length(min=1, max=50)])
    email=EmailField('Email', [validators.Email(message='Ingrese un correo válido')])
    
    

class DistanciaForm(Form):
    x1 = FloatField('X1', [validators.DataRequired(message='Campo requerido')])
    x2 = FloatField('X2', [validators.DataRequired(message='Campo requerido')])
    y1 = FloatField('Y1', [validators.DataRequired(message='Campo requerido')])
    y2 = FloatField('Y2', [validators.DataRequired(message='Campo requerido')])
    
    

class PizzeriaForm(Form):
    nombre = StringField('Nombre del Cliente', [validators.DataRequired(message='Campo requerido')])
    direccion = StringField('Dirección', [validators.DataRequired(message='Campo requerido')])
    telefono = StringField('Teléfono', [validators.DataRequired(message='Campo requerido')])

    tamano = RadioField('Tamaño de Pizza', 
                        choices=[('Chica', 'Chica $40'), ('Mediana', 'Mediana $80'), ('Grande', 'Grande $120')],
                        validators=[validators.DataRequired(message='Seleccione un tamaño')])
    
    ingredientes = SelectMultipleField('Ingredientes',
                        choices=[('Jamón', 'Jamón $10'), ('Piña', 'Piña $10'), ('Champiñones', 'Champiñones $10')],
                        option_widget=widgets.CheckboxInput(),
                        widget=widgets.ListWidget(prefix_label=False))
    
    num_pizzas = IntegerField('Número de Pizzas', [validators.DataRequired(message='Campo requerido')])
