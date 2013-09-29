import unittest
import pyjolokia


class CoreJolikiaTests(unittest.TestCase):

    def setUp(self):
        self.client = pyjolokia.Jolokia('http://httpbin.org/post')

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

    def test_read_response(self):
        response = self.client.request(
            type='read',
            mbean='java.lang:type=Threading',
            attribute='ThreadCount')

        json_data = response['json']

        self.assertEqual(json_data['type'], 'read')
        self.assertEqual(json_data['mbean'], 'java.lang:type=Threading')
        self.assertEqual(json_data['attribute'], 'ThreadCount')

    def test_auth_header(self):

        self.client.auth(httpusername='test', httppassword='testpassword')

        response = self.client.request(
            type='read',
            mbean='java.lang:type=Threading',
            attribute='ThreadCount')

        headers = response['headers']

        self.assertTrue('Authorization' in headers)
