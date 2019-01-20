from unittest import TestCase, mock

from bcrypt import checkpw

from server.database.model import User


class TestUserModel(TestCase):

    @mock.patch('server.database.model.gensalt')
    @mock.patch('server.database.model.hashpw', return_value='hashed-pass')
    def test_hash_password(self, hashpw, gensalt):

        user = User(password='pass')
        user.hash_password()
        self.assertEqual(user.password, 'hashed-pass')

    @mock.patch('server.database.model.checkpw', return_value=True)
    def test_check_password(self, checkpw):
        user = User(password='pass')
        self.assertTrue(user.check_password('pass'))

    def test_model_repr(self):
        expected_repr = '<User(id=1, username=john, password=password, ' \
                        'email=john@email.net, is_moderator=True, created_at=1234567890)>'

        user = User(
            id=1,
            username='john',
            email='john@email.net',
            password='password',
            is_moderator=True,
            created_at=1234567890)

        self.assertEqual(expected_repr, user.__repr__())
