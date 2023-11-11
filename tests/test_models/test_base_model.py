#!/usr/bin/python3
"""This module test_base_model.py is unittests for the class BaseModel"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """TestBaseModel class contains unit tests for the BaseModel class."""

    def setUp(self):
        self.base_model = BaseModel()

    def test_instance_creation(self):
        self.assertIsInstance(self.base_model, BaseModel)

    def test_attributes_existence(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(original_updated_at, self.base_model.updated_at)

    def test_to_dict_returns_dict(self):
        self.assertIsInstance(self.base_model.to_dict(), dict)

    def test_str_representation(self):
        expected_str = (
                f"[{self.base_model.__class__.__name__}] "
                f"({self.base_model.id}) {self.base_model.__dict__}"
                )
        self.assertEqual(str(self.base_model), expected_str)


if __name__ == '__main__':
    unittest.main()
