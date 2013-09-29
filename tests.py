import unittest
import pyjolokia


class CoreJolikiaTests(unittest.TestCase):

    def setUp(self):
        self.client = pyjolokia.Jolokia('http://example.com/joloka/')

    def default_test_timeout(self):
        """ Test default timeout """
        self.assertEqual(self.client.timeout, 10)

    def custom_test_timeout(self):
        """ Test for custom timeout """
        client = pyjolokia.Jolokia('http://example.com/jolokia/', timeout=20)
        self.assertEqual(client.timeout, 20)

    def basic_auth_test(self):
        self.client.auth(httpusername='test', httppassword='testpassword')

        self.assertEqual(self.client.authConfig['auth']['username'],
                         'test')
        self.assertEqual(self.client.authConfig['auth']['password'],
                         'testpassword')
