from flask import Flask, render_template, url_for, request, flash, redirect

app = Flask(__name__)

from aplicacao import routes