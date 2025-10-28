import os
import pymysql
from pymysql.cursors import DictCursor

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASS", "admin"),
    "db": os.getenv("DB_NAME", "esquema_estudiantes_cursos"),
    "charset": "utf8mb4",
    "cursorclass": DictCursor,
}


class MySQLConnection:
    def __init__(self, db_config=None):
        self.db = db_config or DB_CONFIG

    def query_db(self, query, data=None):
        connection = None
        try:
            connection = pymysql.connect(**self.db)
            with connection.cursor() as cursor:
                cursor.execute(query, data or {})
                if query.strip().lower().startswith("select"):
                    result = cursor.fetchall()
                else:
                    connection.commit()
                    result = {"lastrowid": cursor.lastrowid}
            return result
        finally:
            if connection:
                connection.close()


def connectToMySQL(db=None):
    cfg = DB_CONFIG.copy()
    if db:
        cfg["db"] = db
    return MySQLConnection(cfg)