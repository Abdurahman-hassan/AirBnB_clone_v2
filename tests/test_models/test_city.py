"""Unit tests for the City class."""
import unittest
import os

from models.city import City
from datetime import datetime
from time import sleep

# Add a condition to skip the tests of file storage
# if the environment variable is set to 'db'
condition = os.getenv('HBNB_TYPE_STORAGE') == 'db'


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestCity(unittest.TestCase):
    """Contains unit tests for the City class."""

    def test_city_instance_with_state_id_and_name_attributes(self):
        """
        Test that a City instance can be created with state_id and
        name attributes
        """
        city = City(state_id="CA", name="San Francisco")
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

    def test_city_instance_without_state_id_and_name_attributes(self):
        """
        Test that a City instance can be created without state_id and
        name attributes
        """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_instance_with_non_string_state_id_and_name_attributes(self):
        """
        Test that a City instance can be created with non-string state_id and
        name attributes
        """
        city = City(state_id=123, name=456)
        self.assertEqual(city.state_id, 123)
        self.assertEqual(city.name, 456)

    def test_city_instance_with_empty_state_id_and_name_attributes(self):
        """
        Test that a City instance can be created with empty state_id and
        name attributes
        """
        city = City(state_id="", name="")
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestCityInit(unittest.TestCase):
    """Contains unit tests for the City class."""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_City_instance_no_arguments(self):
        """
        Test that a City instance can be created with no arguments
        """
        city = City()
        self.assertIsInstance(city, City)

    def test_City_args_types(self):
        """Tests the types of attributes after City instantiation"""
        obj = City()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_City_instance_keyword_arguments(self):
        """
        Test that a City instance can be created with keyword arguments
        """
        city = City(created_at='2022-01-01T00:00:00.000')
        self.assertIsInstance(city, City)
        self.assertEqual(city.created_at, datetime(2022, 1, 1, 0, 0, 0))

    def test_City_init_with_kwargs(self):
        """Tests City initialization with keyword arguments"""
        data = {'id': '415b1fec-2336-4dfa-8254-3b9006da20f1',
                'created_at': '2024-01-14T12:00:00.000'}
        obj = City(**data)

        self.assertEqual(obj.id, '415b1fec-2336-4dfa-8254-3b9006da20f1')
        self.assertEqual(obj.created_at, datetime(2024, 1, 14, 12, 0, 0))

    def test_base_moder_not_used_args(self):
        """Tests City instantiation with unused positional arguments"""
        city = City("415b1fec-2336-4dfa-8254-3b9006da20e3")

        self.assertIsInstance(city, City)
        self.assertNotEqual(city.id,
                            "415b1fec-2336-4dfa-8254-3b9006da20e3")

    def test_City_with_None(self):
        """Tests City instantiation with None as an argument"""
        city = City(None)
        self.assertIsInstance(city, City)

    def test_City_str(self):
        """Tests the string representation of City instances"""

        obj = City()
        obj.id = "415swfec-4536-4dfa-8254-3b9006da20fa"
        date = datetime.now()
        obj.created_at = obj.updated_at = date
        output = str(obj)

        self.assertIn("[City] (415swfec-4536-4dfa-8254-3b9006da20fa)",
                      output)
        self.assertIn("'id': '415swfec-4536-4dfa-8254-3b9006da20fa'", output)
        self.assertIn(f"'created_at': {repr(date)}", output)
        self.assertIn(f"'updated_at': {repr(date)}", output)

    def test_City_instance_invalid_created_at(self):
        """
        Test that a City instance cannot be created with an
        invalid created_at
        """
        with self.assertRaises(ValueError):
            City(created_at='invalid_date')


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestCitySave(unittest.TestCase):
    """Contains tests related to the save method of City instances"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save_method(self):
        """Tests the save method of City instances"""
        obj = City()
        old_updated_at = obj.updated_at
        sleep(0.1)
        obj.save()
        self.assertGreater(obj.updated_at, old_updated_at)

    def test_save_two_times(self):
        """
        Tests calling the save method twice and checking
        if updated_at is greater the second time
        """
        obj = City()
        sleep(0.1)
        first_updated_at = obj.updated_at
        obj.save()
        sleep(0.1)
        obj.save()
        second_updated_at = obj.updated_at
        self.assertGreater(second_updated_at, first_updated_at)

    def test_save_with_arg(self):
        """
        Tests calling the save method with an argument
        (expects a TypeError).
        """
        obj = City()
        old_updated_at = obj.updated_at
        sleep(0.1)
        with self.assertRaises(TypeError):
            obj.save(None)


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestCityToDict(unittest.TestCase):
    """Contains tests related to the to_dict method of City instances"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_to_dict_method(self):
        """Tests the to_dict method of City instances"""
        obj = City()
        self.assertIsInstance(obj.to_dict(), dict)

    def test_to_dict_contents(self):
        """Tests the contents of the dictionary returned by to_dict"""
        obj = City()
        obj.id = "99283s39sn2v"
        new_dict = obj.to_dict()
        self.assertEqual(new_dict['id'], "99283s39sn2v")
        self.assertEqual(new_dict['__class__'], "City")

    def test_to_dict_with_arg(self):
        """
        Tests calling the to_dict method with an argument
        (expects a TypeError)
        """
        obj = City()
        with self.assertRaises(TypeError):
            obj.to_dict(None)
