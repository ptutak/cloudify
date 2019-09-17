import json
from unittest import TestCase
from unittest.mock import patch
from amartus import main_app, main_app_register


class TestRoutes(TestCase):
    def setUp(self):
        main_app.config['TESTING'] = True
        self.app = main_app.test_client()
        main_app_register._register = {}

    def tearDown(self):
        pass

    def test_main_route(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 404)

    def test_register_route(self):
        with patch('amartus.routes.main_app_register') as mocked_register:
            response = self.app.put(
                '/ztp/register/1',
                data=json.dumps({
                    'ip': '1.1.1.1',
                    'name': 'Peter',
                    'userdata': 'My special string'}),
                follow_redirects=True)
        calls = []
        for call in mocked_register.mock_calls:
            name, args, kwargs = call
            calls.append((name, args, kwargs))
        self.assertEqual(
            calls,
            [('register', ('1', '1.1.1.1', 'Peter', 'My special string'), {})])
        self.assertEqual(
            json.loads(response.data.decode()),
            {'register': 'SUCCESS'})
        response = self.app.put(
            '/ztp/register/1',
            data={
                'ip': '1.11.1.1'
            }
        )
        self.assertEqual(response.status_code, 400)
        self.app.put(
            '/ztp/register/1',
            data=json.dumps({
                'ip': '1.1.1.1',
                'name': 'Peter',
                'userdata': 'My special string'}),
            follow_redirects=True)
        response = self.app.put(
            '/ztp/register/1',
            data=json.dumps({
                'ip': '1.1.1.1',
                'name': 'Peter',
                'userdata': 'My special string'}),
            follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def test_check_route(self):
        self.app.put(
            '/ztp/register/1',
            data=json.dumps({
                'ip': '1.1.1.1',
                'name': 'Peter',
                'userdata': 'MyData'
            }),
            follow_redirects=True
        )
        response = self.app.get('/ztp/check/1')
        self.assertEqual(
            {'ip': '1.1.1.1', 'name': 'Peter', 'userdata': 'MyData'},
            json.loads(response.data.decode()))
        response = self.app.get('/ztp/check/2')
        self.assertEqual({}, json.loads(response.data.decode()))

    def test_list_route(self):
        self.app.put(
            '/ztp/register/1',
            data=json.dumps({
                'ip': '1.1.1.1',
                'name': 'Peter',
                'userdata': 'MyData'
            }),
            follow_redirects=True)
        self.app.put(
            '/ztp/register/2',
            data=json.dumps({
                'ip': '1.1.3.1',
                'name': 'Ela',
                'userdata': 'ElaData'
            }),
            follow_redirects=True)
        response = self.app.get('/ztp/mng/list')
        self.assertEqual(
            {'hosts': ['1', '2']},
            json.loads(response.data.decode()))

    def test_delete_route(self):
        self.app.put(
            '/ztp/register/1',
            data=json.dumps({
                'ip': '1.1.1.1',
                'name': 'Peter',
                'userdata': 'MyData'
            }),
            follow_redirects=True)
        response = self.app.get('ztp/check/1')
        self.assertTrue(json.loads(response.data.decode()))
        self.app.get('/ztp/mng/1/delete')
        response = self.app.get('/ztp/check/1')
        self.assertFalse(json.loads(response.data.decode()))

    def test_edit_route(self):
        self.app.put(
            '/ztp/register/1',
            data=json.dumps({
                'ip': '1.1.1.1',
                'name': 'Peter',
                'userdata': 'MyData'
            }),
            follow_redirects=True)
        self.app.put(
            '/ztp/mng/1',
            data=json.dumps({
                'ip': '2.2.2.2'
            }),
            follow_redirects=True
        )
        response = self.app.get('/ztp/check/1')
        self.assertEqual(
            json.loads(response.data.decode()),
            {
                'ip': '2.2.2.2',
                'name': 'Peter',
                'userdata': 'MyData'
            }
        )
        response = self.app.put(
            '/ztp/mng/1',
            data=json.dumps({
                'sss': 'error'
            }),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 400)
        response = self.app.put(
            '/ztp/mng/3',
            data=json.dumps({
                'ip': '1.1.1.1'
            })
        )
        self.assertEqual(response.status_code, 400)
