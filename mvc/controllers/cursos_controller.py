from flask import render_template, request, redirect, url_for
from mvc.config.mysqlconnection import connectToMySQL
from mvc.models.curso import Curso

from flask import Blueprint
cursos_bp = Blueprint('cursos', __name__)

@cursos_bp.route('/')
def index_root():
    return redirect(url_for('cursos.listar_cursos'))

@cursos_bp.route('/cursos')
def listar_cursos():
    cursos = Curso.get_all()
    return render_template('cursos.html', cursos=cursos)

@cursos_bp.route('/cursos/create', methods=['POST'])
def crear_curso():
    nombre = request.form.get('nombre', '').strip()
    if nombre:
        Curso.create({'nombre': nombre})
    return redirect(url_for('cursos.listar_cursos'))

@cursos_bp.route('/cursos/<int:curso_id>')
def mostrar_curso(curso_id):
    curso = Curso.get_with_students(curso_id)
    if not curso:
        return redirect(url_for('cursos.listar_cursos'))
    return render_template('mostrar_curso.html', curso=curso)