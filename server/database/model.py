from bcrypt import hashpw, gensalt, checkpw
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    func,
    ForeignKey,
    Table
)
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Category(db.Model):
    """
    Define the category data.
    """
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def __repr__(self):  # pragma: no cover
        return f'<Category(id={self.id}, name={self.name})>'


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

    def hash_password(self):
        self.password = hashpw(bytes(self.password, 'utf8'), gensalt())

    def check_password(self, password: str) -> bool:
        return checkpw(bytes(password, 'utf8'), self.password)

    def __repr__(self):  # pragma: no cover
        return '<User(id={}, username={}, password={}, email={}, ' \
               'is_moderator={}, created_at={})>'\
            .format(
                self.id,
                self.username,
                self.password,
                self.email,
                self.is_moderator,
                self.created_at
            )


class ArticleContent(db.Model):
    """
    Define the contents of an article.
    """
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)

    author = relationship('User')
    author_id = Column(Integer, ForeignKey('user.id'))

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    is_approved_by_author = Column(Boolean, default=False)
    is_approved_by_moderator = Column(Boolean, default=False)

    def __repr__(self):  # pragma: no cover
        return 'ArticleContent(id={}, text={}, author={}, ' \
               'is_approved_by_author={}, is_approved_by_moderator={}, ' \
               'created_at={}'\
            .format(
                self.id,
                self.text,
                self.author,
                self.is_approved_by_author,
                self.is_approved_by_moderator,
                self.created_at
            )


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

    def __repr__(self):  # pragma: no cover
        return 'Article(id={}, title={}, created_by={}, created_at={}, ' \
               'updated_at={}, useful_users={}, useless_users={})'\
            .format(
                self.id,
                self.title,
                self.created_by,
                self.created_at,
                self.updated_at,
                self.useful_users,
                self.useless_users
            )
