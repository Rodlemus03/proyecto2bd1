from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy # type: ignore

app = Flask(__name__)

# Configurar la conexión a la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pelu1503@localhost:5432/proyecto2'
db = SQLAlchemy(app)

# Definir el modelo de la tabla de usuarios
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

# Ruta para manejar la solicitud POST del formulario de registro
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Crear un nuevo objeto Usuario
        nuevo_usuario = Usuario(email=email, password=password)

        # Agregar el nuevo usuario a la base de datos
        db.session.add(nuevo_usuario)
        db.session.commit()

        return '¡Usuario registrado correctamente!'

if __name__ == '__main__':
    app.run(debug=True)
