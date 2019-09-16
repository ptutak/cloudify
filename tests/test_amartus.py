from amartus import main_app
from unittest import TestCase


class FirstTestCase(TestCase):
    def setUp(self):
        self.app = main_app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_main_route(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 404)
