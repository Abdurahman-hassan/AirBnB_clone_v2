"""Unit tests for the HBNBCommand class"""
import sys
import unittest
import os
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage

condition = os.getenv('HBNB_TYPE_STORAGE') == 'db'


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestHBNBCommand(unittest.TestCase):
    """Contains unit tests for the HBNBCommand class"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_do_quit(self):
        """
        Test that the 'do_quit' method returns True when called.
        """
        cmd = HBNBCommand()
        result = cmd.do_quit("")
        self.assertTrue(result)

    def test_do_EOF(self):
        """
        Test that the 'do_EOF' method returns True when called.
        """
        cmd = HBNBCommand()
        result = cmd.do_EOF("")
        self.assertTrue(result)

    def test_emptyline(self):
        """
        Test that the 'emptyline' method does not raise any errors when called.
        """
        cmd = HBNBCommand()
        try:
            cmd.emptyline()
        except Exception as e:
            self.fail(f"emptyline raised an exception: {e}")

    def test_do_create_no_class_name(self):
        """
        Test that the 'do_create' method prints an error message
        if no class name is provided.
        """
        cmd = HBNBCommand()
        # Save a reference to the original standard output
        original_stdout = sys.stdout
        # Redirect standard output to a new StringIO object
        sys.stdout = StringIO()
        cmd.do_create("")
        # Retrieve the output from the StringIO object
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout  # Restore the original standard output
        self.assertTrue('** class name missing **' in output)

    def test_do_create_invalid_class_name(self):
        """
        Test that the 'do_create' method prints an error message
        if an invalid class name is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_create("InvalidClass")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('** class doesn\'t exist **' in output)

    def test_do_show_no_class_name(self):
        """
        Test that the 'do_show' method prints an error message
        if no class name is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_show("")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('** class name missing **' in output)

    def test_do_show_invalid_class_name(self):
        """
        Test that the 'do_show' method prints an error message
        if an invalid class name is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_show("InvalidClass")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('** class doesn\'t exist **' in output)

    def test_do_destroy_no_class_name(self):
        """
        Test that the 'do_destroy' method prints an error message
        if no class name is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_destroy("")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('** class name missing **' in output)

    def test_do_destroy_invalid_class_name(self):
        """
        Test that the 'do_destroy' method prints an error message
        if an invalid class name is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_destroy("InvalidClass")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('** class doesn\'t exist **' in output)

    def test_do_all_no_class_name(self):
        """
        Test that the 'do_all' method prints all instances
        if no class name is provided.
        """
        cmd = HBNBCommand()
        cmd.do_all("")
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_all("")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('[]' in output)

    def test_do_all_invalid_class_name(self):
        """
        Test that the 'do_all' method prints an error message
        if an invalid class name is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_all("InvalidClass")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('** class doesn\'t exist **' in output)

    def test_do_update_no_class_name(self):
        """
        Test that the 'do_update' method prints an error message
        if no class name is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_update("")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('** class name missing **' in output)

    def test_do_update_invalid_class_name(self):
        """
        Test that the 'do_update' method prints an error message
        if an invalid class name is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.do_update("InvalidClass")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('** class doesn\'t exist **' in output)

    def test_default_unknown_command(self):
        """
        Test that the 'default' method prints an error message
        if an unknown command is provided.
        """
        cmd = HBNBCommand()
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        cmd.default("UnknownCommand")
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertTrue('*** Unknown syntax: UnknownCommand' in output)

    def test_prompt(self):
        """
        Tests that the prompt is set to "(hbnb)".
        """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        """
        Tests the behavior when an empty line is entered.
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestHBNBCommandHelp(unittest.TestCase):
    """Contains unit tests for the HBNBCommand help messages."""

    def test_help_create(self):
        """
        Tests the help message for the 'create' command.
        """
        create = ("Create a new instance of a specified class.\n        "
                  "USAGE: create <class name>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(create, output.getvalue().strip())

    def test_help_quit(self):
        """
        Tests the help message for the 'quit' command.
        """
        quit = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(quit, output.getvalue().strip())

    def test_help_EOF(self):
        """
        Tests the help message for the 'EOF' command.
        """
        eof = "Signal to exit the command loop."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(eof, output.getvalue().strip())

    def test_help_all(self):
        """
        Tests the help message for the 'all' command.
        """
        all = ("List all instances or instances of a specific class.\n        "
               "USAGE: all <class name>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(all, output.getvalue().strip())

    def test_help_show(self):
        """
        Tests the help message for the 'show' command.
        """
        show = ("Display information about a specific instance.\n        "
                "USAGE: show <class name> <id>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(show, output.getvalue().strip())

    def test_help_destroy(self):
        """
        Tests the help message for the 'destroy' command.
        """
        destroy = ("Remove a specified instance.\n        "
                   "USAGE: show <class name> <id>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(destroy, output.getvalue().strip())

    def test_help_update(self):
        """
        Tests the help message for the 'update' command.
        """
        update = ("Update the attributes of a specified instance.\n        "
                  "USAGE: update <class name> <id> <attribute name> "
                  '"<attribute value>"')
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(update, output.getvalue().strip())

    def test_help_count(self):
        """
        Tests the help message for the 'count' command.
        """
        count = \
            ("Count the number of instances of a specified class.\n        "
                "USAGE: count <class name>")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(count, output.getvalue().strip())

    def test_help(self):
        """
        Tests the help message for the 'help' command.
        """
        help = ("Documented commands (type help <topic>):\n"
                "========================================\n"
                "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(help, output.getvalue().strip())


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestHBNBCommandCreate(unittest.TestCase):
    """Contains unit tests for the 'create' command in HBNBCommand."""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_class_name_missing(self):
        """Tests behavior when the class name is missing."""
        msg = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_invalid_class_name(self):
        """Tests behavior when an invalid class name is provided."""
        msg = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create invalid"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_class_unknown_syntax_default(self):
        """Tests behavior with an unknown syntax for the 'create' command."""
        msg = "*** Unknown syntax: Invalid.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Invalid.create()"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_create_objects(self):
        """Tests the successful creation of objects for various classes."""

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            id = f"BaseModel.{output.getvalue().strip()}"
            self.assertIn(id, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            id = f"User.{output.getvalue().strip()}"
            self.assertIn(id, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            id = f"State.{output.getvalue().strip()}"
            self.assertIn(id, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            id = f"City.{output.getvalue().strip()}"
            self.assertIn(id, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            id = f"Amenity.{output.getvalue().strip()}"
            self.assertIn(id, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            id = f"Place.{output.getvalue().strip()}"
            self.assertIn(id, storage.all().keys())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            id = f"Review.{output.getvalue().strip()}"
            self.assertIn(id, storage.all().keys())


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestHBNBCommandShow(unittest.TestCase):
    """Contains unit tests for the 'show' command in HBNBCommand."""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_show_class_name_missing(self):
        """Tests behavior when the class name is missing."""
        msg = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_show_invalid_class_name(self):
        """Tests behavior when an invalid class name is provided."""
        msg = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show invalid"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Invalid.show()"))
            self.assertEqual("*** Unknown syntax: Invalid.show()",
                             output.getvalue().strip())

    def test_show_id_missing(self):
        """Tests behavior when the id is missing."""
        msg = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show()"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_show_not_exist_id(self):
        """Tests behavior when the instance is not exist"""
        msg = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 12345"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.show('12345')"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_show_objects(self):
        """Tests displaying information about existing objects."""

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"BaseModel.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"show BaseModel {id}"))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"User.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"show User {id}"))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"State.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"show State {id}"))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"Review.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"show Review {id}"))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"Place.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"show Place {id}"))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"City.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"show City {id}"))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"Amenity.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"show Amenity {id}"))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

    def test_show_objects_default(self):
        """Tests displaying information using the default syntax."""

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"BaseModel.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"BaseModel.show({id})"))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"User.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"User.show({id})"))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"State.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"State.show({id})"))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"Review.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"Review.show({id})"))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"Place.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"Place.show({id})"))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"City.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"City.show({id})"))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"Amenity.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"Amenity.show({id})"))
            self.assertEqual(obj.__str__(), output.getvalue().strip())


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestHBNBCommandDestroy(unittest.TestCase):
    """Contains unit tests for the 'destroy' command in HBNBCommand."""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        FileStorage.__objects = {}

    def test_destroy_class_name_missing(self):
        """Tests behavior when the class name is missing."""
        msg = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_destroy_invalid_class_name(self):
        """Tests behavior when an invalid class name is provided."""
        msg = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy invalid"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Invalid.destroy()"))
            self.assertEqual("*** Unknown syntax: Invalid.destroy()",
                             output.getvalue().strip())

    def test_destroy_id_missing(self):
        """Tests behavior when the id is missing."""
        msg = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy()"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy()"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy()"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.destroy()"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy()"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy()"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy()"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_destroy_not_exist_id(self):
        """Tests behavior when the instance is not exist"""
        msg = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1234"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.destroy('1234')"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.destroy('1234')"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.destroy('1234')"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.destroy('1234')"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.destroy('1234')"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.destroy('1234')"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.destroy('1234')"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_destroy_objects(self):
        """Tests destroying existing objects."""

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"BaseModel.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"destroy BaseModel {id}"))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"User.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"destroy User {id}"))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"State.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"destroy State {id}"))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"Review.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"destroy Review {id}"))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"Place.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"destroy Place {id}"))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"City.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"destroy City {id}"))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"Amenity.{id}"]
            self.assertFalse(HBNBCommand().onecmd(f"destroy Amenity {id}"))
            self.assertNotIn(obj, storage.all())

    def test_destroy_objects_default(self):
        """Tests destroying objects using the default syntax."""

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"BaseModel.{id}"]
            command = f'BaseModel.destroy("{id}")'
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"User.{id}"]
            command = f'User.destroy("{id}")'
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"State.{id}"]
            command = f'State.destroy("{id}")'
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"Review.{id}"]
            command = f'Review.destroy("{id}")'
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"Place.{id}"]
            command = f'Place.destroy("{id}")'
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"City.{id}"]
            command = f'City.destroy("{id}")'
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()[f"Amenity.{id}"]
            command = f'Amenity.destroy("{id}")'
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestHBNBCommandAll(unittest.TestCase):
    """Contains unit tests for the 'all' command in HBNBCommand."""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_all_invalid_class(self):
        """Tests behavior when an invalid class is provided."""
        msg = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Imvalid"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Invalid.all()"))
            self.assertEqual("*** Unknown syntax: Invalid.all()",
                             output.getvalue().strip())

    def test_all_objects(self):
        """Tests listing objects of specific classes."""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

    def test_all_objects_default(self):
        """Tests listing objects using the default syntax."""

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestHBNBCommandUpdate(unittest.TestCase):
    """Contains unit tests for the 'update' command in HBNBCommand."""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_update_class_name_missing(self):
        """Tests behavior when the class name is missing."""
        msg = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_update_class_not_exist(self):
        """Tests behavior when the class doesn't exist."""
        msg = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Invalid"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Invalid.update()"))
            self.assertEqual("*** Unknown syntax: Invalid.update()",
                             output.getvalue().strip())

    def test_update_id_missing(self):
        """Tests behavior when the instance ID is missing."""
        msg = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.update()"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_update_id_missing(self):
        """Tests behavior when the instance ID is not found."""
        msg = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User 1234"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.update(1234)"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_update_attribute_name_missing(self):
        """Tests behavior when the attribute name is missing."""
        msg = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(f"update User {id}"))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(f"User.update('{id}')"))
            self.assertEqual(msg, output.getvalue().strip())

    def test_update_attribute_value_missing(self):
        """Tests behavior when the attribute value is missing."""
        msg = "** value missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = f"update User {id} first_name"
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(msg, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            command = f"User.update('{id}', 'first_name')"
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(msg, output.getvalue().strip())

    def test_update_objects(self):
        """Tests updating objects of different classes."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            id = output.getvalue().strip()
        command = f"update BaseModel {id} test_name 'test_value'"
        self.assertFalse(HBNBCommand().onecmd(command))
        obj_dict = storage.all()[f"BaseModel.{id}"].__dict__
        self.assertEqual(obj_dict["test_name"], "test_value")

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            id = output.getvalue().strip()
        command = f"update User {id} test_name 'test_value'"
        self.assertFalse(HBNBCommand().onecmd(command))
        obj_dict = storage.all()[f"User.{id}"].__dict__
        self.assertEqual(obj_dict["test_name"], "test_value")

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            id = output.getvalue().strip()
        command = f"update State {id} test_name 'test_value'"
        self.assertFalse(HBNBCommand().onecmd(command))
        obj_dict = storage.all()[f"State.{id}"].__dict__
        self.assertEqual(obj_dict["test_name"], "test_value")

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            id = output.getvalue().strip()
        command = f"update Review {id} test_name 'test_value'"
        self.assertFalse(HBNBCommand().onecmd(command))
        obj_dict = storage.all()[f"Review.{id}"].__dict__
        self.assertEqual(obj_dict["test_name"], "test_value")

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            id = output.getvalue().strip()
        command = f"update Place {id} test_name 'test_value'"
        self.assertFalse(HBNBCommand().onecmd(command))
        obj_dict = storage.all()[f"Place.{id}"].__dict__
        self.assertEqual(obj_dict["test_name"], "test_value")

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            id = output.getvalue().strip()
        command = f"update City {id} test_name 'test_value'"
        self.assertFalse(HBNBCommand().onecmd(command))
        obj_dict = storage.all()[f"City.{id}"].__dict__
        self.assertEqual(obj_dict["test_name"], "test_value")

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            id = output.getvalue().strip()
        command = f"update Amenity {id} test_name 'test_value'"
        self.assertFalse(HBNBCommand().onecmd(command))
        obj_dict = storage.all()[f"Amenity.{id}"].__dict__
        self.assertEqual(obj_dict["test_name"], "test_value")

    def test_update_objects_default(self):
        """Tests updating objects using the default syntax."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            id = output.getvalue().strip()
        command = f"BaseModel.update('{id}', 'test_name', 'test_value')"
        self.assertFalse(HBNBCommand().onecmd(command))
        obj_dict = storage.all()[f"BaseModel.{id}"].__dict__
        self.assertEqual(obj_dict["test_name"], "test_value")

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            id = output.getvalue().strip()
        command = f"User.update('{id}', 'test_name', 'test_value')"
        self.assertFalse(HBNBCommand().onecmd(command))
        obj_dict = storage.all()[f"User.{id}"].__dict__
        self.assertEqual(obj_dict["test_name"], "test_value")

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            id = output.getvalue().strip()
        command = f"State.update('{id}', 'test_name', 'test_value')"
        self.assertFalse(HBNBCommand().onecmd(command))
        obj_dict = storage.all()[f"State.{id}"].__dict__
        self.assertEqual(obj_dict["test_name"], "test_value")

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            id = output.getvalue().strip()
        command = f"Review.update('{id}', 'test_name', 'test_value')"
        self.assertFalse(HBNBCommand().onecmd(command))
        obj_dict = storage.all()[f"Review.{id}"].__dict__
        self.assertEqual(obj_dict["test_name"], "test_value")

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            id = output.getvalue().strip()
        command = f"Place.update('{id}', 'test_name', 'test_value')"
        self.assertFalse(HBNBCommand().onecmd(command))
        obj_dict = storage.all()[f"Place.{id}"].__dict__
        self.assertEqual(obj_dict["test_name"], "test_value")

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            id = output.getvalue().strip()
        command = f"City.update('{id}', 'test_name', 'test_value')"
        self.assertFalse(HBNBCommand().onecmd(command))
        obj_dict = storage.all()[f"City.{id}"].__dict__
        self.assertEqual(obj_dict["test_name"], "test_value")

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            id = output.getvalue().strip()
        command = f"Amenity.update('{id}', 'test_name', 'test_value')"
        self.assertFalse(HBNBCommand().onecmd(command))
        obj_dict = storage.all()[f"Amenity.{id}"].__dict__
        self.assertEqual(obj_dict["test_name"], "test_value")

    def test_update_objects_dictionary(self):
        """Tests updating objects using a dictionary as input."""

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            id = output.getvalue().strip()
        command = f"update BaseModel {id} "
        command += "{'test_name': 'test_value'}"
        HBNBCommand().onecmd(command)
        obj_dict = storage.all()[f"BaseModel.{id}"].__dict__
        self.assertEqual("test_value", obj_dict["test_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            id = output.getvalue().strip()
        command = f"update User {id} "
        command += "{'test_name': 'test_value'}"
        HBNBCommand().onecmd(command)
        obj_dict = storage.all()[f"User.{id}"].__dict__
        self.assertEqual("test_value", obj_dict["test_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            id = output.getvalue().strip()
        command = f"update State {id} "
        command += "{'test_name': 'test_value'}"
        HBNBCommand().onecmd(command)
        obj_dict = storage.all()[f"State.{id}"].__dict__
        self.assertEqual("test_value", obj_dict["test_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            id = output.getvalue().strip()
        command = f"update Review {id} "
        command += "{'test_name': 'test_value'}"
        HBNBCommand().onecmd(command)
        obj_dict = storage.all()[f"Review.{id}"].__dict__
        self.assertEqual("test_value", obj_dict["test_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            id = output.getvalue().strip()
        command = f"update Place {id} "
        command += "{'test_name': 'test_value'}"
        HBNBCommand().onecmd(command)
        obj_dict = storage.all()[f"Place.{id}"].__dict__
        self.assertEqual("test_value", obj_dict["test_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            id = output.getvalue().strip()
        command = f"update City {id} "
        command += "{'test_name': 'test_value'}"
        HBNBCommand().onecmd(command)
        obj_dict = storage.all()[f"City.{id}"].__dict__
        self.assertEqual("test_value", obj_dict["test_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            id = output.getvalue().strip()
        command = f"update Amenity {id} "
        command += "{'test_name': 'test_value'}"
        HBNBCommand().onecmd(command)
        obj_dict = storage.all()[f"Amenity.{id}"].__dict__
        self.assertEqual("test_value", obj_dict["test_name"])

    def test_update_objects_default_dictionary(self):
        """
        Tests updating objects using a dictionary
        as input with default syntax.
        """

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            id = output.getvalue().strip()
        command = f"BaseModel.update('{id}', "
        command += "{'test_name': 'test_value'})"
        HBNBCommand().onecmd(command)
        obj_dict = storage.all()[f"BaseModel.{id}"].__dict__
        self.assertEqual("test_value", obj_dict["test_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            id = output.getvalue().strip()
        command = f"User.update('{id}', "
        command += "{'test_name': 'test_value'})"
        HBNBCommand().onecmd(command)
        obj_dict = storage.all()[f"User.{id}"].__dict__
        self.assertEqual("test_value", obj_dict["test_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            id = output.getvalue().strip()
        command = f"State.update('{id}', "
        command += "{'test_name': 'test_value'})"
        HBNBCommand().onecmd(command)
        obj_dict = storage.all()[f"State.{id}"].__dict__
        self.assertEqual("test_value", obj_dict["test_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            id = output.getvalue().strip()
        command = f"Review.update('{id}', "
        command += "{'test_name': 'test_value'})"
        HBNBCommand().onecmd(command)
        obj_dict = storage.all()[f"Review.{id}"].__dict__
        self.assertEqual("test_value", obj_dict["test_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            id = output.getvalue().strip()
        command = f"Place.update('{id}', "
        command += "{'test_name': 'test_value'})"
        HBNBCommand().onecmd(command)
        obj_dict = storage.all()[f"Place.{id}"].__dict__
        self.assertEqual("test_value", obj_dict["test_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            id = output.getvalue().strip()
        command = f"City.update('{id}', "
        command += "{'test_name': 'test_value'})"
        HBNBCommand().onecmd(command)
        obj_dict = storage.all()[f"City.{id}"].__dict__
        self.assertEqual("test_value", obj_dict["test_name"])

        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            id = output.getvalue().strip()
        command = f"Amenity.update('{id}', "
        command += "{'test_name': 'test_value'})"
        HBNBCommand().onecmd(command)
        obj_dict = storage.all()[f"Amenity.{id}"].__dict__
        self.assertEqual("test_value", obj_dict["test_name"])

    def test_update_valid_object_default_int(self):
        """Tests updating an object with a default integer attribute."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            id = output.getvalue().strip()
        command = f"Place.update('{id}', "
        command += "{'max_guest': 100})"
        HBNBCommand().onecmd(command)
        obj_dict = storage.all()[f"Place.{id}"].__dict__
        self.assertEqual(100, obj_dict["max_guest"])

    def test_update_valid_object_float(self):
        """Tests updating an object with a float attribute."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            id = output.getvalue().strip()
        command = f"update Place {id} "
        command += "{'latitude': 8.5})"
        HBNBCommand().onecmd(command)
        obj_dict = storage.all()[f"Place.{id}"].__dict__
        self.assertEqual(8.5, obj_dict["latitude"])

    def test_update_valid_object_default_float(self):
        """Tests updating an object with a default float attribute."""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            id = output.getvalue().strip()
        command = f"Place.update('{id}', "
        command += "{'latitude': 8.5})"
        HBNBCommand().onecmd(command)
        obj_dict = storage.all()[f"Place.{id}"].__dict__
        self.assertEqual(8.5, obj_dict["latitude"])


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestHBNBCommandCount(unittest.TestCase):
    """Test cases for the 'count' command in HBNBCommand class."""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

        FileStorage._FileStorage__objects = {}

    def test_count_invalid_class_name(self):
        """Test that an invalid class name raises an Unknown syntax error."""

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Invalid.count()"))
            self.assertEqual("*** Unknown syntax: Invalid.count()",
                             output.getvalue().strip())

    def test_count_objects(self):
        """Test the 'count' command for various classes."""

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("1", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("1", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("1", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("1", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("1", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("1", output.getvalue().strip())
