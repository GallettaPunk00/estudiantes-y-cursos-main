from flask import render_template, request, redirect, url_for, Blueprint
from mvc.models.curso import Curso
from mvc.models.estudiante import Estudiante

estudiantes_bp = Blueprint('estudiantes', __name__)

@estudiantes_bp.route('/estudiante')
def nuevo_estudiante():
    cursos = Curso.get_all()
    return render_template('nuevo_estudiante.html', cursos=cursos)

@estudiantes_bp.route('/estudiante/create', methods=['POST'])
def crear_estudiante():
    data = {
        'nombre': request.form.get('nombre', '').strip(),
        'apellido': request.form.get('apellido', '').strip(),
        'edad': request.form.get('edad') or None,
        'curso_id': request.form.get('curso_id')
    }
    if data['nombre'] and data['apellido'] and data['curso_id']:
        Estudiante.create(data)
    return redirect(url_for('estudiantes.nuevo_estudiante'))