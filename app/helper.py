from app import db
from app.models import User, Roles
from sqlalchemy.exc import IntegrityError

class UserDoesNotExistException(Exception):
    pass

def save_changes(employee, form, new=False):
    try:
        employee.emp_id = str(form.emp_id.data)
        employee.name = str(form.name.data)
        employee.email = str(form.email.data)
        employee.position = str(form.position.data)
        employee.team = str(form.team.data)
        employee.phone = str(form.phone.data)

        if new:
            db.session.add(employee)
        db.session.commit()
    except IntegrityError:
        """Handle integrity errors, such as
        when adding an resource that already exists
        """

        db.session.rollback()
        return {"error": "An error occurred. Please review your output and "
                "try again."}, 400

def save_changes_addroom(rooms, form, new=False):
    try:
        rooms.room_id = str(form.room_id.data)       
        rooms.email = str(form.email.data)
        rooms.name = str(form.name.data)
        rooms.sitting = form.sitting.data
        rooms.status = 'Available'
        if new:
            db.session.add(rooms)
        db.session.commit()
    except IntegrityError:
        """Handle integrity errors, such as
        when adding an resource that already exists
        """

        db.session.rollback()
        return {"error": "An error occurred. Please review your output and "
                "try again."}, 400
    
def check_user_permission(role):
    if role == "admin":
        permission_level = ("employee_create",
                            "employee_read",
                            "employee_edit",
                            "employee_delete",
                            "conf_room_create",
                            "conf_room_read","conf_room_edit",
                            "conf_room_delete")
    elif role == "Engg Manager":
        permission_level = ("employee_create",
                        "employee_read",
                        "employee_edit")
    else:
        permission_level = ("conf_room_create",
                            "conf_room_read",
                            "conf_room_edit")
    return permission_level



def get_access(email):

    try:
        requesting_user = User.query.filter_by(email=str(email)).first()
    except Exception as ex:
        raise UserDoesNotExistException()

    requesting_user_obj = User.query.filter_by(email=str(email)).first()
    requesting_user_role = requesting_user_obj.role.name

    return check_user_permission(requesting_user_role)

def delete_resource(resource, **kwargs):
    """
    Delete a resource permanently from the database.
    Arguments:
    """

    db.session.delete(resource)
    db.session.commit()
    return {"message": "You have successfully deleted" }





