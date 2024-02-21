#!/usr/bin/python3
"""This module defines and runs a series of unit tests for the models.
DBStorage class, which is responsible for managing the database storage
in the project."""

import unittest
import models
from models import storage_type
from models.engine.db_storage import DBStorage
from models.base_model import Base, BaseModel
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import sessionmaker
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import MySQLdb


@unittest.skipIf((storage_type != 'db'), "Testing FileStorage Engine")
class TestDBStorage(unittest.TestCase):
    """
    TestDBStorage class definition.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the class for testing.
        """

        if storage_type == 'db':
            cls.db_storage = DBStorage()
            Base.metadata.create_all(cls.db_storage._DBStorage__engine)
            Session = sessionmaker(bind=cls.db_storage._DBStorage__engine,
                                   expire_on_commit=False)
            cls.db_storage._DBStorage__session = Session()

            cls.state = State(name="California")
            cls.db_storage._DBStorage__session.add(cls.state)

            cls.city = City(name="San Francisco", state_id=cls.state.id)
            cls.db_storage._DBStorage__session.add(cls.city)

            cls.user = User(email="gui@hbtn.io", password="guipwd")
            cls.db_storage._DBStorage__session.add(cls.user)

            cls.place = Place(city_id=cls.city.id, user_id=cls.user.id,
                              name="Lovely_place")
            cls.db_storage._DBStorage__session.add(cls.place)

            cls.amenity = Amenity(name="Oven")
            cls.db_storage._DBStorage__session.add(cls.amenity)

            cls.review = Review(place_id=cls.place.id, user_id=cls.user.id,
                                text="Amazing_place,_huge_kitchen")
            cls.db_storage._DBStorage__session.add(cls.review)

            cls.db_storage._DBStorage__session.commit()

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the class after testing.
        """
        if storage_type == 'db':
            cls.db_storage._DBStorage__session.close()
            Base.metadata.drop_all(cls.db_storage._DBStorage__engine)

    def test_all_method_returns_dict(self):
        """Tests that the 'all' method returns a dictionary."""
        all_objects = self.db_storage.all()
        self.assertEqual(type(all_objects), dict)


if __name__ == '__main__':
    unittest.main()
