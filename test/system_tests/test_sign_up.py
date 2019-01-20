import json
from unittest import TestCase, mock

from flask import Flask, url_for

from server.__main__ import app
from server.blueprints import configure_blueprints
from server.database.model import User

class TestSignUp(TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.testing = True
        self.app.app_context = app.test_request_context()
        self.app.app_context.push()
        configure_blueprints(self.app)
        self.client = app.test_client()
    
    @mock.patch('flask_sqlalchemy._QueryProperty.__get__')
    def test_check_duplicate_should_return_success_message_if_user_does_not_exist(self, mocked_query):
        mocked_query.return_value.filter_by.return_value = []
        r = self.client.post(url_for("contributor.check_duplicate_username"),
                             data=dict(username='foo'))
        expected_data = {'success': 'available username'}
        self.assertEqual(json.loads(r.data), expected_data)
