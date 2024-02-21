#!/usr/bin/python3
"""Provides a base class for data models with common functionality."""
import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models


if models.storage_type == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """Base class for data models."""
    if models.storage_type == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            # The __class__ key if being deleted from the kwargs
            # in the BaseModel __init__ method without first checking
            # if it exists.
            # it will throw a KeyError if the key is not present in the kwargs.
            # we should only delete it if it's actually present in the kwargs.
            # so we use the pop method instead of the del method.
            kwargs.pop('__class__', None)
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self,
                            key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Return a string representation of the object.

        Returns:
            str: String representation of the object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.to_dict()}"

    def save(self):
        """Save the current state of the object and trigger
        the storage save process.
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict

    def delete(self):
        """
        Delete the current instance from the storage.
        """
        models.storage.delete(self)