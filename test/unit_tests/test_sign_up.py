from unittest import TestCase, mock

from server.helpers.sign_up import (username_exists,
                                    email_exists,
                                    get_missing_fields,
                                    register_user)


class TestSignUp(TestCase):

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

    def test_get_missing_fields_should_return_empty_list_when_all_parameters_are_passed(self):
        """Validates the function that gets missing fields from dict passed."""
        data = {
            'username': 'xpto'
        }
        result = get_missing_fields(data, required_fields=('username',))
        self.assertEqual(result, ())

    def test_get_missing_fields_should_return_all_missing_required_fields(self):
        """Validates the function that gets missing fields from dict passed."""
        data = {
            'username': 'xpto'
        }
        result = get_missing_fields(data, required_fields=('username', 'email', 'password'))
        self.assertEqual(result, ('email', 'password'))

    @mock.patch('server.helpers.sign_up.session')
    def test_register_user_with_invalid_field(self, m_session):
        """Validates that the register function uses only intended data."""
        data = {
            'email': 'test@foo.bar',
            'username': 'testuser',
            'password': 'secret',
            'is_moderator': True
        }
        register_user(data)
        call = m_session.add.call_args_list[0][0][0]
        self.assertEqual(call.is_moderator, None)

    @classmethod
    @mock.patch('server.helpers.sign_up.session')
    def test_rollback_should_be_called_if_an_exception_is_raised_and_there_is_invalid_data(self, m_session):
        """Validates that the rollback is called if an exception is raised"""
        m_session.commit.side_effect = Exception()
        data = {
            'email': 'test@foo.bar',
            'username': 'testuser',
            'password': 'secret',
            'is_moderator': False
        }
        register_user(data)
        m_session.rollback.assert_called_once()

    @classmethod
    @mock.patch('server.helpers.sign_up.session')
    def test_rollback_should_be_called_if_an_exception_is_raised_and_there_is_no_invalid_data(self, m_session):
        """Validates that the rollback is called if an exception is raised"""
        m_session.commit.side_effect = Exception()
        data = {
            'email': 'test@foo.bar',
            'username': 'testuser',
            'password': 'secret',
            'is_moderator': True
        }
        register_user(data)
        m_session.rollback.assert_called_once()
