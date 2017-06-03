from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError


class RegisterForm(FlaskForm):

    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password_1 = StringField('Password', validators=[DataRequired()])
    password_2 = StringField('Repeat Password', validators=[DataRequired()])

    def is_42(form, field):
        if field.data != 42:
            raise ValidationError('Must be 42')