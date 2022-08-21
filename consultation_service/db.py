from mysql import connector
import os
import random
import datetime


class MySqlConnection:
    connection = None

    @classmethod
    def get_conection_instance(cls):
        if not cls.connection or not cls.connection.is_connected():
            cls.connection = connector.connect(
                user=os.getenv("USER_DB"),
                password=os.getenv("PASSWORD_DB"),
                host=os.getenv("HOST_DB"),
                database=os.getenv("NAME_DB"),
                port=os.getenv("PORT_DB"),
            )
        return cls.connection

    @classmethod
    def get_cursor(cls):
        if not cls.connection or not cls.connection.is_connected():
            cls.get_conection_instance()
        return cls.connection.cursor(buffered=True)

    @classmethod
    def close_conection(cls):
        if cls.connection:
            cls.connection.close()
            cls.connection = None


class DBHelper:

    query_all = "select * from {0};"

    @classmethod
    def get_all(cls, cursor, entity):
        cursor.execute(cls.query_all.format(entity.db_name))
        results = cursor.fetchall()
        list_dict_results = []
        for result in results:
            list_dict_results.append(
                {
                    entity.fields[i]: result[i]
                    if not isinstance(result[i], datetime.datetime)
                    else str(result[i])
                    for i in range(len(result))
                }
            )
        list_object_to_return = [entity(**result) for result in list_dict_results]
        return list_object_to_return

    @classmethod
    def get_by_filter(cls, cursor, entity, **kwargs):
        query_sentence = cls.query_all.format(entity.db_name)
        query_sentence = query_sentence.replace(";", " ")
        count = 0
        for key, value in kwargs.items():
            if not isinstance(value, float) and not isinstance(value, int):
                value = f"'{value}'"
            if count == 0:
                query_sentence += f"where {key}={value}"
            else:
                query_sentence += f" and {key}={value}"
            count += 1
        query_sentence += ";"
        cursor.execute(query_sentence)
        results = cursor.fetchall()
        list_dict_results = []
        for result in results:
            list_dict_results.append(
                {
                    entity.fields[i]: result[i]
                    if not isinstance(result[i], datetime.datetime)
                    else str(result[i])
                    for i in range(len(result))
                }
            )
        list_object_to_return = [entity(**result) for result in list_dict_results]
        return list_object_to_return
