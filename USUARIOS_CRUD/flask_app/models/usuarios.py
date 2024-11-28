from dataclasses import dataclass
from flask_app.models.default_model import default_model
from typing import ClassVar


@dataclass(init=False)
class Usuario(default_model):

    table_name: ClassVar[str] = 'usuarios'

    nombre: str
    apellido: str
    email: str

    