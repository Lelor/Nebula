import json
from unittest import TestCase, mock

from flask import url_for

from server import create_app

class TestSignUp(TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()

    @mock.patch('server.controllers.sign_up.username_exists', return_value=False)
    def test_check_duplicate_should_return_success_message_if_user_does_not_exist(self, mocked_function):
        r = self.client.post(url_for("sign_up.check_duplicate_username"),
                             data=dict(username='foo'))
        expected_data = {'success': 'available username'}
        self.assertEqual(r.status_code, 200)
        self.assertEqual(json.loads(r.data), expected_data)

    @mock.patch('server.controllers.sign_up.username_exists', return_value=True)
    def test_check_duplicate_should_return_error_message_if_user_does_exist(self, mocked_function):
        r = self.client.post(url_for("sign_up.check_duplicate_username"),
                             data=dict(username='foo'))
        expected_data = {'error': 'username already registered in database'}
        self.assertEqual(r.status_code, 409)
        self.assertEqual(json.loads(r.data), expected_data)

    def test_check_duplicate_should_return_error_message_if_request_is_not_in_the_right_format(self):
        r = self.client.post(url_for("sign_up.check_duplicate_username"),
                             data=dict(usernme='foo'))
        expected_data = {'error': 'username not informed'}
        self.assertEqual(r.status_code, 422)
        self.assertEqual(json.loads(r.data), expected_data)

    @mock.patch('server.controllers.sign_up.email_exists', return_value=False)
    def test_check_duplicate_should_return_success_message_if_email_does_not_exist(self, mocked_function):
        r = self.client.post(url_for("sign_up.check_duplicate_email"),
                             data=dict(email='foo'))
        expected_data = {'success': 'available email'}
        self.assertEqual(r.status_code, 200)
        self.assertEqual(json.loads(r.data), expected_data)

    @mock.patch('server.controllers.sign_up.email_exists', return_value=True)
    def test_check_duplicate_should_return_error_message_if_email_does_exist(self, mocked_function):
        r = self.client.post(url_for("sign_up.check_duplicate_email"),
                             data=dict(email='foo'))
        expected_data = {'error': 'email already registered in database'}
        self.assertEqual(r.status_code, 409)
        self.assertEqual(json.loads(r.data), expected_data)

    def test_duplicate_email_should_return_error_message_if_request_is_not_in_the_right_format(self):
        r = self.client.post(url_for("sign_up.check_duplicate_email"),
                             data=dict(emal='foo'))
        expected_data = {'error': 'email not informed'}
        self.assertEqual(r.status_code, 422)
        self.assertEqual(json.loads(r.data), expected_data)

    @mock.patch('server.controllers.sign_up.email_exists', return_value=False)
    @mock.patch('server.controllers.sign_up.username_exists', return_value=False)
    @mock.patch('server.controllers.sign_up.register_user')
    def test_sign_up_route_with_valid_data_should_register_new_user(self,
                                                                    m_email,
                                                                    m_username,
                                                                    m_register_user):
        data = {
            'username': 'testuser',
            'email': 'test@foo.bar',
            'password': 'secret'
        }
        r = self.client.post(url_for("sign_up.register_new_user"),
                             data=data)
        expected_data = {'success': 'user registered'}
        m_register_user.assert_called_once()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(json.loads(r.data), expected_data)

    def test_sign_up_route_with_invalid_data_should_send_missing_fields(self):
        data = {
            'usernme': 'testuser',
            'email': 'test@foo.bar',
            'passwrd': 'secret'
        }
        r = self.client.post(url_for("sign_up.register_new_user"),
                             data=data)
        expected_data = {'missing_parameters': ['username', 'password']}
        self.assertEqual(r.status_code, 422)
        self.assertEqual(json.loads(r.data), expected_data)

    @mock.patch('server.controllers.sign_up.email_exists', return_value=True)
    def test_sign_up_route_with_registered_email_should_return_error_message(self,
                                                                             m_email):
        data = {
            'username': 'testuser',
            'email': 'test@foo.bar',
            'password': 'secret'
        }
        r = self.client.post(url_for("sign_up.register_new_user"),
                             data=data)
        expected_data = {'error': 'email already registered in database'}
        self.assertEqual(r.status_code, 409)
        self.assertEqual(json.loads(r.data), expected_data)

    @mock.patch('server.controllers.sign_up.email_exists', return_value=False)
    @mock.patch('server.controllers.sign_up.username_exists', return_value=True)
    def test_sign_up_route_with_registered_username_should_return_error_message(self,
                                                                                m_email,
                                                                                m_username):
        data = {
            'username': 'testuser',
            'email': 'test@foo.bar',
            'password': 'secret'
        }
        r = self.client.post(url_for("sign_up.register_new_user"),
                             data=data)
        expected_data = {'error': 'username already registered in database'}
        self.assertEqual(r.status_code, 409)
        self.assertEqual(json.loads(r.data), expected_data)
