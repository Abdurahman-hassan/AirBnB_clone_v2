#!/usr/bin/python3
""" Defines the Amenity class as a subclass of BaseModel."""
from sqlalchemy import Column, String
import models
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Represents an amenity entity."""
    if models.storage_type == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
