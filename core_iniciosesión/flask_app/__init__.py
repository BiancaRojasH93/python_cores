import os
from flask import Flask, render_template
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt

# App Initialization 
load_dotenv() 
app = Flask(__name__) 
bcrypt = Bcrypt(app)
app.secret_key = os.getenv('APP_SECRET_KEY')
