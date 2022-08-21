from models.status_history import StatusHistory
from db import MySqlConnection, DBHelper
import json


class StatusHistoryController:
    @classmethod
    def get_status_history_lines(cls, **kwargs):
        error = None
        response = None
        cursor = MySqlConnection.get_cursor()
        try:
            list_status_history_lines = DBHelper.get_all(cursor, StatusHistory)
            response = json.dumps(
                {
                    "msg": "Query completed successfully",
                    "data": [obj.__dict__ for obj in list_status_history_lines],
                }
            )
        except Exception as e:
            error = True
            print(e)
        finally:
            cursor.close()
        return response, error
