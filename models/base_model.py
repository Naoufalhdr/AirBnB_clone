#!/usr/bin/python3
"""This module base_model.py defines the BaseModel class."""
import uuid
import models
from datetime import datetime


class BaseModel:
    """
    BaseModel class defines common attributes and methods for other classes.

    Attributes:
    - id (str): A unique identifier for each instance.
    - created_at (datetime): The datetime when the instance is created.
    - updated_at (datetime): The datetime when the instance is last updated.
    """
    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance."""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, time_format))
                elif k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Update the 'updated_at' attribute with the current datetime and
        save the instance."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        new_dict = self.__dict__.copy()
        new_dict.update({'updated_at': self.updated_at.isoformat()})
        new_dict.update({'created_at': self.created_at.isoformat()})
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """Return a sting representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
