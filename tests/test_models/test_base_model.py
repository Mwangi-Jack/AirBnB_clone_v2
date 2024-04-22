#!/usr/bin/python3

import time
import unittest
from datetime import datetime
import uuid
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up a BaseModel instance for testing."""
        self.new_model = BaseModel()

    def test_constructor(self):
        """
        Test the constructor of the BaseModel class.
        """
        self.assertIsInstance(self.new_model.id, str)
        self.assertIsInstance(self.new_model.created_at, datetime)
        self.assertIsInstance(self.new_model.updated_at, datetime)

    def test_save(self):
        """Test the save method of the BaseModel class."""
        self.assertTrue(len(self.new_model.save.__doc__) > 0)
        previous_updated_at = self.new_model.updated_at
        time.sleep(0.01)
        self.new_model.save()
        self.assertNotEqual(previous_updated_at, self.new_model.updated_at)
        self.assertIsInstance(self.new_model.updated_at, datetime)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel class."""
        expected_dict = {
            'id': self.new_model.id,
            'created_at': self.new_model.created_at.isoformat(),
            'updated_at': self.new_model.updated_at.isoformat(),
            '__class__': 'BaseModel'
        }
        self.assertDictEqual(expected_dict, self.new_model.to_dict())

    def test_str(self):
        """Test the string representation of the BaseModel class."""
        _str = f"[BaseModel] ({self.new_model.id}) {self.new_model.__dict__}"
        self.assertEqual(_str, str(self.new_model))

    def test_constructor_with_arguments(self):
        """
        Test the constructor of the BaseModel class with keyword arguments
        """
        kwargs = {
            'id': str(uuid.uuid4()),
            'created_at': '2024-02-12T10:26:27.647394',
            'updated_at': '2024-02-12T10:26:27.647394'
        }
        new_model = BaseModel(**kwargs)
        self.assertEqual(new_model.id, kwargs['id'])
        self.assertEqual(new_model.created_at.isoformat(),
                         kwargs['created_at'])
        self.assertEqual(new_model.updated_at.isoformat(),
                         kwargs['created_at'])


if __name__ == '__main__':
    unittest.main()
