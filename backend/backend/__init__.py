import os

from .utils import get_db_handle

global db, client
db, client = get_db_handle()
