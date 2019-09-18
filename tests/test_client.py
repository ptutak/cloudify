import json
from unittest import TestCase
from unittest.mock import patch, MagicMock
import amartus.client as client
from amartus.client import getnode, get_ip


class TestClient(TestCase):
    def setUp(self):
        self.patcher = patch('amartus.client.urlopen')
        self.mocked_urlopen = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_args(self):
        args = client.parse_args([
            'https:/my.local.address',
            '-n',
            'Peter',
            '-u',
            'Data'])
        self.assertEqual(args.name, 'Peter')
        self.assertEqual(args.userdata, 'Data')

    def test_get_ip(self):
        # Don't really have an idea how to test this functionality
        pass

    def test_main(self):
        with patch('amartus.client.parse_args') as mocked_parse:
            with patch('builtins.print'):
                local_args = MagicMock()
                local_args.name = 'Peter'
                local_args.userdata = 'Data'
                local_args.server_address = 'http://my.local.address'
                mocked_parse.return_value = local_args
                self.mocked_urlopen.return_value.read\
                    .return_value.decode.return_value\
                    = '{"register": "SUCCESS"}'
                client.main()

        args, kwargs = self.mocked_urlopen.call_args
        request = args[0]
        self.assertEqual(
            request.full_url,
            'http://my.local.address/ztp/register/{}'.format(getnode()))
        self.assertEqual(
            json.loads(request.data),
            {'ip': get_ip(), 'name': 'Peter', 'userdata': 'Data'}
        )
        self.assertEqual(
            request.header_items(),
            [('Content-type', 'application/json')]
        )
