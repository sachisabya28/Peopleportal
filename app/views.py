import json
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session
from flask_login import login_required, login_user, logout_user
from app.forms import UserForm, EmployeeForm, RoomForm
from app.models import User, Employee, Rooms
from app.helper import save_changes, get_access, delete_resource, save_changes_addroom

if os.getenv("ENVIRONMENT") == "development":
    path = "http://127.0.0.1:5000/"
else:
    path = ""


# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
# -------------------------------------------------

@app.route('/employee', methods=['GET'])
@login_required
def show_employee():
    employees = Employee.query.all()
    return render_template('employee_detail.html', employee=employees)

@app.route('/addemp', methods=['GET','POST'])
@login_required
def add_employee():
    try:
        email_id = request.cookies.get('YourSessionCookie')
        form = EmployeeForm(request.form)
        if request.method == 'POST':     
            if 'employee_create' in get_access(email_id):
                employee = Employee()
                save_changes(employee, form, new=True)
                return redirect(url_for('show_employee'))
            flash('Can not create employee details!!! Access Denied')
        return render_template('new_employee.html', form=form)
    except Exception as ex:
        flash(ex)


@app.route('/deleteemp/<string:id>', methods=['GET', 'POST'])
@login_required
def delete_emp(id):
    employee = Employee.query.filter_by(emp_id=id).first()
    email_id = request.cookies.get('YourSessionCookie')
    if employee:
        if 'employee_delete' in get_access(email_id):
            delete_resource(employee, id=id)
        else:
            flash("Can't delete employee detail", "error")
    else:
        flash("Specified student doesn't exit!", "error")

    return redirect(url_for('show_employee'))

@app.route('/editemp/<string:id>', methods=['GET', 'POST'])
@login_required
def edit_emp(id):
    employee = Employee.query.filter_by(emp_id=id).first()
    email_id = request.cookies.get('YourSessionCookie')
    if employee:
        if 'employee_edit' in get_access(email_id):
            employee.email = request.form['email']
            employee.name  = request.form['name']
            employee.position   = request.form['position']
            employee.team  = request.form['team']
            employee.phone   = request.form['phone']
            db.session.commit()
    else:
        flash("Specified employee doesn't exist!", "error")

    return redirect(url_for('show_employee'))

@app.route('/rooms', methods=['GET', 'POST'])
@login_required
def show_rooms():
    rooms = Rooms.query.all()
    return render_template('rooms.html', rooms=rooms)

@app.route('/addroom', methods=['GET','POST'])
@login_required
def add_room():
    try:
        email_id = request.cookies.get('YourSessionCookie')
        form = RoomForm(request.form)
        if request.method == 'POST':     
            if 'conf_room_create' in get_access(email_id):
                rooms = Rooms()
                save_changes_addroom(rooms, form, new=True)
                return redirect(url_for('show_rooms'))
            flash('Can not create room!!! Access Denied')
        return render_template('new_room.html', form=form)
    except Exception as ex:
        flash(ex)
        return ex

@app.route('/deleteroom/<string:id>', methods=['GET', 'POST'])
@login_required
def delete_room(id):
    try:
        room = Rooms.query.filter_by(room_id=id).first()
        email_id = request.cookies.get('YourSessionCookie')
        if room:
            if 'conf_room_delete' in get_access(email_id):
                delete_resource(room, id=id)
            else:
                flash("Can't delete room detail", "error")
        else:
            flash("Specified room doesn't exit!", "error")

        return redirect(url_for('show_rooms'))
    except Exception as ex:
        return ex


@app.route('/editroom/<string:id>', methods=['GET', 'POST'])
@login_required
def edit_room(id):
    form = RoomForm(request.form)
    room = Rooms.query.filter_by(room_id=id).first()
    email_id = request.cookies.get('YourSessionCookie')
    if room:
        if 'conf_room_edit' in get_access(email_id):
            room.email = str(form.email.data)
            room.name = str(form.name.data)
            room.sitting = str(form.sitting.data)
            room.status = 'Available'
            db.session.commit()
    else:
        flash("Specified employee doesn't exist!", "error")
    return redirect(url_for('show_rooms'))


@app.route('/', methods=['GET', 'POST'])
def login():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():  
        
        email = form.email.data 
        password = form.password.data
        user_data = User.query.filter_by(email=email).first()
        if user_data:           
            if user_data.password == str(password) :   
                logged_user = User.query.get(int(user_data.id))
                login_user(logged_user)
                session['username'] = email               
                response = redirect(url_for('show_employee')) 
                response.set_cookie('YourSessionCookie', email)               
                return response
            flash('Wrong email or password')
            return render_template('login.html', form=form)
        return render_template("login.html", form=form)
    else: 
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    message = "Successfully logged out."
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
