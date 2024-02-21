"""Unit tests for the Place class."""
import os
import unittest
from datetime import datetime
from time import sleep

from models.place import Place

condition = os.getenv('HBNB_TYPE_STORAGE') == 'db'


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestPlace(unittest.TestCase):
    """Contains unit tests for the Place class."""

    def test_create_place_with_all_attributes(self):
        """
        test_create_place_with_all_attributes tests that
        when a Place object is
        """
        place = Place(city_id='123', user_id='456', name='Test Place',
                      description='This is a test place',
                      number_rooms=2, number_bathrooms=1, max_guest=4,
                      price_by_night=100.0, latitude=37.7749,
                      longitude=-122.4194, amenity_ids=['wifi', 'pool'])
        self.assertEqual(place.city_id, '123')
        self.assertEqual(place.user_id, '456')
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.description, 'This is a test place')
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100.0)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ['wifi', 'pool'])

    def test_update_and_save_place(self):
        """
        test_update_and_save_place tests that when a Place object is
        updated and saved the updated_at attribute is updated
        """
        place = Place()
        place.city_id = '123'
        place.user_id = '456'
        place.name = 'Test Place'
        place.description = 'This is a test place'
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100.0
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ['wifi', 'pool']
        place.save()

        self.assertEqual(place.city_id, '123')
        self.assertEqual(place.user_id, '456')
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.description, 'This is a test place')
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100.0)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ['wifi', 'pool'])

    #  Place object attributes can be accessed and modified
    def test_access_and_modify_attributes(self):
        place = Place()
        place.city_id = '123'
        place.user_id = '456'
        place.name = 'Test Place'
        place.description = 'This is a test place'
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100.0
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ['wifi', 'pool']

        self.assertEqual(place.city_id, '123')
        self.assertEqual(place.user_id, '456')
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.description, 'This is a test place')
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100.0)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ['wifi', 'pool'])

        place.city_id = '789'
        place.user_id = '012'
        place.name = 'Modified Place'
        place.description = 'This is a modified place'
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 200.0
        place.latitude = 37.7748
        place.longitude = -122.4195
        place.amenity_ids = ['wifi', 'pool', 'gym']

        self.assertEqual(place.city_id, '789')
        self.assertEqual(place.user_id, '012')
        self.assertEqual(place.name, 'Modified Place')
        self.assertEqual(place.description, 'This is a modified place')
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 200.0)
        self.assertEqual(place.latitude, 37.7748)
        self.assertEqual(place.longitude, -122.4195)
        self.assertEqual(place.amenity_ids, ['wifi', 'pool', 'gym'])

    def test_create_place_with_minimum_attributes(self):
        """
        test_create_place_with_minimum_attributes tests that
        when a Place object is
        """
        place = Place(city_id='123', user_id='456', name='Test Place')

        self.assertEqual(place.city_id, '123')
        self.assertEqual(place.user_id, '456')
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.description, '')
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_create_place_with_maximum_attributes(self):
        """
        test_create_place_with_maximum_attributes tests that when
        a Place object is
        """
        place = Place(city_id='123', user_id='456', name='Test Place',
                      description='This is a test place',
                      number_rooms=1000000, number_bathrooms=1000000,
                      max_guest=1000000, price_by_night=1000000.0,
                      latitude=90.0, longitude=180.0,
                      amenity_ids=['wifi'] * 1000000)

        self.assertEqual(place.city_id, '123')
        self.assertEqual(place.user_id, '456')
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.description, 'This is a test place')
        self.assertEqual(place.number_rooms, 1000000)
        self.assertEqual(place.number_bathrooms, 1000000)
        self.assertEqual(place.max_guest, 1000000)
        self.assertEqual(place.price_by_night, 1000000.0)
        self.assertEqual(place.latitude, 90.0)
        self.assertEqual(place.longitude, 180.0)
        self.assertEqual(place.amenity_ids, ['wifi'] * 1000000)

    def test_create_place_with_empty_string_attributes(self):
        """
        test_create_place_with_empty_string_attributes tests that
        when a Place object is
        """
        place = Place(city_id='', user_id='', name='', description='')

        self.assertEqual(place.city_id, '')
        self.assertEqual(place.user_id, '')
        self.assertEqual(place.name, '')
        self.assertEqual(place.description, '')
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_create_place_with_integer_values_for_float_attributes(self):
        """
        test_create_place_with_integer_values_for_float_attributes
        tests that when a Place
        """
        place = Place(price_by_night=100, latitude=37, longitude=-122)

        self.assertEqual(place.price_by_night, 100.0)
        self.assertEqual(place.latitude, 37.0)
        self.assertEqual(place.longitude, -122.0)

    def test_create_place_with_non_ascii_characters(self):
        """
        test_create_place_with_non_ascii_characters tests that
        when a Place object is
        """
        place = Place(name='Café')

        self.assertEqual(place.name, 'Café')


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestPlaceInit(unittest.TestCase):
    """Contains unit tests for the Place class."""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_Place_instance_no_arguments(self):
        """
        Test that a Place instance can be created with no arguments
        """
        place = Place()
        self.assertIsInstance(place, Place)

    def test_Place_args_types(self):
        """Tests the types of attributes after Place instantiation"""
        obj = Place()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_Place_instance_keyword_arguments(self):
        """
        Test that a Place instance can be created with keyword arguments
        """
        place = Place(created_at='2022-01-01T00:00:00.000')
        self.assertIsInstance(place, Place)
        self.assertEqual(place.created_at, datetime(2022, 1, 1, 0, 0, 0))

    def test_Place_init_with_kwargs(self):
        """Tests Place initialization with keyword arguments"""
        data = {'id': '415b1fec-2336-4dfa-8254-3b9006da20f1',
                'created_at': '2024-01-14T12:00:00.000'}
        obj = Place(**data)

        self.assertEqual(obj.id, '415b1fec-2336-4dfa-8254-3b9006da20f1')
        self.assertEqual(obj.created_at, datetime(2024, 1, 14, 12, 0, 0))

    def test_base_moder_not_used_args(self):
        """Tests Place instantiation with unused positional arguments"""
        place = Place("415b1fec-2336-4dfa-8254-3b9006da20e3")

        self.assertIsInstance(place, Place)
        self.assertNotEqual(place.id,
                            "415b1fec-2336-4dfa-8254-3b9006da20e3")

    def test_Place_with_None(self):
        """Tests Place instantiation with None as an argument"""
        place = Place(None)
        self.assertIsInstance(place, Place)

    def test_Place_str(self):
        """Tests the string representation of Place instances"""

        obj = Place()
        obj.id = "415swfec-4536-4dfa-8254-3b9006da20fa"
        date = datetime.now()
        obj.created_at = obj.updated_at = date
        output = str(obj)

        self.assertIn("[Place] (415swfec-4536-4dfa-8254-3b9006da20fa)",
                      output)
        self.assertIn("'id': '415swfec-4536-4dfa-8254-3b9006da20fa'", output)
        self.assertIn(f"'created_at': {repr(date)}", output)
        self.assertIn(f"'updated_at': {repr(date)}", output)

    def test_Place_instance_invalid_created_at(self):
        """
        Test that a Place instance cannot be created with an
        invalid created_at
        """
        with self.assertRaises(ValueError):
            Place(created_at='invalid_date')


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestPlaceSave(unittest.TestCase):
    """Contains tests related to the save method of Place instances"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save_method(self):
        """Tests the save method of Place instances"""
        obj = Place()
        old_updated_at = obj.updated_at
        sleep(0.1)
        obj.save()
        self.assertGreater(obj.updated_at, old_updated_at)

    def test_save_two_times(self):
        """
        Tests calling the save method twice and checking
        if updated_at is greater the second time
        """
        obj = Place()
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
        obj = Place()
        old_updated_at = obj.updated_at
        sleep(0.1)
        with self.assertRaises(TypeError):
            obj.save(None)


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestPlaceToDict(unittest.TestCase):
    """Contains tests related to the to_dict method of Place instances"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_to_dict_method(self):
        """Tests the to_dict method of Place instances"""
        obj = Place()
        self.assertIsInstance(obj.to_dict(), dict)

    def test_to_dict_contents(self):
        """Tests the contents of the dictionary returned by to_dict"""
        obj = Place()
        obj.id = "99283s39sn2v"
        new_dict = obj.to_dict()
        self.assertEqual(new_dict['id'], "99283s39sn2v")
        self.assertEqual(new_dict['__class__'], "Place")

    def test_to_dict_with_arg(self):
        """
        Tests calling the to_dict method with an argument
        (expects a TypeError)
        """
        obj = Place()
        with self.assertRaises(TypeError):
            obj.to_dict(None)
