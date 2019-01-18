from unittest import TestCase, mock

from server.database.model import User


class TestUserModel(TestCase):

    @mock.patch('server.database.model.hashpw')
    @mock.patch('server.database.model.gensalt')
    @mock.patch('server.database.model.checkpw', return_value=True)
    def test_check_password_should_validate_user_password(self, checkpw, gensalt, hashpw):

        user = User(username='john', email='john@email.net', password='test-pass')
        self.assertTrue(user.check_password('test-pass'))

    @mock.patch('server.database.model.hashpw', return_value='hashed-password')
    def test_model_repr(self, mocked_password):
        expected_repr = f'<User(username=john, email=john@email.net, password=hashed-password)>'

        user = User(username='john', email='john@email.net', password='john123')
        self.assertEqual(expected_repr, user.__repr__())
