#!/usr/bin/python3
""" This module review.py defines the review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class represents a review in the application.

    Attributes:
    - place_id (str): The ID of the place to which the review is related.
    - user_id (str): The ID of the user who wrote the review.
    - text (str): The text content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
