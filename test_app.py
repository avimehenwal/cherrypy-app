import unittest
import requests

from lxml.html import fromstring

class TestHelloWorld(unittest.TestCase):

    URL = "http://localhost:8080/"
    #URL = "http://example.com/"

    def setUp(self):
        self.homepage = requests.get(self.URL)

    def test_homepage_response(self):
        http_code = self.homepage.status_code
        self.assertEqual(http_code, 200)

    def test_app_title(self):
        tree = fromstring(self.homepage.content)
        expected = "avimehenwal"
        actual   = tree.findtext('.//title').strip()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()

