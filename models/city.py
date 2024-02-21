#!/usr/bin/python3
"""Defines the City class as a subclass of BaseModel."""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

import models
from models import storage_type
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """Represents a city entity."""
    if models.storage_type == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)