from guachi.database import dbdict
from guachi.config import DictMatch
import os

class ConfigMapper(object):

    def __init__(self, path):
        self.path = self._path_verify(path)


    def __call__(self):
        db = dbdict(self.path)
        return db


    def set_ini_options(self, dictionary):
        """Maps your INI configuration keys to dictionary keys"""
        db = dbdict(self.path, table='_guachi_options') 
        for key, value in dictionary.items():
            db[key] = value 


    def set_default_options(self, dictionary):
        """Maps the default values that we can fill in if keys are empty"""
        db = dbdict(self.path, table='_guachi_defaults') 
        for key, value in dictionary.items():
            db[key] = value


    def get_ini_options(self):
        """Returns the dictionary that maps INI style options to 
        dictionary options"""
        db = dbdict(self.path, table='_guachi_options') 
        return db


    def get_default_options(self):
        """Returns the default options we hold"""
        db = dbdict(self.path, table='_guachi_defaults') 
        return db


    def set_config(self, configuration=None):
        """Accepts a dictionary or a file to set persistent configurations"""
        mapped_ini = self.get_ini_options()
        mapped_defaults = self.get_default_options()

        # First make sure that whatever we get, gets translated
        # into a dictionary 
        dict_match = DictMatch(configuration, mapped_ini, mapped_defaults)
