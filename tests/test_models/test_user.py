"""Unit tests for the User class."""
import os
import unittest
from datetime import datetime
from time import sleep

from models.user import User

condition = os.getenv('HBNB_TYPE_STORAGE') == 'db'


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestUser(unittest.TestCase):
    """Contains unit tests for the User class."""

    def test_user_creation_with_valid_details(self):
        """Test that a User object can be created with valid email,
         password, first name, and last name"""
        user = User(email='test@example.com', password='password',
                    first_name='John', last_name='Doe')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'password')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

    def test_user_update_and_save_to_storage(self):
        """Test that a User object can be updated and saved to storage"""
        user = User(email='test@example.com', password='password',
                    first_name='John', last_name='Doe')
        user.save()
        user.first_name = 'Jane'
        user.save()
        self.assertEqual(user.first_name, 'Jane')

    def test_user_creation_with_empty_details(self):
        """Test that a User object can be created with
        empty email, password, first name, and last name"""
        user = User()
        self.assertEqual(user.email, '')
        self.assertEqual(user.password, '')
        self.assertEqual(user.first_name, '')
        self.assertEqual(user.last_name, '')


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestUserInit(unittest.TestCase):
    """Contains unit tests for the User class."""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_user_instance_no_arguments(self):
        """
        Test that a User instance can be created with no arguments
        """
        user = User()
        self.assertIsInstance(user, User)

    def test_user_args_types(self):
        """Tests the types of attributes after User instantiation"""
        obj = User()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_user_instance_keyword_arguments(self):
        """
        Test that a User instance can be created with keyword arguments
        """
        user = User(created_at='2022-01-01T00:00:00.000')
        self.assertIsInstance(user, User)
        self.assertEqual(user.created_at, datetime(2022, 1, 1, 0, 0, 0))

    def test_user_init_with_kwargs(self):
        """Tests User initialization with keyword arguments"""
        data = {'id': '415b1fec-2336-4dfa-8254-3b9006da20f1',
                'created_at': '2024-01-14T12:00:00.000'}
        obj = User(**data)

        self.assertEqual(obj.id, '415b1fec-2336-4dfa-8254-3b9006da20f1')
        self.assertEqual(obj.created_at, datetime(2024, 1, 14, 12, 0, 0))

    def test_base_moder_not_used_args(self):
        """Tests User instantiation with unused positional arguments"""
        user = User("415b1fec-2336-4dfa-8254-3b9006da20e3")

        self.assertIsInstance(user, User)
        self.assertNotEqual(user.id,
                            "415b1fec-2336-4dfa-8254-3b9006da20e3")

    def test_user_with_None(self):
        """Tests User instantiation with None as an argument"""
        user = User(None)
        self.assertIsInstance(user, User)

    def test_user_str(self):
        """Tests the string representation of User instances"""

        obj = User()
        obj.id = "415swfec-4536-4dfa-8254-3b9006da20fa"
        date = datetime.now()
        obj.created_at = obj.updated_at = date
        output = str(obj)

        self.assertIn("[User] (415swfec-4536-4dfa-8254-3b9006da20fa)",
                      output)
        self.assertIn("'id': '415swfec-4536-4dfa-8254-3b9006da20fa'", output)
        self.assertIn(f"'created_at': {repr(date)}", output)
        self.assertIn(f"'updated_at': {repr(date)}", output)

    def test_user_instance_invalid_created_at(self):
        """
        Test that a User instance cannot be created with an
        invalid created_at
        """
        with self.assertRaises(ValueError):
            User(created_at='invalid_date')


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestUserSave(unittest.TestCase):
    """Contains tests related to the save method of User instances"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save_method(self):
        """Tests the save method of User instances"""
        obj = User()
        old_updated_at = obj.updated_at
        sleep(0.1)
        obj.save()
        self.assertGreater(obj.updated_at, old_updated_at)

    def test_save_two_times(self):
        """
        Tests calling the save method twice and checking
        if updated_at is greater the second time
        """
        obj = User()
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
        obj = User()
        old_updated_at = obj.updated_at
        sleep(0.1)
        with self.assertRaises(TypeError):
            obj.save(None)


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestUserToDict(unittest.TestCase):
    """Contains tests related to the to_dict method of User instances"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_to_dict_method(self):
        """Tests the to_dict method of User instances"""
        obj = User()
        self.assertIsInstance(obj.to_dict(), dict)

    def test_to_dict_contents(self):
        """Tests the contents of the dictionary returned by to_dict"""
        obj = User()
        obj.id = "99283s39sn2v"
        new_dict = obj.to_dict()
        self.assertEqual(new_dict['id'], "99283s39sn2v")
        self.assertEqual(new_dict['__class__'], "User")

    def test_to_dict_with_arg(self):
        """
        Tests calling the to_dict method with an argument
        (expects a TypeError)
        """
        obj = User()
        with self.assertRaises(TypeError):
            obj.to_dict(None)
