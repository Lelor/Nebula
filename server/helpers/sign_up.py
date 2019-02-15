from server.database.model import session, User


REQUIRED_FIELDS = ['username', 'password', 'email']


def username_exists(username: str) -> bool:
    """Checks if the username already exists in the database."""
    return bool(User.query.filter_by(username=username))


def email_exists(email: str) -> bool:
    """Checks if the email already exists in the database."""
    return bool(User.query.filter_by(email=email))


def get_missing_fields(data: dict, required_fields) -> tuple:
    """Gets the missing fields on the request json."""
    return tuple(filter(lambda x: x not in data.keys(), required_fields))


def register_user(data: dict):
    """Registers the user on database"""
    if data.get('is_moderator'):
        del data['is_moderator']
    try:
        user = User(**data)
        session.add(user)
        session.commit()

    except Exception:
        session.rollback()
