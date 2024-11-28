from flask import render_template, request, redirect
from flask_app import app
from flask_app.models import usuarios

@app.route('/')
def index():
    usuarios_list = usuarios.Usuario.all()
    return render_template('index.html', usuarios=usuarios_list)


@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/save', methods=['POST'])
def save():
    usuario_data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email']
    }
    usuarios.Usuario.save(usuario_data)
    return redirect ('/')



@app.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    usuario = usuarios.Usuario.find_by_id(id)
    if usuario is None:
        return redirect('/')
    return render_template('editar.html', usuario=usuario)



@app.route('/editar/<int:id>', methods=['POST'])
def actualizar(id):
    usuario_data = {
        'id': id,
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email']
    }
    usuarios.Usuario.update(usuario_data)
    return redirect('/')

@app.route('/ver/<int:id>', methods=['GET'])
def ver(id):
    usuario = usuarios.Usuario.find_by_id(id)
    
    if usuario is None:
        return redirect('/')
    return render_template('ver.html', usuario=usuario)

@app.route('/borrar/<int:id>', methods=['POST'])
def borrar(id):
    usuario = usuarios.Usuario.find_by_id(id)
    if usuario is None:
        return redirect('/')
    usuarios.Usuario.delete_by_id(id)
    return redirect('/')