from flask import redirect, render_template, request, session
from flask_app import app
from flask_app.models import estudiantes, cursos


@app.route('/', methods=['POST', 'GET'])
def index():
    curso = cursos.Curso.all()
    return render_template('cursos.html', cursos=curso)


@app.route('/nuevo_curso', methods=['POST'])
def nuevo_curso():
    curso_data = {
        'nombre': request.form['nombre']
    }
    cursos.Curso.save(curso_data)
    return redirect('/')

@app.route('/estudiante')
def estudiante():
    curso = cursos.Curso.all()
    return render_template('estudiante.html', cursos=curso)


@app.route('/nuevo_estudiante', methods=['POST'])
def nuevo_estudiante():
    estudiante_data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'edad': request.form['edad'],
        'curso_id': request.form['curso_id']
    }
    estudiantes.Estudiante.save(estudiante_data)
    return redirect ('/')


@app.route('/cursos/<int:id>', methods=['GET'])
def mostrar_curso(id):
    cursos_lista = cursos.Curso.find_by_id(id)
    estudiantes_list = estudiantes.Estudiante.show(id)
    return render_template('mostrar_curso.html', estudiantes=estudiantes_list, curso=cursos_lista)
