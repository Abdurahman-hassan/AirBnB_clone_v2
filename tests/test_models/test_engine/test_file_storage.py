"""Unit tests for the FileStorage class."""
import os
import unittest
from unittest.mock import patch
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.engine.file_storage import get_class_name_to_class

# Add a condition to skip the tests of file storage
# if the environment variable is set to 'db'
condition = os.getenv('HBNB_TYPE_STORAGE') != 'db'


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestFileStorage(unittest.TestCase):
    """Contains unit tests for the FileStorage class."""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

        FileStorage._FileStorage__objects = {}

    def test_create_instance(self):
        """
        Test that a new instance of FileStorage can be created.
        """
        file_storage = FileStorage()
        self.assertIsInstance(file_storage, FileStorage)
        self.assertEqual(FileStorage, type(storage))

    def test_FileStorage_file_path_private_var(self):
        """
        Test that the __file_path attribute of FileStorage
        is a private variable of type string.
        """
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_private_var(self):
        """
        Test that the __objects attribute of FileStorage
        is a private variable of type dictionary.
        """
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all_method_returns_dict(self):
        """Tests that the 'all' method returns a dictionary."""
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(type(storage.all()), dict)

    def test_add_object(self):
        """
        Test that a new object can be added to the __objects
        dictionary using the new method.
        """
        # Use an instance of a class derived from BaseModel
        obj = BaseModel()
        storage.new(obj)
        self.assertIn(obj, storage.all().values())
        self.assertIn(f"helloThisisWorng.{obj.id}", storage.all().keys())

    def test_new_method_and_get_class_method(self):
        """Tests the 'new' method and 'get_class_name_to_class' function."""
        class_dict = get_class_name_to_class()
        all_objects = storage.all()
        obj = class_dict['User']()
        obj_name = f'{obj.__class__.__name__}.{obj.id}'
        storage.new(obj)
        self.assertIn(obj_name, all_objects)
        file_storage = FileStorage()
        self.assertIn(obj, file_storage.all().values())
        self.assertIn(f"User.{obj.id}", file_storage.all().keys())

    def test_new_method_for_state_class(self):
        """Tests the 'new' method for the State class."""
        class_dict = get_class_name_to_class()
        all_objects = storage.all()
        obj = class_dict['State']()
        obj_name = f'{obj.__class__.__name__}.{obj.id}'
        storage.new(obj)
        self.assertIn(obj_name, all_objects)
        file_storage = FileStorage()
        self.assertIn(obj, file_storage.all().values())
        self.assertIn(f"State.{obj.id}", file_storage.all().keys())

    def test_new_method_for_city_class(self):
        """Tests the 'new' method for the City class."""
        class_dict = get_class_name_to_class()
        all_objects = storage.all()
        obj = class_dict['City']()
        obj_name = f'{obj.__class__.__name__}.{obj.id}'
        storage.new(obj)
        self.assertIn(obj_name, all_objects)
        file_storage = FileStorage()
        self.assertIn(obj, file_storage.all().values())
        self.assertIn(f"City.{obj.id}", file_storage.all().keys())

    def test_new_method_for_amenity_class(self):
        """Tests the 'new' method for the Amenity class."""
        class_dict = get_class_name_to_class()
        all_objects = storage.all()
        obj = class_dict['Amenity']()
        obj_name = f'{obj.__class__.__name__}.{obj.id}'
        storage.new(obj)
        self.assertIn(obj_name, all_objects)
        file_storage = FileStorage()
        self.assertIn(obj, file_storage.all().values())
        self.assertIn(f"Amenity.{obj.id}", file_storage.all().keys())

    def test_new_method_for_place_class(self):
        """Tests the 'new' method for the Place class."""
        class_dict = get_class_name_to_class()
        all_objects = storage.all()
        obj = class_dict['Place']()
        obj_name = f'{obj.__class__.__name__}.{obj.id}'
        storage.new(obj)
        self.assertIn(obj_name, all_objects)
        file_storage = FileStorage()
        self.assertIn(obj, file_storage.all().values())
        self.assertIn(f"Place.{obj.id}", file_storage.all().keys())

    def test_new_method_for_review_class(self):
        """Tests the 'new' method for the Review class."""
        class_dict = get_class_name_to_class()
        all_objects = storage.all()
        obj = class_dict['Review']()
        obj_name = f'{obj.__class__.__name__}.{obj.id}'
        storage.new(obj)
        self.assertIn(obj_name, all_objects)
        file_storage = FileStorage()
        self.assertIn(obj, file_storage.all().values())
        self.assertIn(f"Review.{obj.id}", file_storage.all().keys())

    def test_save_method_creates_json_file(self):
        """
        Tests that the 'save' method creates a JSON file
        with object information.
        """
        class_dict = get_class_name_to_class()
        base = BaseModel()
        user = class_dict['User']()
        state = class_dict['State']()
        review = class_dict['Review']()
        place = class_dict['Place']()
        city = class_dict['City']()
        amenity = class_dict['Amenity']()
        file_storage = FileStorage()

        file_storage.new(base)
        file_storage.new(user)
        file_storage.new(state)
        file_storage.new(review)
        file_storage.new(place)
        file_storage.new(city)
        file_storage.new(amenity)
        file_storage.save()
        storage.save()

        with open("file.json", "r") as file:
            content = file.read()
            self.assertIn(f'BaseModel.{base.id}', content)
            self.assertIn(f'User.{user.id}', content)
            self.assertIn(f'State.{state.id}', content)
            self.assertIn(f'Review.{review.id}', content)
            self.assertIn(f'Place.{place.id}', content)
            self.assertIn(f'City.{city.id}', content)
            self.assertIn(f'Amenity.{amenity.id}', content)

    def test_reload_method_loads_objects(self):
        """Tests that the 'reload' method loads objects from the JSON file."""
        class_dict = get_class_name_to_class()
        base = BaseModel()
        user = class_dict['User']()
        state = class_dict['State']()
        review = class_dict['Review']()
        place = class_dict['Place']()
        city = class_dict['City']()
        amenity = class_dict['Amenity']()

        storage.new(base)
        storage.new(user)
        storage.new(state)
        storage.new(review)
        storage.new(place)
        storage.new(city)
        storage.new(amenity)
        storage.save()
        storage.reload()

        objs = FileStorage._FileStorage__objects

        self.assertIn(f'BaseModel.{base.id}', objs)
        self.assertIn(f'User.{user.id}', objs)
        self.assertIn(f'State.{state.id}', objs)
        self.assertIn(f'Review.{review.id}', objs)
        self.assertIn(f'Place.{place.id}', objs)
        self.assertIn(f'City.{city.id}', objs)
        self.assertIn(f'Amenity.{amenity.id}', objs)

    def test_all_method_with_arg(self):
        """Tests that the 'all' method raises a TypeError with an argument."""
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_save_method_with_arg(self):
        """Tests that the 'save' method raises a TypeError with an argument."""
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload_method_with_arg(self):
        """
        Tests that the 'reload' method raises
        a TypeError with an argument.
        """
        with self.assertRaises(TypeError):
            storage.reload(None)

    def test_new_method_with_two_args(self):
        """
        Tests that the 'new' method raises
        a TypeError with two arguments.
        """
        obj = BaseModel
        with self.assertRaises(TypeError):
            storage.new(obj, None)

    def test_reload_file_not_found(self):
        """
        Tests that the 'reload' method handles
        FileNotFound error gracefully.
        """
        # No exception should be raised,
        # and the method should return without errors

        try:
            storage.reload()
        except FileNotFoundError:
            self.fail()

        with patch('builtins.open', side_effect=FileNotFoundError()):
            storage.reload()
