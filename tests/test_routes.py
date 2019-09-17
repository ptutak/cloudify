from amartus import main_app
from unittest import TestCase
from unittest.mock import patch


class FirstTestCase(TestCase):
    def setUp(self):
        main_app.config['TESTING'] = True
        self.app = main_app.test_client()

    def tearDown(self):
        pass

    def test_main_route(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 404)

    def test_register_route(self):
        with patch('amartus.routes.main_app_register') as mocked_register:
            result = self.app.put(
                '/ztp/register/1',
                data={
                    'ip': '1.1.1.1',
                    'name': 'Peter',
                    'userdata': 'My special string'},
                follow_redirects=True)
        calls = []
        for call in mocked_register.mock_calls:
            name, args, kwargs = call
            calls.append((name, args, kwargs))
        self.assertEqual(
            calls,
            [('register', ('1', '1.1.1.1', 'Peter', 'My special string'), {})])
