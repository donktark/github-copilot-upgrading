import unittest
import shutil
from os import remove, mkdir, path

from guachi.config  import DictMatch, OptionConfigurationError 

class MockDict(dict):
    pass

def create_configs():
    try:
        if path.exists('/tmp/guachi'):
            remove('/tmp/guachi')
        else:
            mkdir('/tmp/guachi')
    except Exception:
        pass

    txt = open('/tmp/guachi/conf.ini', 'w')
    text = """
[DEFAULT]
# Middleware Configuration
guachi.middleware.server_id = 2
guachi.middleware.application = secondary

# Database (Mongo)
guachi.db.host = remote.example.com
guachi.db.port = 00000

# Web Interface
guachi.web.host = web.example.com
guachi.web.port = 80

# Logging
guachi.log.level = DEBUG
guachi.log.datefmt = %H:%M:%S
guachi.log.format = %(asctime)s %(levelname)s %(name)s  %(message)s

# Cache
guachi.cache = 10
    """
    txt.write(text)
    txt.close()

    txt = open('/tmp/guachi/conf_two.ini', 'w')
    text = """
[DEFAULT]
# Middleware Configuration
guachi.middleware.application = secondary

