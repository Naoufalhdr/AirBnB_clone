#!/usr/bin/python3
"""This module user.py defines the class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class represents a user in the application.

    Attributes:
    - id (str): A unique identifier for each User instance.
    - email (str): The email address of the user.
    - password (str): The password associated with the user.
    - first_name (str): The first name of the user.
    - last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
