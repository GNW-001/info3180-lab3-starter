from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import  DataRequired

class ContactForm(FlaskForm):
    name = TextField('Name',validators=[DataRequired()])
    email = TextField('E-mail', validators=[DataRequired()])
    subject = TextField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')
