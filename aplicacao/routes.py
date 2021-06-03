from flask import Flask, render_template, url_for, request, flash, redirect
from aplicacao import app, bcrypt
from aplicacao.formularios import Formulario


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video')
def video():
    formulario = Formulario()
    
    return render_template('video.html', formulario=formulario)

@app.route('/musica')
def musica():
    formulario = Formulario()
    
    return render_template('musica.html', formulario=formulario)
