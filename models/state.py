#!/usr/bin/python3
""" This module state.py defines the State class """
from models.base_model import BaseModel


class State(BaseModel):
    """
    Place class represents a place in the application.

    Attributes:
    - name (str): The name of the place.
    """

    name = ""
