from flask import redirect, render_template, request, session
from flask_app import app
from flask_app.models import usuarios, eventos
from flask_app import bcrypt
from flask import flash


from flask_app.utils.auth import session_required


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    if (not usuarios.Usuario.validate(request.form)):
        return redirect('/')
    # Encriptar la contraseña
    nuevo_usuario = usuarios.Usuario(request.form)
    nuevo_usuario.contraseña = bcrypt.generate_password_hash(
        request.form['contraseña'])
    user_id = usuarios.Usuario.save(nuevo_usuario.__dict__())
    session['user_id'] = user_id
    return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    usuario_id = usuarios.Usuario.validate_login(request.form)
    if not usuario_id:
        flash('Email o contraseña incorrectos', 'login')
        return redirect('/')
    session['usuario_id'] = usuario_id
    return redirect('/dashboard')

@app.route('/dashboard')
@session_required("/")
def dashboard():
    usuarios_list = usuarios.Usuario.find_by_id(session['usuario_id'])
    eventos_list = eventos.Evento.all()
    return render_template('dashboard.html', usuario=usuarios_list, eventos=eventos_list)


@app.route('/logout')
@session_required("/")
def logout():
    session.clear()
    return redirect('/')

