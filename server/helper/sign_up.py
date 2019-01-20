from server.database.model import User


def username_exists(username: str) -> bool:
    """Checks if the username already exists in the database."""
    return bool(User.query.filter_by(username=username))

def email_exists(email: str) -> bool:
    """Checks if the email already exists in the database."""
    return bool(User.query.filter_by(email=email))