from flask import Flask, render_template, url_for, request, flash, redirect
from aplicacao import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/musica')
def musica():
    return render_template('musica.html')

@app.route('/converter')
def converter(): 
    return render_template('converter.html')