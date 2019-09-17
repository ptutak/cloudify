from amartus import main_app
from unittest import TestCase


class FirstTestCase(TestCase):
    def setUp(self):
        main_app.config['TESTING'] = True
        main_app.config['WTF_CSRF_ENABLED'] = False
        main_app.config['DEBUG'] = False
        self.app = main_app.test_client()

    def tearDown(self):
        pass

    def test_main_route(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 404)

    def test_register_route(self):
        result = self.app.put(
            '/ztp/register/1',
            data={
                'ip': '1.1.1.1',
                'name': 'Peter',
                'userdata': 'My special string'
            },
            follow_redirects=True)
        print(result.data)
