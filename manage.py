import os
import unittest
import main.models.userModels
import main.models.schoolModels

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from main import create_app
from main.models import db


app = create_app('dev')

app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    #app.run(host='0.0.0.0')
    app.run()

@manager.command
def test():
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()

