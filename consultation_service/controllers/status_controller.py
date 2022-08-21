from models.status import Status
from db import MySqlConnection, DBHelper
from cachetools import cached, TTLCache
from datetime import timedelta, datetime
import json


cache = TTLCache(maxsize=100, ttl=timedelta(minutes=10), timer=datetime.now)


class StatusController:

    @classmethod
    @cached(cache)
    def get_name_status_by_id(cls, id_):
        status_by_id = None
        cursor = MySqlConnection.get_cursor()
        try:
            id_ = int(id_)
            status_by_id = DBHelper.get_by_filter(cursor, Status, **{"id": id_})
            status_by_id = status_by_id[0]
        except Exception as e:
            print(e)
        finally:
            cursor.close()
        return status_by_id.name if status_by_id else ""
