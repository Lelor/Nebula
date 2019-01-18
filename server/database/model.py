from bcrypt import hashpw, gensalt, checkpw
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

db = SQLAlchemy()


class Category(db.Model):
    """
    Define the category data.
    """
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f'<Category(name={self.name})>'


class User(db.Model):
    """
    Define the user information.
    """
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)

    password = Column(String)
    email = Column(String, unique=True, nullable=False)
    is_moderator = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = hashpw(bytes(password, 'utf8'), gensalt())

    def check_password(self, password: str) -> bool:
        return checkpw(bytes(password, 'utf8'), self.password)

    def __repr__(self):
        return f'<User(username={self.username}, email={self.email}, password={self.password})>'


class ArticleContent(db.Model):
    """
    Define the contents of an article.
    """
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)

    author = relationship('User')
    author_id = Column(Integer, ForeignKey('user.id'))

    is_approved_by_author = Column(Boolean, default=False)
    is_approved_by_moderator = Column(Boolean, default=False)


# Association table for link users that consider an article useful.
useful_users = Table(
    'useful_users',
    db.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('article_id', Integer, ForeignKey('article.id'))
)


# Association table for link users that consider an article useless.
useless_users = Table(
    'useless_users',
    db.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('article_id', Integer, ForeignKey('article.id'))
)


class Article(db.Model):
    """
    Define the meta data of an article.
    """
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)

    created_by = relationship('User')
    created_by_id = Column(Integer, ForeignKey('user.id'))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    useful_users = relationship('User', secondary=useful_users)
    useless_users = relationship('User', secondary=useless_users)
