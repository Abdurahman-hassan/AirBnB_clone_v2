"""Unit tests for the Review class."""
import os
import unittest
from datetime import datetime
from time import sleep

from models.review import Review

condition = os.getenv('HBNB_TYPE_STORAGE') == 'db'


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestReview(unittest.TestCase):
    """Contains unit tests for the Review class."""

    def test_create_review_with_required_attributes(self):
        """test_create_review_with_required_attributes tests that when a"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

    def test_create_review_with_all_attributes(self):
        """test_create_review_with_all_attributes tests that when a Review"""
        review = Review(place_id='123', user_id='456', text='test')
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, '123')
        self.assertEqual(review.user_id, '456')
        self.assertEqual(review.text, 'test')

    #  Review instance can be saved successfully
    def test_save_review_successfully(self):
        """
        test_save_review_successfully tests that when
        a Review instance is
        """
        review = Review()
        review.save()
        self.assertIsNotNone(review.updated_at)

    def test_create_review_with_empty_attributes(self):
        """test_create_review_with_empty_attributes tests that when a"""
        review = Review(place_id='', user_id='', text='')
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, '')
        self.assertEqual(review.user_id, '')
        self.assertEqual(review.text, '')

    def test_create_review_with_non_string_attributes(self):
        """test_create_review_with_non_string_attributes tests that when a"""
        review = Review(place_id=123, user_id=456, text=789)
        self.assertIsInstance(review, Review)
        self.assertNotEqual(review.place_id, '123')
        self.assertNotEqual(review.user_id, '456')
        self.assertNotEqual(review.text, '789')

    def test_create_review_with_non_existent_attributes(self):
        """test_create_review_with_non_existent_attributes tests that when a"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertFalse(hasattr(review, 'non_existent_attr'))

    def test_create_review_with_invalid_dates(self):
        """test_create_review_with_invalid_dates tests that when a Review"""
        review = Review(created_at='2021-01-01T00:00:00.000000',
                        updated_at='2022-01-01T00:00:00.000000')
        self.assertIsInstance(review, Review)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestReviewInit(unittest.TestCase):
    """Contains unit tests for the review class."""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_review_instance_no_arguments(self):
        """
        Test that a review instance can be created with no arguments
        """
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_args_types(self):
        """Tests the types of attributes after Review instantiation"""
        obj = Review()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_review_instance_keyword_arguments(self):
        """
        Test that a Review instance can be created with keyword arguments
        """
        review = Review(created_at='2022-01-01T00:00:00.000')
        self.assertIsInstance(review, Review)
        self.assertEqual(review.created_at, datetime(2022, 1, 1, 0, 0, 0))

    def test_review_init_with_kwargs(self):
        """Tests review initialization with keyword arguments"""
        data = {'id': '415b1fec-2336-4dfa-8254-3b9006da20f1',
                'created_at': '2024-01-14T12:00:00.000'}
        obj = Review(**data)

        self.assertEqual(obj.id, '415b1fec-2336-4dfa-8254-3b9006da20f1')
        self.assertEqual(obj.created_at, datetime(2024, 1, 14, 12, 0, 0))

    def test_base_moder_not_used_args(self):
        """Tests Review instantiation with unused positional arguments"""
        review = Review("415b1fec-2336-4dfa-8254-3b9006da20e3")

        self.assertIsInstance(review, Review)
        self.assertNotEqual(review.id,
                            "415b1fec-2336-4dfa-8254-3b9006da20e3")

    def test_review_with_None(self):
        """Tests Review instantiation with None as an argument"""
        review = Review(None)
        self.assertIsInstance(review, Review)

    def test_review_str(self):
        """Tests the string representation of Review instances"""

        obj = Review()
        obj.id = "415swfec-4536-4dfa-8254-3b9006da20fa"
        date = datetime.now()
        obj.created_at = obj.updated_at = date
        output = str(obj)

        self.assertIn("[Review] (415swfec-4536-4dfa-8254-3b9006da20fa)",
                      output)
        self.assertIn("'id': '415swfec-4536-4dfa-8254-3b9006da20fa'", output)
        self.assertIn(f"'created_at': {repr(date)}", output)
        self.assertIn(f"'updated_at': {repr(date)}", output)

    def test_review_instance_invalid_created_at(self):
        """
        Test that a Review instance cannot be created with an
        invalid created_at
        """
        with self.assertRaises(ValueError):
            Review(created_at='invalid_date')


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestReviewSave(unittest.TestCase):
    """Contains tests related to the save method of Review instances"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_save_method(self):
        """Tests the save method of Review instances"""
        obj = Review()
        old_updated_at = obj.updated_at
        sleep(0.1)
        obj.save()
        self.assertGreater(obj.updated_at, old_updated_at)

    def test_save_two_times(self):
        """
        Tests calling the save method twice and checking
        if updated_at is greater the second time
        """
        obj = Review()
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
        obj = Review()
        old_updated_at = obj.updated_at
        sleep(0.1)
        with self.assertRaises(TypeError):
            obj.save(None)


@unittest.skipIf(condition, "Reason for skipping the tests")
class TestReviewToDict(unittest.TestCase):
    """Contains tests related to the to_dict method of review instances"""

    def tearDown(self):
        """Delete any created files during testing."""
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_to_dict_method(self):
        """Tests the to_dict method of Review instances"""
        obj = Review()
        self.assertIsInstance(obj.to_dict(), dict)

    def test_to_dict_contents(self):
        """Tests the contents of the dictionary returned by to_dict"""
        obj = Review()
        obj.id = "99283s39sn2v"
        new_dict = obj.to_dict()
        self.assertEqual(new_dict['id'], "99283s39sn2v")
        self.assertEqual(new_dict['__class__'], "Review")

    def test_to_dict_with_arg(self):
        """
        Tests calling the to_dict method with an argument
        (expects a TypeError)
        """
        obj = Review()
        with self.assertRaises(TypeError):
            obj.to_dict(None)
