from models.property import Property
from db import MySqlConnection, DBHelper
import json
from controllers.status_history_controller import StatusHistoryController
from controllers.status_controller import StatusController


class PropertyController:

    @classmethod
    def get_properties(cls, **kwargs):
        error = None
        response = None
        cursor = MySqlConnection.get_cursor()
        filter_by_state = "state" in kwargs.keys()
        if filter_by_state:
            state_to_filter = kwargs["state"]
            del kwargs["state"]
        print(kwargs)
        if len(kwargs) > 0:
            list_properties = DBHelper.get_by_filter(cursor, Property, **kwargs)
        else:
            list_properties = DBHelper.get_all(cursor, Property)
        cls.add_actually_status(list_properties)
        if filter_by_state:
            list_properties = cls.filter_by_status_valid_to_show(list_properties, [state_to_filter,])
        list_properties = cls.filter_by_status_valid_to_show(list_properties)
        data_to_return = [obj.__dict__ for obj in list_properties]
        response = json.dumps(
            {
                "msg": "Query completed successfully",
                "count": len(data_to_return),
                "data": data_to_return
            }
        )
        return response, error

    @classmethod
    def add_actually_status(cls, list_properties):
        response, _ = StatusHistoryController.get_status_history_lines()
        response = json.loads(response)
        data = response["data"]
        for prop in list_properties:
            temp_prop_id = prop.id_

            def filter_property_by_id(prop, prop_id=temp_prop_id):
                return prop["property_id"] == prop_id

            temp_status_by_property = filter(filter_property_by_id, data)
            temp_status_by_property = sorted(
                temp_status_by_property, key=lambda x: x["update_date"], reverse=True
            )
            if len(temp_status_by_property) > 0:
                prop.status = StatusController.get_name_status_by_id(
                    temp_status_by_property[0]["status_id"]
                )
            else:
                prop.status = None

    @classmethod
    def filter_by_status_valid_to_show(
        cls, list_properties,
        valid_states=[
            "en_venta",
            "pre_venta",
            "vendido"
        ]
    ):
        def filter_by_states(obj, valid_states=valid_states):
            return obj.status in valid_states
        list_properties = [element for element in filter(filter_by_states, list_properties)]
        return list_properties