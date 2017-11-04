#!/usr/bin/env python3

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import app
from app.models import db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command("db", MigrateCommand)

@manager.command
def runserver():
    "Runs server in debug mode"
    app.run(debug=True)

if __name__ == "__main__":
    manager.run()
