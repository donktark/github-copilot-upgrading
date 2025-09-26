import os
import unittest

from guachi import ConfigMapper
from guachi.database import dbdict

# An example of a default config dict
DEFAULT_CONFIG = {
            'frequency': 60,
            'master': 'False',
            'host': 'localhost',
            'ssh_user': 'root',
            'ssh_port': 22,
            'hosts_path': '/opt/pacha',
            'hg_autocorrect': 'True',
            'log_enable': 'False',
            'log_path': 'False',
            'log_level': 'DEBUG',
            'log_format': '%(asctime)s %(levelname)s %(name)s %(message)s',
            'log_datefmt' : '%H:%M:%S'
            }


class test_ConfigMapper(unittest.TestCase):

    def setUp(self):
        try:
            os.remove('/tmp/guachi.db')
            os.remove('/tmp/foo_guachi.db')
        except Exception:
            pass 

    def tearDown(self):
        try:
            os.remove('/tmp/guachi.db')
            os.remove('/tmp/foo_guachi.db')
        except Exception:
            pass 


    def test_init(self):
        foo = ConfigMapper('/tmp')
        expected = '/tmp/guachi.db'
        actual = foo.path 
        self.assertEqual(actual, expected) 


    def test__call__(self):
        """ConfigMapper should be callable"""
        foo = ConfigMapper('/tmp')
