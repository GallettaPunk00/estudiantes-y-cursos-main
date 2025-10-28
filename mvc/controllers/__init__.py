from flask import blueprints


def register_controllers(app):
    from .cursos_controller import cursos_bp
    from .estudiantes_controller import estudiantes_bp
    app.register_blueprint(cursos_bp)
    app.register_blueprint(estudiantes_bp)
