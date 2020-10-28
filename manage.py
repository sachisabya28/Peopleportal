import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import app, db
from app.models import User, Roles, Employee, Rooms

basedir = os.path.abspath(os.path.dirname(__file__))
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)


def make_shell_context():
    """Returns application and database instances
    to the shell importing them automatically
    on `python manager.py shell`.
    """
    return dict(app=app, db=db, User=User, Roles=Roles,
                Employee=Employee, Rooms=Rooms )


manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()