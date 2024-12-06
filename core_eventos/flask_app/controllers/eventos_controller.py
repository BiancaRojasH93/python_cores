from flask import redirect, render_template, request, session
from flask_app.models import eventos
from flask_app import app
from flask import flash
from flask_app.utils.auth import session_required

## RUTA PARA CREAR UN VIAJE ##

@app.route('/nuevo')
@session_required('/')
def nuevo_evento():
    evento = eventos.Evento
    return render_template('crear.html', eventos=evento)

@app.route('/crear', methods=['POST', 'GET'])
@session_required("/")
def crear_evento():
    data = {
        'nombre': request.form['nombre'],
        'ubicacion': request.form['ubicacion'],
        'fecha': request.form['fecha'],  # Asegúrate de que el formato sea correcto
        'detalles': request.form['detalles'] or "detalles no disponibles",
        'usuario_id': session['usuario_id']
    }
    # Validación
    if not eventos.Evento.validate(data):
        return redirect('/nuevo')  # Si la validación falla, redirige al formulario para corregir los errores
    eventos.Evento.save(data)  # Si la validación pasa, guarda el evento
    return redirect('/dashboard')


## RUTA PARA ACCEDER A LA PAGINA DE EDICION ##

@app.route('/editar/<int:id>', methods=['GET'])
@session_required("/")
def edit_evento(id):
    evento = eventos.Evento.find_by_id(id)
    if (evento.usuario_id != session['usuario_id']):
        return "Usted no tiene permiso para editar este evento"
    return render_template('editar.html', evento=evento)


# RUTA PARA EDITAR evento ##

@app.route('/editar/<int:id>', methods=['POST'])
@session_required("/")
def update(id):
    data = {
        'id': id,
        'nombre': request.form['nombre'],
        'ubicacion': request.form['ubicacion'],
        'fecha': request.form['fecha'],
        'detalles': request.form['detalles'],
        'usuario_id': session['usuario_id']
    }
    if not eventos.Evento.validate(data):
        return redirect(f'/editar/{id}') 
    eventos.Evento.update(data)
    return redirect('/dashboard')


# RUTA PARA ELIMINAR evento ##

@app.route('/eliminar/<int:id>', methods=['POST'])
@session_required("/")
def delete_evento(id):
    eventos.Evento.delete_by_id(id)
    return redirect('/dashboard')



# RUTA PARA VER EL evento ##

@app.route('/ver/<int:id>')
@session_required("/")
def ver(id):
    evento = eventos.Evento.find_by_id(id)
    return render_template('ver.html', evento=evento)