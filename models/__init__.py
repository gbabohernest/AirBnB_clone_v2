#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
OR DBStorage, it depends on the env variable HBNB_TYPE_STORAGE"""
from os import getenv

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == "db":
    from models.engine.db_storage import DBStroage
    storage = DBStroage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
