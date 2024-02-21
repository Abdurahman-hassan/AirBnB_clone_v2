"""Unit tests for the Amenity class."""
import unittest
import os
from models.amenity import Amenity
from datetime import datetime
from time import sleep

# Add a condition to skip the tests of file storage
# if the environment variable is set to 'db'
condition = os.getenv('HBNB_TYPE_STORAGE') == 'db'


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestAmenity(unittest.TestCase):
    """Contains unit tests for the Amenity class."""

    def test_amenity_instance_with_name_attribute(self):
        """
        Test that an Amenity instance can be created with a name attribute
        """
        amenity = Amenity(name="Sw")
        self.assertEqual(amenity.name, "Sw")

    def test_amenity_instance_without_name_attribute(self):
        """
        Test that an Amenity instance can be created without a name attribute
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_instance_with_non_string_name_attribute(self):
        """
        Test that an Amenity instance can be created with a non-string
        name attribute
        """
        amenity = Amenity(name=123)
        self.assertEqual(amenity.name, 123)


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestAmenityInit(unittest.TestCase):
    """Contains unit tests for the Amenity class."""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_Amenity_instance_no_arguments(self):
        """
        Test that a Amenity instance can be created with no arguments
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_Amenity_args_types(self):
        """Tests the types of attributes after Amenity instantiation"""
        obj = Amenity()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_Amenity_instance_keyword_arguments(self):
        """
        Test that a Amenity instance can be created with keyword arguments
        """
        amenity = Amenity(created_at='2022-01-01T00:00:00.000')
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.created_at, datetime(2022, 1, 1, 0, 0, 0))

    def test_Amenity_init_with_kwargs(self):
        """Tests Amenity initialization with keyword arguments"""
        data = {'id': '415b1fec-2336-4dfa-8254-3b9006da20f1',
                'created_at': '2024-01-14T12:00:00.000'}
        obj = Amenity(**data)

        self.assertEqual(obj.id, '415b1fec-2336-4dfa-8254-3b9006da20f1')
        self.assertEqual(obj.created_at, datetime(2024, 1, 14, 12, 0, 0))

    def test_base_moder_not_used_args(self):
        """Tests Amenity instantiation with unused positional arguments"""
        amenity = Amenity("415b1fec-2336-4dfa-8254-3b9006da20e3")

        self.assertIsInstance(amenity, Amenity)
        self.assertNotEqual(amenity.id,
                            "415b1fec-2336-4dfa-8254-3b9006da20e3")

    def test_Amenity_with_None(self):
        """Tests Amenity instantiation with None as an argument"""
        amenity = Amenity(None)
        self.assertIsInstance(amenity, Amenity)

    def test_Amenity_str(self):
        """Tests the string representation of Amenity instances"""

        obj = Amenity()
        obj.id = "415swfec-4536-4dfa-8254-3b9006da20fa"
        date = datetime.now()
        obj.created_at = obj.updated_at = date
        output = str(obj)

        self.assertIn("[Amenity] (415swfec-4536-4dfa-8254-3b9006da20fa)",
                      output)
        self.assertIn("'id': '415swfec-4536-4dfa-8254-3b9006da20fa'", output)
        self.assertIn(f"'created_at': {repr(date)}", output)
        self.assertIn(f"'updated_at': {repr(date)}", output)

    def test_Amenity_instance_invalid_created_at(self):
        """
        Test that a Amenity instance cannot be created with an
        invalid created_at
        """
        with self.assertRaises(ValueError):
            Amenity(created_at='invalid_date')


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestAmenitySave(unittest.TestCase):
    """Contains tests related to the save method of Amenity instances"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save_method(self):
        """Tests the save method of Amenity instances"""
        obj = Amenity()
        old_updated_at = obj.updated_at
        sleep(0.1)
        obj.save()
        self.assertGreater(obj.updated_at, old_updated_at)

    def test_save_two_times(self):
        """
        Tests calling the save method twice and checking
        if updated_at is greater the second time
        """
        obj = Amenity()
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
        obj = Amenity()
        old_updated_at = obj.updated_at
        sleep(0.1)
        with self.assertRaises(TypeError):
            obj.save(None)


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestAmenityToDict(unittest.TestCase):
    """Contains tests related to the to_dict method of Amenity instances"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_to_dict_method(self):
        """Tests the to_dict method of Amenity instances"""
        obj = Amenity()
        self.assertIsInstance(obj.to_dict(), dict)

    def test_to_dict_contents(self):
        """Tests the contents of the dictionary returned by to_dict"""
        obj = Amenity()
        obj.id = "99283s39sn2v"
        new_dict = obj.to_dict()
        self.assertEqual(new_dict['id'], "99283s39sn2v")
        self.assertEqual(new_dict['__class__'], "Amenity")

    def test_to_dict_with_arg(self):
        """
        Tests calling the to_dict method with an argument
        (expects a TypeError)
        """
        obj = Amenity()
        with self.assertRaises(TypeError):
            obj.to_dict(None)
