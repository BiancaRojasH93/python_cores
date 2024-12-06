from datetime import date
import re
from flask import flash
from flask_app import bcrypt

# Función decoradora para crear el mensaje en una categoria especifica si se cumple un condicion
def error_message(if_condition:bool=False, message:str="ERROR: Intentelo de nuevo",message_category:str="error"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if(result == if_condition):
                flash(message,message_category)
            return result
        return wrapper
    return decorator


# Función que devuelve True si el texto dado esta vacio ("") o es nulo (None)
def esta_vacio(texto:str) -> bool:
    esta_vacio = False
    if texto == None or texto == "":
        esta_vacio = True

    return esta_vacio

