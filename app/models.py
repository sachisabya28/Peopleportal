from app import db, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique=True)    
    password =  db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    
    def __init__(self, email, password, role_id=None):
        self.email = email
        self.password = password
        self.role_id = role_id

    # this is not essential, but a valuable method to overwrite as this is what we will see when we print out an instance in a REPL.
    def __repr__(self):
        return '<User email %r>' % self.email

    def get_role(self):
        return self.role_id

    def set_role(self, role_id):
        self.role_id = role_id

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Roles(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    user_id = db.relationship('User', backref='role',lazy=True)

    
    def __init__(self, name):
        self.name = name

    def get_id(self):
        return self.id

class Employee(db.Model):
    __tablename__ = 'employee'
    emp_id = db.Column(db.String(255), primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    position = db.Column(db.String(255))
    team = db.Column(db.String(255))
    phone = db.Column(db.String(255))

class Rooms(db.Model):
    __tablename__ = 'rooms'
    room_id = db.Column(db.String(255), primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    sitting = db.Column(db.String(255))
    status = db.Column(db.String(255))



