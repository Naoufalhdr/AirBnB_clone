#!/usr/bin/python3
""" This module city.py defines the City class """
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class represents a city in the application.

    Attributes:
    - state_id (str): The ID of the state to which the city belongs.
    - name (str): The name of the city.
    """

    state_id = ""
    name = ""
