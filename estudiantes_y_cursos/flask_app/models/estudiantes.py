from dataclasses import dataclass
from flask_app.models.default_model import default_model
from typing import ClassVar
from flask_app.config.mysqlconnection import connectToMySQL
import os

db_name = os.getenv('DB_NAME')

@dataclass(init=False)
class Estudiante(default_model):
    table_name: ClassVar[str] = 'estudiantes'

    nombre: str
    apellido: str
    edad: int
    curso_id: int

    @classmethod
    def show(cls, curso_id):
        # Query para obtener los estudiantes de un curso
        query = f'SELECT * FROM {cls.table_name} WHERE curso_id = {curso_id}'
        results = connectToMySQL(db_name).query_db(query)
        # Crear una lista de instancias de Estudiante
        instances = []
        for result in results:
            instances.append(cls(result))  # Usar el constructor heredado de default_model
        return instances