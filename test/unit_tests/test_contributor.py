from unittest import TestCase, mock

from server.helper.sign_up import username_exists, email_exists


class TestContributor(TestCase):

    @mock.patch('flask_sqlalchemy._QueryProperty.__get__')
    def test_username_exists_should_return_true_if_username_already_registered(self, mocked_query):
        """Validates that the function returns true if the query filtered anything."""
        mocked_query.return_value.filter_by.return_value = ['foo']
        result = username_exists('foo')
        self.assertTrue(result)
        self.assertFalse


    @mock.patch('flask_sqlalchemy._QueryProperty.__get__')
    def test_username_exists_should_return_false_if_username_is_not_registered(self, mocked_query):
        """Validates that the function returns true if the query filtered anything."""
        mocked_query.return_value.filter_by.return_value = []
        result = username_exists('foo')
        self.assertFalse(result)

    @mock.patch('flask_sqlalchemy._QueryProperty.__get__')
    def test_email_exists_should_return_true_if_email_is_registered(self, mocked_query):
        """Validates that the function returns true if the query filtered anything."""
        mocked_query.return_value.filter_by.return_value = ['foo']
        result = email_exists('foo')
        self.assertTrue(result)

    @mock.patch('flask_sqlalchemy._QueryProperty.__get__')
    def test_email_exists_should_return_false_if_email_is_not_registered(self, mocked_query):
        """Validates that the function returns true if the query filtered anything."""
        mocked_query.return_value.filter_by.return_value = []
        result = email_exists('foo')
        self.assertFalse(result)
