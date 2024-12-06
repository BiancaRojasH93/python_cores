import os
from dotenv import load_dotenv
from dataclasses import dataclass, fields
from datetime import datetime
from typing import ClassVar
from flask_app.config.mysqlconnection import connectToMySQL

load_dotenv()
db_name = os.getenv('DB_NAME')


@dataclass(init=False)
class default_model:

    table_name: ClassVar[str] = None


    id: int
    created_at: datetime
    updated_at: datetime

    def __init__(self, data):
        for field in fields(self):
            if field.type == int and data.get(field.name) == '':
                setattr(self, field.name, None)
            else:
                setattr(self, field.name, data.get(field.name))

    def __dict__(self):
        data = {}
        for field in fields(self):
            data[field.name] = getattr(self, field.name)
        return data

    # Métodos CRUD


    @classmethod
    def all(cls):
        query = f'SELECT * FROM {cls.table_name}'
        results = connectToMySQL(db_name).query_db(query)
        instances = []
        for result in results:
            instances.append(cls(result))
        return instances

    @classmethod
    def find_by_id(cls, data):
        try:
            query = f'SELECT * FROM {cls.table_name} WHERE id = {data}'
            result = connectToMySQL(db_name).query_db(query)
            return cls(result[0])
        except:
            return None

    @classmethod
    def save(cls, data):
        query = f'INSERT INTO {cls.table_name} ({cls.string_fields()}) VALUES ({cls.string_values()})'
        return connectToMySQL(db_name).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = f'UPDATE {cls.table_name} SET {
            cls.string_update()} WHERE id = %(id)s'
        return connectToMySQL(db_name).query_db(query, data)

    @classmethod
    def delete_by_id(cls, id):
        query = f'DELETE FROM {cls.table_name} WHERE id = {id}'
        return connectToMySQL(db_name).query_db(query)

    @classmethod
    def data_fields(cls):
        class_data_fields = []
        for field in fields(cls):
            if (field.name != 'id' and field.name != 'created_at' and field.name != 'updated_at'):
                class_data_fields.append(field.name)
        return class_data_fields

    @classmethod
    def string_fields(cls):
        return ', '.join(cls.data_fields())

    @classmethod
    def string_values(cls):
        return ', '.join([f'%({field})s' for field in cls.data_fields()])

    @classmethod
    def string_update(cls):
        return ', '.join([f'{field} = %({field})s' for field in cls.data_fields()])

    @staticmethod
    def run_query(query, data):
        return connectToMySQL(db_name).query_db(query, data)


# PRUEBAS
if __name__ == '__main__':
    pass