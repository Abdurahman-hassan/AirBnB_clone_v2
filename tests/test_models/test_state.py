"""Unit tests for the State class."""
import unittest
import os
from models.state import State
from datetime import datetime
from time import sleep

condition = os.getenv('HBNB_TYPE_STORAGE') == 'db'


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestState(unittest.TestCase):
    """Contains unit tests for the State class."""

    def test_name_class_attribute(self):
        """
        Test that the State has a class attribute 'name'
        """
        state = State()
        self.assertEqual(type(State.name), str)
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state.__dict__)

    #  State object can be instantiated with no arguments
    def test_instantiate_with_no_arguments(self):
        """
        Test that a State object can be instantiated
        with no arguments.
        """
        state = State()
        self.assertIsInstance(state, State)

    #  State object can be instantiated with name argument
    def test_instantiate_with_name_argument(self):
        """
        Test that a State object can be instantiated
        with a name argument.
        """
        state = State(name="California")
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "California")

    #  State object name can be set to an empty string
    def test_set_name_to_empty_string(self):
        """
        Test that the name of a State object can be
        set to an empty string.
        """
        state = State()
        state.name = ""
        self.assertEqual(state.name, "")

    #  State object name can be set to a string with length 128
    def test_set_name_to_string_with_length_128(self):
        """
        Test that the name of a State object can be
        set to a string with a length of 128.
        """
        state = State()
        state.name = "A" * 128
        self.assertEqual(state.name, "A" * 128)

    #  State object name can be set to a string with length greater than 128
    def test_set_name_to_string_with_length_greater_than_128(self):
        """
        Test that the name of a State object can be set to
        a string with a length greater than 128.
        """
        state = State()
        state.name = "A" * 129
        self.assertEqual(state.name, "A" * 129)


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestStateInit(unittest.TestCase):
    """Contains unit tests for the State class."""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_state_instance_no_arguments(self):
        """
        Test that a state instance can be created with no arguments
        """
        state = State()
        self.assertIsInstance(state, State)

    def test_state_args_types(self):
        """Tests the types of attributes after state instantiation"""
        obj = State()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_state_instance_keyword_arguments(self):
        """
        Test that a state instance can be created with keyword arguments
        """
        state = State(created_at='2022-01-01T00:00:00.000')
        self.assertIsInstance(state, State)
        self.assertEqual(state.created_at, datetime(2022, 1, 1, 0, 0, 0))

    def test_state_init_with_kwargs(self):
        """Tests state initialization with keyword arguments"""
        data = {'id': '415b1fec-2336-4dfa-8254-3b9006da20f1',
                'created_at': '2024-01-14T12:00:00.000'}
        obj = State(**data)

        self.assertEqual(obj.id, '415b1fec-2336-4dfa-8254-3b9006da20f1')
        self.assertEqual(obj.created_at, datetime(2024, 1, 14, 12, 0, 0))

    def test_base_moder_not_used_args(self):
        """Tests state instantiation with unused positional arguments"""
        state = State("415b1fec-2336-4dfa-8254-3b9006da20e3")

        self.assertIsInstance(state, State)
        self.assertNotEqual(state.id,
                            "415b1fec-2336-4dfa-8254-3b9006da20e3")

    def test_state_with_None(self):
        """Tests state instantiation with None as an argument"""
        state = State(None)
        self.assertIsInstance(state, State)

    def test_state_str(self):
        """Tests the string representation of state instances"""

        obj = State()
        obj.id = "415swfec-4536-4dfa-8254-3b9006da20fa"
        date = datetime.now()
        obj.created_at = obj.updated_at = date
        output = str(obj)

        self.assertIn("[State] (415swfec-4536-4dfa-8254-3b9006da20fa)",
                      output)
        self.assertIn("'id': '415swfec-4536-4dfa-8254-3b9006da20fa'", output)
        self.assertIn(f"'created_at': {repr(date)}", output)
        self.assertIn(f"'updated_at': {repr(date)}", output)

    def test_state_instance_invalid_created_at(self):
        """
        Test that a state instance cannot be created with an
        invalid created_at
        """
        with self.assertRaises(ValueError):
            State(created_at='invalid_date')


@unittest.skipIf(condition, "Reason for skipping the tests")
class TeststateSave(unittest.TestCase):
    """Contains tests related to the save method of State instances"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save_method(self):
        """Tests the save method of state instances"""
        obj = State()
        old_updated_at = obj.updated_at
        sleep(0.1)
        obj.save()
        self.assertGreater(obj.updated_at, old_updated_at)

    def test_save_two_times(self):
        """
        Tests calling the save method twice and checking
        if updated_at is greater the second time
        """
        obj = State()
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
        obj = State()
        old_updated_at = obj.updated_at
        sleep(0.1)
        with self.assertRaises(TypeError):
            obj.save(None)


@unittest.skipIf(condition, "Reason for skipping the tests")
class TeststateToDict(unittest.TestCase):
    """Contains tests related to the to_dict method of State instances"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_to_dict_method(self):
        """Tests the to_dict method of state instances"""
        obj = State()
        self.assertIsInstance(obj.to_dict(), dict)

    def test_to_dict_contents(self):
        """Tests the contents of the dictionary returned by to_dict"""
        obj = State()
        obj.id = "99283s39sn2v"
        new_dict = obj.to_dict()
        self.assertEqual(new_dict['id'], "99283s39sn2v")
        self.assertEqual(new_dict['__class__'], "State")

    def test_to_dict_with_arg(self):
        """
        Tests calling the to_dict method with an argument
        (expects a TypeError)
        """
        obj = State()
        with self.assertRaises(TypeError):
            obj.to_dict(None)
