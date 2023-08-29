from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, NumberRange

class RegistrarProductoForm(FlaskForm):
    nombre = StringField("Nombre del producto:", validators = [InputRequired(message = "Nombre de Producto Requerido")])
    precio = IntegerField("Precio del producto:", validators = [InputRequired(message = "Precio Requerido"),
                                                                NumberRange (message = "Precio Fuera de rango",
                                                                min = 10,
                                                                max = 100000)])
    imagen = FileField("Selecione imagen del producto", validators= [FileRequired(message= "Debe seleccionar una imagen"),
                                                                     FileAllowed(['jpg', 'png'], "Solo se permiten imagenes")])
    submit = SubmitField("Guardar")