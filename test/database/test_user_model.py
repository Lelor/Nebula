from unittest import TestCase, mock

from server.database.model import User


class TestUserModel(TestCase):

    @mock.patch('server.database.model.hashpw', return_value='hashed-password')
    def test_model_repr(self, mocked_password):
        expected_repr = f'<User(username=john, email=john@email.net, password=hashed-password)>'

        user = User(username='john', email='john@email.net', password='john123')
        self.assertEqual(expected_repr, user.__repr__())