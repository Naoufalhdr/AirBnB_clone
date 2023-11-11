#!/usr/bin/python3
""" This module amenity.py defines the Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class represents a amenity in the application.

    Attributes:
    - name (str): The name of the city.
    """

    name = ""
