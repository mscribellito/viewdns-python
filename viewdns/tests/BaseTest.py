import os
import unittest

class BaseTest(unittest.TestCase):

    def setUp(self):

        self.base_url = 'https://api.viewdns.info/'
        self.api_token = '2d1cb7571b6bb06a1d287398db51cd20'

    def load_from_file(self, json_file):

        cwd = os.path.dirname(__file__)

        with open(os.path.join(cwd, 'data/%s' % json_file), 'r') as f:
            return f.read()
