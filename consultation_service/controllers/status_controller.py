from models.status import Status
from db import MySqlConnection, DBHelper
from cachetools import cached, TTLCache
from datetime import timedelta, datetime
import json


cache = TTLCache(maxsize=100, ttl=timedelta(minutes=10), timer=datetime.now)


class StatusController:

    @classmethod
    @cached(cache)
    def get_name_status_by_id(cls, id):
        status_by_id = None
        cursor = MySqlConnection.get_cursor()
        try:
            id = int(id)
            status_by_id = DBHelper.get_by_filter(cursor, Status, **{"id": id})
            status_by_id = status_by_id[0]
            print(f"id: {id} value: {status_by_id}")
        except Exception as e:
            print(e)
        finally:
            cursor.close()
        return status_by_id[1] or ""
