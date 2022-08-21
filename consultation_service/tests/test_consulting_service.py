from main import Server
from db import DBHelper, MySqlConnection
from models.property import Property
from controllers.property_controller import PropertyController
from mysql.connector.errors import ProgrammingError
import unittest
import json


class ConsultingService(unittest.TestCase):

    def setUp(self) -> None:
        self.filters = {
            "city": "bogota",
            "year": 2011
        }
        self.custom_filters = [
            "city=bogota",
            "state=en_venta"
        ]
        self.expected_dict_filters = {
            "city": "bogota",
            "state": "en_venta"
        }
        self.cursor = MySqlConnection.get_cursor()

    def tearDown(self) -> None:
        self.cursor.close()

    def test_convert_filters_to_dict(self):
        result = Server.convert_filters_to_dict(self.custom_filters)
        assert result == self.expected_dict_filters

    def test_db_helper_query_all(self):
        result = DBHelper.get_all(self.cursor, Property)
        assert isinstance(result, list)
        for item in result:
            assert isinstance(item, Property)

    def test_db_helper_query_filter_bad_column(self):
        with self.assertRaises(ProgrammingError):
            DBHelper.get_by_filter(self.cursor, Property, **self.expected_dict_filters)

    def test_db_helper_query_filter(self):
        results = DBHelper.get_by_filter(self.cursor, Property, **self.filters)
        self.assertTrue(isinstance(results, list))
        for item in results:
            self.assertTrue(isinstance(item, Property))
            self.assertTrue(item.city == self.filters["city"])
            self.assertTrue(item.year == self.filters["year"])

    def test_add_actually_status(self):
        results = DBHelper.get_by_filter(self.cursor, Property, **self.filters)
        with self.assertRaises(Exception):
            for item in results:
                # Validate that state not exists
                self.assertTrue(item.status)
        PropertyController.add_actually_status(results)
        for item in results:
            self.assertTrue(item.status)

    def test_filter_by_status_valid_to_show(self):
        results = DBHelper.get_all(self.cursor, Property)
        PropertyController.add_actually_status(results)
        has_not_valid_status_to_show = False
        for item in results:
            if item.status == "comprando":
                has_not_valid_status_to_show = True
                break
        self.assertTrue(has_not_valid_status_to_show)
        results = PropertyController.filter_by_status_valid_to_show(results)
        for item in results:
            if item.status in ["comprando", "comprado"]:
                raise Exception("Status invalid to show")

    def test_get_properties(self):
        result, error = PropertyController.get_properties()
        self.assertTrue(isinstance(result, str))
        result = json.loads(result)
        self.assertTrue(
            "msg" in result.keys()
        )
        self.assertTrue(
            "count" in result.keys()
        )
        self.assertTrue(
            "data" in result.keys()
        )


