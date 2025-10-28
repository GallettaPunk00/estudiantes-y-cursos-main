from mvc.config.mysqlconnection import connectToMySQL

DB = "esquema_estudiantes_cursos"

class Curso:
    @staticmethod
    def get_all():
        mysql = connectToMySQL(DB)
        query = "SELECT id, nombre, created_at FROM cursos ORDER BY id DESC;"
        return mysql.query_db(query)

    @staticmethod
    def create(data):
        mysql = connectToMySQL(DB)
        query = "INSERT INTO cursos (nombre) VALUES (%(nombre)s);"
        return mysql.query_db(query, data)

    @staticmethod
    def get_with_students(curso_id):
        mysql = connectToMySQL(DB)
        query = """
        SELECT c.id AS curso_id, c.nombre AS curso_nombre, 
        s.id AS estudiante_id, s.nombre AS estudiante_nombre, s.apellido, s.edad
        FROM cursos c
        LEFT JOIN estudiantes s ON s.curso_id = c.id
        WHERE c.id = %(id)s;
        """
        rows = mysql.query_db(query, {"id": curso_id})
        if not rows:
            return None
        curso = {"id": rows[0]["curso_id"], "nombre": rows[0]["curso_nombre"], "estudiantes": []}
        for r in rows:
            if r.get("estudiante_id"):
                curso["estudiantes"].append({
                    "id": r["estudiante_id"],
                    "nombre": r["estudiante_nombre"],
                    "apellido": r["apellido"],
                    "edad": r["edad"],
                })
        return curso