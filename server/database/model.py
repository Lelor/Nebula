from bcrypt import hashpw, gensalt, checkpw
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()


class Category(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f'<Category(name={self.name})>'


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)

    email = Column(String, unique=True, nullable=False)
    password = Column(String)

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = hashpw(password.encode(), gensalt())

    def check_password(self, password: str) -> bool:
        return checkpw(password, self.password)

    def __repr__(self):
        return f'<User(username={self.username}, email={self.email}, password={self.password})>'
