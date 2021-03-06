import unittest
import urlparse
from pyphoenix.avatica import parse_url


class ParseUrlTest(unittest.TestCase):

    def test_parse_url(self):
        self.assertEqual(urlparse.urlparse('http://localhost:8765/'), parse_url('localhost'))
        self.assertEqual(urlparse.urlparse('http://localhost:2222/'), parse_url('localhost:2222'))
        self.assertEqual(urlparse.urlparse('http://localhost:2222/'), parse_url('http://localhost:2222/'))
