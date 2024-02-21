"""Unit tests for the BaseModel class."""
import os
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel
from models import storage

# Add a condition to skip the tests of file storage
# if the environment variable is set to 'db'
condition = os.getenv('HBNB_TYPE_STORAGE') == 'db'


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestBaseModelInit(unittest.TestCase):
    """Contains unit tests for the BaseModel class."""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_base_model_instance_no_arguments(self):
        """
        Test that a BaseModel instance can be created with no arguments
        """
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        self.assertEqual(type(BaseModel()), BaseModel)

    def test_base_models_args_types(self):
        """Tests the types of attributes after BaseModel instantiation"""
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertEqual(type(obj.id), str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertEqual(type(obj.created_at), datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(type(obj.updated_at), datetime)

    def test_base_model_instance_exist_in_storage(self):
        """
        Tests that a BaseModel instance exists in the storage
        after instantiation.
        """
        self.assertIn(BaseModel(), storage.all().values())

    def test_base_model_id(self):
        """
        Tests that the 'id' attribute of different BaseModel
        instances is not equal.
        """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_base_model_instance_keyword_arguments(self):
        """
        Test that a BaseModel instance can be created with keyword arguments
        """
        base_model = BaseModel(created_at='2022-01-01T00:00:00.000')
        self.assertIsInstance(base_model, BaseModel)
        self.assertEqual(base_model.created_at, datetime(2022, 1, 1, 0, 0, 0))

    def test_base_model_init_with_kwargs(self):
        """Tests BaseModel initialization with keyword arguments"""
        data = {'id': '415b1fec-2336-4dfa-8254-3b9006da20f1',
                'created_at': '2024-01-14T12:00:00.000', 'name': 'ALX'}
        obj = BaseModel(**data)

        self.assertEqual(obj.id, '415b1fec-2336-4dfa-8254-3b9006da20f1')
        self.assertEqual(obj.created_at, datetime(2024, 1, 14, 12, 0, 0))
        self.assertEqual(obj.name, 'ALX')

    def test_base_model_init_with_kwargs_from_object(self):
        """
        Tests initializing a BaseModel instance with kwargs
        obtained from another BaseModel instance.
        """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertFalse(my_model is my_new_model)

    def test_base_moder_not_used_args(self):
        """Tests BaseModel instantiation with unused positional arguments"""
        base_model = BaseModel("415b1fec-2336-4dfa-8254-3b9006da20e3")

        self.assertIsInstance(base_model, BaseModel)
        self.assertNotEqual(base_model.id,
                            "415b1fec-2336-4dfa-8254-3b9006da20e3")

    def test_base_moder_with_None(self):
        """Tests BaseModel instantiation with None as an argument"""
        base_model = BaseModel(None)
        self.assertIsInstance(base_model, BaseModel)

    def test_base_model_str(self):
        """Tests the string representation of BaseModel instances"""

        obj = BaseModel()
        obj.id = "415swfec-4536-4dfa-8254-3b9006da20fa"
        date = datetime.now()
        obj.created_at = obj.updated_at = date
        obj.name = 'ALX'
        output = str(obj)

        self.assertIn("[BaseModel] (415swfec-4536-4dfa-8254-3b9006da20fa)",
                      output)
        self.assertIn("'id': '415swfec-4536-4dfa-8254-3b9006da20fa'", output)
        self.assertIn(f"'created_at': {repr(date)}", output)
        self.assertIn(f"'updated_at': {repr(date)}", output)
        self.assertIn("'name': 'ALX'", output)

    def test_base_model_instance_invalid_created_at(self):
        """
        Test that a BaseModel instance cannot be created with an
        invalid created_at
        """
        with self.assertRaises(ValueError):
            BaseModel(created_at='invalid_date')


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestBaseModelSave(unittest.TestCase):
    """Contains tests related to the save method of BaseModel instances"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save_method(self):
        """Tests the save method of BaseModel instances"""
        obj = BaseModel()
        sleep(0.1)
        old_updated_at = obj.updated_at
        obj.save()
        self.assertLess(old_updated_at, obj.updated_at)

    def test_save_two_times(self):
        """
        Tests calling the save method twice and checking
        if updated_at is greater the second time
        """
        obj = BaseModel()
        sleep(0.1)
        first_updated_at = obj.updated_at
        obj.save()
        second_updated_at = obj.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.1)
        obj.save()
        self.assertLess(second_updated_at, obj.updated_at)

    def test_save_file(self):
        """Test 'save' method saves an object to a file"""
        base = BaseModel()
        base.save()
        base_id = "BaseModel." + base.id
        with open("file.json", "r") as json_file:
            self.assertIn(base_id, json_file.read())

    def test_save_with_arg(self):
        """
        Tests calling the save method with an argument
        (expects a TypeError).
        """
        obj = BaseModel()
        old_updated_at = obj.updated_at
        sleep(0.1)
        with self.assertRaises(TypeError):
            obj.save(None)


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestBaseModelToDict(unittest.TestCase):
    """Contains tests related to the to_dict method of BaseModel instances"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_to_dict_method(self):
        """Tests the to_dict method of BaseModel instances"""
        obj = BaseModel()
        self.assertEqual(type(obj.to_dict()), dict)

    def test_to_dict_contents(self):
        """Tests the contents of the dictionary returned by to_dict"""
        obj = BaseModel()
        obj.id = "99283s39sn2v"
        new_dict = obj.to_dict()
        self.assertEqual(new_dict['id'], "99283s39sn2v")
        self.assertEqual(new_dict['__class__'], "BaseModel")

    def test_to_dict_with_arg(self):
        """
        Tests calling the to_dict method with an argument
        (expects a TypeError)
        """
        obj = BaseModel()
        with self.assertRaises(TypeError):
            obj.to_dict(None)
