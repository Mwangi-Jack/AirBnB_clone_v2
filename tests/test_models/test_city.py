#!/usr/bin/pthon3

import unittest
import uuid
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def setUp(self):
        self.new_city = City()
        self.new_city.state_id = str(uuid.uuid4())
        self.new_city.name = 'Bahamas'

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        self.assertTrue(issubclass(City, BaseModel))

    def test_constructor(self):
        """Test the constructor of the City class."""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_save_method(self):
        """Test the save method of the City class."""
        self.new_city.save()
        self.assertIsNotNone(self.new_city.created_at)
        self.assertIsNotNone(self.new_city.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of the City class."""
        city_dict = self.new_city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('state_id', city_dict)
        self.assertIn('name', city_dict)

    def test_str_method(self):
        """Test the __str__ method of the City class."""
        city_str = str(self.new_city)

        self.assertIn("[City]", city_str)
        self.assertIn("'id':", city_str)
        self.assertIn("'created_at':", city_str)
        self.assertIn("'updated_at':", city_str)
        self.assertIn("'state_id':", city_str)
        self.assertIn("'name':", city_str)


if __name__ == '__main__':
    unittest.main()
