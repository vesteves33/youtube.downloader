from flask import Flask, render_template, url_for, request, flash, redirect
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'

bcrypt = Bcrypt(app)

from aplicacao import routes