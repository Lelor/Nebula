from functools import singledispatch

from flask.json import JSONEncoder

from server.database.model import User, Category, Article, ArticleContent

DATE_PATTERN = '%d/%m/%Y %H:%M:%S'


class Encoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, (Category, User, Article, ArticleContent)):
            return to_dictionary(object)

        return super(Encoder, self).default(object)


@singledispatch
def to_dictionary(object):  # pragma: no cover
    ...


@to_dictionary.register(Category)
def _(args: Category) -> dict:
    return {
        'name': args.name
    }


@to_dictionary.register(User)
def _(args: User) -> dict:
    return {
        'username': args.username,
        'is_moderator': args.is_moderator,
        'created_at': args.created_at.strftime(DATE_PATTERN)
    }


@to_dictionary.register(Article)
def _(args: Article) -> dict:
    return {
        'title': args.title,
        'created_by': args.created_by,
        'created_at': args.created_at.strftime(DATE_PATTERN),
        'updated_at': args.updated_at.strftime(DATE_PATTERN),
        'useful_users': args.useful_users,
        'useless_users': args.useless_users
    }


@to_dictionary.register(ArticleContent)
def _(args: ArticleContent) -> dict:
    return {
        'text': args.text,
        'author': args.author,
        'is_approved_by_author': args.is_approved_by_author,
        'is_approved_by_moderator': args.is_approved_by_moderator,
        'created_at': args.created_at.strftime(DATE_PATTERN)
    }
