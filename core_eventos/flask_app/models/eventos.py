from dataclasses import InitVar, dataclass
from typing import ClassVar
from datetime import date, datetime
from flask import flash
from flask_app.models import usuarios
from flask_app.models.default_model import default_model
from flask_app import app

@dataclass (init=False)
class Evento(default_model):

    table_name: ClassVar[str] = 'eventos'

    nombre : str
    ubicacion : str
    fecha : date
    detalles: str
    usuario_id : int

        ## CAMPOS VIRTUALES ##
    autor: InitVar["usuarios.Usuario"]

    ## CONSTRUCTOR ##

    def __init__(self, data):
        super().__init__(data)
        if data.get('usuario_id'):
            self.get_autor()
            

    def get_autor(self):

        autor = usuarios.Usuario.find_by_id(self.usuario_id)
        self.autor = autor
        return self



    @staticmethod
    def validate(data):
        is_valid = True

        # Validación de 'nombre'
        if data.get('nombre') is None or len(data.get('nombre')) < 3:
            is_valid = False
            flash('El nombre debe tener al menos 3 caracteres', 'nombre')

        # Validación de 'ubicacion'
        if data.get('ubicacion') is None or len(data.get('ubicacion')) < 3:
            is_valid = False
            flash('La ubicacion debe tener al menos 3 caracteres', 'ubicacion')

        # Validación de 'detalles'
        if data.get('detalles') is None or len(data.get('detalles')) < 3:
            is_valid = False
            flash('El detalle debe tener al menos 3 caracteres', 'detalles')

        # Validación de 'fecha'
        fecha_str = data.get('fecha')
        if not fecha_str:  # Verifica si la fecha está vacía o es None
            is_valid = False
            flash('Debes poner una fecha', 'fecha')
        else:
            try:
                # Convierte la fecha de cadena a tipo 'date'
                fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
                data['fecha'] = fecha  # Reemplaza el valor de 'fecha' en los datos procesados
            except ValueError:
                is_valid = False
                flash('El formato de la fecha es incorrecto', 'fecha')

        return is_valid
    
    