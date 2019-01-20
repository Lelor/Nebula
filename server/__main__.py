from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from server.blueprints import configure_blueprints
from server.database.model import db

app = Flask(__name__)
app.config.from_object('dev-confguration')

#registering blueprints
configure_blueprints(app)

# Initializing database.
db.init_app(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
