from datetime import datetime
from unittest import TestCase

from werkzeug.http import http_date

from server.database.model import Category, User, ArticleContent, Article
from server.encoder import Encoder, DATE_PATTERN


class TestEncoder(TestCase):

    def test_category_encoding(self):

        expected = {'name': 'test-category'}
        actual = Encoder().default(Category(id=1, name='test-category'))

        self.assertEqual(expected, actual)

    def test_user_encoding(self):

        created_date = datetime.now()
        formatted_datetime = created_date.strftime(DATE_PATTERN)

        expected = {
            'username': 'test-user',
            'is_moderator': True,
            'created_at': formatted_datetime
        }

        actual = Encoder().default(User(
            id=1,
            username='test-user',
            is_moderator=True,
            email='user@test.net',
            password='test123',
            created_at=created_date
        ))

        self.assertEqual(expected, actual)

    def test_article_encoding(self):
        created_date = datetime.now()
        formatted_datetime = created_date.strftime(DATE_PATTERN)

        expected = {
            'title': 'The article title',
            'created_by': None,
            'created_at': formatted_datetime,
            'updated_at': formatted_datetime,
            'useful_users': [],
            'useless_users': []
        }

        actual = Encoder().default(Article(
            id=1,
            title='The article title',
            created_by=None,
            created_at=created_date,
            updated_at=created_date,
            useful_users=[],
            useless_users=[]
        ))

        self.assertEqual(expected, actual)

    def test_article_content_encoding(self):

        created_date = datetime.now()
        formatted_datetime = created_date.strftime(DATE_PATTERN)

        expected = {
            'text': 'The article text',
            'author': None,
            'is_approved_by_author': True,
            'is_approved_by_moderator': False,
            'created_at': formatted_datetime
        }

        actual = Encoder().default(ArticleContent(
            id=1,
            text='The article text',
            author=None,
            is_approved_by_author=True,
            is_approved_by_moderator=False,
            created_at=created_date
        ))

        self.assertEqual(expected, actual)

    def test_encoder_should_use_super_implementation_when_instance_is_not_a_table_model(self):
        """Use default implementation of encoder, not ours"""
        date = datetime.now()
        actual = Encoder().default(date)
        self.assertEqual(http_date(date.utctimetuple()), actual)