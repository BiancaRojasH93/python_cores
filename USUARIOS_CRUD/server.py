from flask_app import app
from dotenv import load_dotenv
from flask_app.controllers import root_controller

load_dotenv()
# Correr el servidor
if __name__ == '__main__':
        app.run(debug=True)