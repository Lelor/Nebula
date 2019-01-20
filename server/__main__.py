from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from server.database.model import db

app = Flask(__name__)
app.config.from_object('dev-confguration')

# Initializing database.
db.init_app(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
