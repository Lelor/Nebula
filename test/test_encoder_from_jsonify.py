from datetime import datetime
from unittest import TestCase

from flask import jsonify

from server import create_app
from server.database.model import Category, User, Article, ArticleContent
from server.encoder import DATE_PATTERN


class TestEncoder(TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.app.config['SERVER_NAME'] = 'localhost.domain'
        self.app_context = self.app.test_request_context()
        self.app_context.push()

    def test_should_jsonify_category_correctly(self):

        expected = {'name': 'sports'}
        response = jsonify(Category(id=1, name='sports'))
        self.assertEqual(expected, response.json)

    def test_should_jsonify_user_correctly(self):

        created_date = datetime.now()
        formatted_datetime = created_date.strftime(DATE_PATTERN)

        expected = {
            'created_at': formatted_datetime,
            'is_moderator': True,
            'username': 'test-user'
        }

        response = jsonify(User(
            id=1,
            username='test-user',
            is_moderator=True,
            email='user@test.net',
            password='test123',
            created_at=created_date
        ))

        self.assertEqual(expected, response.json)

    def test_should_jsonify_article_correctly(self):

        date = datetime.now()
        formatted_datetime = date.strftime(DATE_PATTERN)

        expected = {
            'title': 'The article title',
            'created_by': {
                'created_at': formatted_datetime,
                'is_moderator': True,
                'username': 'test-user'
            },
            'created_at': formatted_datetime,
            'updated_at': formatted_datetime,
            'useful_users': [],
            'useless_users': []
        }

        response = jsonify(Article(
            id=1,
            title='The article title',
            created_by=User(
                username='test-user',
                is_moderator=True,
                created_at=date
            ),
            created_at=date,
            updated_at=date,
            useful_users=[],
            useless_users=[]
        ))

        self.assertEqual(expected, response.json)

    def test_should_jsonify_article_content_correctly(self):

        date = datetime.now()
        formatted_datetime = date.strftime(DATE_PATTERN)

        expected = {
            'text': 'The article text',
            'author': {
                'created_at': formatted_datetime,
                'is_moderator': True,
                'username': 'test-user'
            },
            'is_approved_by_author': True,
            'is_approved_by_moderator': True,
            'created_at': formatted_datetime
        }

        response = jsonify(ArticleContent(
            text='The article text',
            author=User(
                username='test-user',
                is_moderator=True,
                created_at=date
            ),
            is_approved_by_author=True,
            is_approved_by_moderator=True,
            created_at=date
        ))

        self.assertEqual(expected, response.json)