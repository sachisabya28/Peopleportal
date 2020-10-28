from app.models import User, Roles, Employee, Rooms
from app import db, app

def main():
    
    try:
        #-----------------create user roles----------------
        role1 = Roles(name ='admin')
        role2 = Roles(name ='Engg Manager')
        role3 = Roles(name ='Office Manager') 
        with app.app_context():
            db.session.add(role1)
            db.session.add(role2)
            db.session.add(role3)
            db.session.commit()
            #---------------------create employee types--------------------
            employee1 = Employee(emp_id='BP001', name='John Doe', email='s.steele@aol.com', position='CEO', team='Management', phone='(+91)078-356-7263')
            employee2 = Employee(emp_id='BP012', name='Gerald Reeves', email='b.fitzgerald@hotmail.com', position='CTO', team='Management', phone='(+91)592-122-8320')
            room1 = Rooms(room_id='BP001', name='John Doe', email='s.steele@aol.com', sitting='10', status='Available')
            room2 = Rooms(room_id='BP012', name='Gerald Reeves', email='b.fitzgerald@hotmail.com', sitting='15', status='Booked')
            db.session.add(employee1)
            db.session.add(employee2)
            db.session.add(room1)
            db.session.add(room2)
            db.session.commit()
            #----------------------create user types------------------------------
            role_val = Roles.query.filter_by(name='admin').first()
            user1 = User(email='admin@email.com', password = 'password1', role_id=role_val.id)  
            role_val = Roles.query.filter_by(name='Engg Manager').first()
            user2 = User(email='engmanager@email.com', password = 'password2', role_id=role_val.id) 
            role_val = Roles.query.filter_by(name='Office Manager').first()
            user3 = User(email='ofcmanager@email.com', password = 'password3', role_id=role_val.id) 
        
            db.session.add(user1)
            db.session.add(user2)
            db.session.add(user3)
            db.session.commit()

    except Exception as ex:
        print(ex) 

if __name__ == '__main__':
    main()




