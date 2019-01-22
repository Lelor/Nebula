import json
from unittest import TestCase, mock

from flask import Flask, url_for

from server.__main__ import app
from server.database.model import User

class TestSignUp(TestCase):

    def setUp(self):
        self.app = app
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
    
    @mock.patch('server.controllers.contributor.username_exists', return_value=False)
    def test_check_duplicate_should_return_success_message_if_user_does_not_exist(self, mocked_function):
        r = self.client.post(url_for("contributor.check_duplicate_username"),
                             data=dict(username='foo'))
        expected_data = {'success': 'available username'}
        self.assertEqual(r.status_code, 200)
        self.assertEqual(json.loads(r.data), expected_data)

    @mock.patch('server.controllers.contributor.username_exists', return_value=True)
    def test_check_duplicate_should_return_error_message_if_user_does_exist(self, mocked_function):
        r = self.client.post(url_for("contributor.check_duplicate_username"),
                             data=dict(username='foo'))
        expected_data = {'error': 'username already registered in database'}
        self.assertEqual(r.status_code, 400)
        self.assertEqual(json.loads(r.data), expected_data)

    def test_check_duplicate_should_return_error_message_if_request_is_not_in_the_right_format(self):
        r = self.client.post(url_for("contributor.check_duplicate_username"),
                             data=dict(usernme='foo'))
        expected_data = {'error': 'username not informed'}
        self.assertEqual(r.status_code, 400)
        self.assertEqual(json.loads(r.data), expected_data)

    @mock.patch('server.controllers.contributor.email_exists', return_value=False)
    def test_check_duplicate_should_return_success_message_if_email_does_not_exist(self, mocked_function):
        r = self.client.post(url_for("contributor.check_duplicate_email"),
                             data=dict(email='foo'))
        expected_data = {'success': 'available email'}
        self.assertEqual(r.status_code, 200)
        self.assertEqual(json.loads(r.data), expected_data)

    @mock.patch('server.controllers.contributor.email_exists', return_value=True)
    def test_check_duplicate_should_return_error_message_if_email_does_exist(self, mocked_function):
        r = self.client.post(url_for("contributor.check_duplicate_email"),
                             data=dict(email='foo'))
        expected_data = {'error': 'email already registered in database'}
        self.assertEqual(r.status_code, 400)
        self.assertEqual(json.loads(r.data), expected_data)

    def test_duplicate_email_should_return_error_message_if_request_is_not_in_the_right_format(self):
        r = self.client.post(url_for("contributor.check_duplicate_email"),
                             data=dict(emal='foo'))
        expected_data = {'error': 'email not informed'}
        self.assertEqual(r.status_code, 400)
        self.assertEqual(json.loads(r.data), expected_data)
