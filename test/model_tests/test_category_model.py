from unittest import TestCase

from server.database.model import Category


class TestCategoryModel(TestCase):

    def test_model_repr(self):
        expected_repr = '<Category(id=None, name=test-category)>'
        self.assertEqual(expected_repr, Category(name='test-category').__repr__())
