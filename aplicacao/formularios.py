from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class Formulario(FlaskForm):
    video = StringField('URL do vídeo', validators=[DataRequired(), URL()])
    musica = StringField('URL da música', validators=[DataRequired(), URL()])
    botao = SubmitField('Baixar')