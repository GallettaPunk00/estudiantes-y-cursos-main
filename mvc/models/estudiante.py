from mvc.config.mysqlconnection import connectToMySQL

DB = "esquema_estudiantes_cursos"

class Estudiante:
    @staticmethod
    def create(data):
        mysql = connectToMySQL(DB)
        query = """INSERT INTO estudiantes (nombre, apellido, edad, curso_id)
                    VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(curso_id)s);"""
        return mysql.query_db(query, data)