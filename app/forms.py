from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class UserForm(FlaskForm):
    
    email = StringField('Email', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired()])

class EmployeeForm(FlaskForm):
    emp_id = StringField('Emp_id', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    name = StringField('Name', validators=[InputRequired()])
    position = StringField('Position', validators=[InputRequired()])
    team = StringField('Team', validators=[InputRequired()])
    phone = StringField('Phoneno', validators=[InputRequired()])


class RoomForm(FlaskForm):
    room_id = StringField('Room_id', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    name = StringField('Name', validators=[InputRequired()])
    sitting = StringField('Sitting', validators=[InputRequired()])
