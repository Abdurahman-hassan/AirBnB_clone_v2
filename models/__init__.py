#!/usr/bin/python3
"""
This script initializes an instance of the FileStorage class from the
'models.engine.file_storage' module and reloads previously stored data.
"""
from os import getenv


storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
