from os import path, remove, mkdir
import unittest 

from guachi import ConfigMapper


class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.mapped_options = {
            'guachi.db.host':'db_host',
            'guachi.db.port':'db_port',
            'guachi.web.host':'web_host',
            'guachi.web.port':'web_port',
            }

        self.mapped_defaults = {
            'db_host': 'localhost',
            'db_port': 27017,
            'web_host': 'localhost',
            'web_port': '8080',
            }

        try:
            if path.exists('/tmp/guachi'):
                remove('/tmp/guachi')
            else:
                mkdir('/tmp/guachi')
        except Exception:
            pass

    def tearDown(self):
        try:
            if path.exists('/tmp/guachi'):
                remove('/tmp/guachi')
            else:
                mkdir('/tmp/guachi')
        except Exception:
            pass



    def test_access_mapped_configs_empty_dict(self):
        foo = ConfigMapper('/tmp/guachi')
        foo.set_ini_options(self.mapped_options)
        foo.set_default_options(self.mapped_defaults)
        foo.set_config({})

        # try as much operations as we can and assert them
        self.assertEqual(foo(), {})
