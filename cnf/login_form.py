from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField
from wtforms.validators import DataRequired, Email, InputRequired, Length

class LoginForm(FlaskForm):
    first_name = StringField('Enter first name: ', validators=[DataRequired(), InputRequired()])
    last_name = StringField('Enter last name: ', validators=[DataRequired(), InputRequired()])
    email = StringField('Enter Email as Username: ', validators=[DataRequired(), Email(), InputRequired()])
    username = StringField('Enter username', validators=[DataRequired(), InputRequired()])
    password = PasswordField('Enter Password between 8 to 32 characters',
                                    validators=[DataRequired(), InputRequired(), Length(8, 32)])
    dob = DateField('Enter your dob', validators=[DataRequired(), InputRequired()])
    submit = SubmitField('Submit')