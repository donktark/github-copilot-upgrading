import os
import sqlite3
import unittest
from guachi import database

class TestDbdict(unittest.TestCase):
    
    def tearDown(self):
        try:
            os.remove('/tmp/test_guachi')
        except Exception:
            pass 

    def test_create_database(self):
        foo = database.dbdict('/tmp/test_guachi')
        self.assertTrue(os.path.isfile('/tmp/test_guachi'))

    def test_init(self):
        foo = database.dbdict('/tmp/test_guachi')

        self.assertEqual(foo.db_filename, '/tmp/test_guachi')
        self.assertEqual(foo.table, '_guachi_data')
        self.assertEqual(foo.select_value, 'SELECT value FROM _guachi_data WHERE key=?')
        self.assertEqual(foo.select_key, 'SELECT key FROM _guachi_data WHERE key=?')
        self.assertEqual(foo.update_value, 'UPDATE _guachi_data SET value=? WHERE key=?')
        self.assertEqual(foo.insert_key_value, 'INSERT INTO _guachi_data (key,value) VALUES (?,?)')
        self.assertEqual(foo.delete_key, 'DELETE FROM _guachi_data WHERE key=?')

    def test_init_guachi_table(self):
        """Make sure we can check other tables"""
        foo = database.dbdict('/tmp/test_guachi', table='_guachi_options')
        self.assertEqual(foo.table, '_guachi_options')

    def test_get_item_keyerror(self):
        foo = database.dbdict('/tmp/test_guachi')
        self.assertRaises(KeyError, foo.__getitem__, 'meh')

    def test_get_item(self):
        foo = database.dbdict('/tmp/test_guachi')
        foo['bar'] = 'beer'
        self.assertEqual(foo['bar'], u'beer')
 
    def test_setitem_update(self):
        """If it already exists, you need to do an update"""
        foo = database.dbdict('/tmp/test_guachi')
        foo['a'] = 1
        foo['a'] = 2
        self.assertEqual(foo['a'], 2)

    def test_close_db(self):
