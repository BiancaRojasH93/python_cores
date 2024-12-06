from dataclasses import dataclass
import re
from typing import ClassVar
from flask import flash
from flask_app.models.default_model import default_model
from flask_bcrypt import Bcrypt
from flask_app import app

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@dataclass(init=False)

class Usuario(default_model):

    table_name: ClassVar[str] = "usuarios"

    nombre: str
    apellido: str
    email: str
    contraseña: str

    

    @staticmethod
    def validate(data):
        is_valid = True

        if( data.get('nombre') == None or len(data.get('nombre')) < 2):
            is_valid = False
            flash('El nombre debe tener al menos 2 caracteres', 'nombre')
        if( data.get('apellido') == None or len(data.get('apellido')) < 2):
            is_valid = False
            flash('El apellido debe tener al menos 2 caracteres', 'apellido')
        if(data.get('email') == None or not EMAIL_REGEX.match(data.get('email'))):
            is_valid = False
            flash('El email no es valido', 'email')
        else:
            query = f"SELECT * FROM {Usuario.table_name} WHERE email = %(email)s"
            result = Usuario.run_query(query, data)
            
            # Asegúrate de que result es una lista
            if not isinstance(result, list):
                result = []

            if len(result) > 0:
                is_valid = False
                flash('El Email ya está registrado', 'email')
        
        if (data.get('contraseña') == None or len(data.get('contraseña')) < 8):
            is_valid = False
            flash('La contraseña debe tener al menos 8 caracteres', 'contraseña')
        elif (data.get('confirmar_contraseña') == None or data.get('contraseña') != data.get('confirmar_contraseña')):
            is_valid = False
            flash('Las contraseñas no coinciden', 'confirmar_contraseña')

        return is_valid

    @staticmethod
    def validate_login(data):
        
        query = f"SELECT * FROM {Usuario.table_name} WHERE email = %(email)s"
        result = Usuario.run_query(query, data)
        if len(result) > 0:
            if bcrypt.check_password_hash(result[0]['contraseña'], data['contraseña']):
                return result[0]['id']
            
        return False
    
