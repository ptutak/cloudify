import amartus.register as register
from unittest import TestCase


class TestRegister(TestCase):
    def setUp(self):
        self.new_register = register.Register()

    def test_register_register(self):
        self.new_register.register(1, '1.1.1.1', 'Piotr', 'My data')
        self.assertEqual(
            self.new_register._register[1],
            {'ip': '1.1.1.1', 'name': 'Piotr', 'userdata': 'My data'})

    def test_register_get(self):
        self.new_register.register(2, '1.1.1.1', 'Piotr', 'MyData')
        data = self.new_register.check(2)
        self.assertDictEqual(
            data,
            {'ip': '1.1.1.1', 'name': 'Piotr', 'userdata': 'MyData'})
        data = self.new_register.check(3)
        self.assertDictEqual(data, {})

    def test_register_list(self):
        self.new_register.register(1, '1.2.2.2', 'Piotr', 'Data')
        self.new_register.register(5, '3.3.3.3', 'Ela', 'DoubleData')
        host_list = self.new_register.list_register()
        self.assertListEqual(host_list, [1, 5])

    def test_register_delete(self):
        self.new_register.register(1, '3.3.3.3', 'Piotr', 'Data')
        self.new_register.delete(1)
        self.assertEqual(self.new_register.check(1), {})
        with self.assertRaises(KeyError):
            self.new_register.delete(3)

    def test_register_edit(self):
        self.new_register.register(1, '1.1.1.1', 'Piotr', 'Data')
        self.new_register.update(1, '2.2.2.2')
        self.assertEqual(
            self.new_register.check(1),
            {'ip': '2.2.2.2', 'name': 'Piotr', 'userdata': 'Data'})
        with self.assertRaises(KeyError):
            self.new_register.update(3)
