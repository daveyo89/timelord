import os

from .utils import get_db_handle

global db, client
db, client = get_db_handle('mongodb', 'mongodb', 27017, os.getenv('MONGO_INITDB_ROOT_USERNAME'),
                           os.getenv('MONGO_INITDB_ROOT_PASSWORD'))
