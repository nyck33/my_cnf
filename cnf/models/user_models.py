from flask_user import UserMixin, UserManager

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from flask import current_app as app

#with app.app_context():
db = app.db

# Define User document
# NB: Make sure to add flask_user UserMixin
class User(db.Document, UserMixin):
    #email_confirmed_at = app.db.StringField('confirmed at', datetime.datetime.now())
    active = db.BooleanField(default=True)
    # User info
    first_name = db.StringField(default='')
    last_name = db.StringField(default='')
    email = db.StringField(default='')
    # User authentication info
    username = db.StringField(default='')
    password = db.StringField(default='')
    # Relationships
    roles = db.ListField(app.db.StringField(), default=[])


#Roles and UsersRoles add later

#Define User profile form
class UserProfileForm(FlaskForm):
    first_name = StringField('First name', validators=[
        validators.DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[
        validators.DataRequired('Last name is required')
    ])
    submit = SubmitField('Save')

