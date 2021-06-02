from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired


class SignInForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    class_usage = SelectField('What class are you here for?',
                              choices=[(2151, 2151), (2155, 2155), (2159, 2159)],
                              validators=[DataRequired()])
    submit = SubmitField('Submit')
