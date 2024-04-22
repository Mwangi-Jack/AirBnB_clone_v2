#!/usr/bin/python3

import unittest
import uuid
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def setUp(self):
        self.place = Place()
        self.place.city_id = ""
        self.place.user_id = ""
        self.place.name = "Bahamas"
        self.place.description = "Nice to be here"
        self.place.max_guest = 50
        self.place.number_bathrooms = 4
        self.place.price_by_night = 1400
        self.place.latitude = 0.0
        self.place.longitude = 0.0
        self.place.amenity_ids = []
        self.place.number_rooms = 0

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_constructor(self):
        """Test the constructor of the Place class."""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, ())

    def test_save_method(self):
        """Test the save method of the Place class."""
        place = Place()
        place.save()
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of the Place class."""
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertIn('city_id', place_dict)
        self.assertIn('user_id', place_dict)
        self.assertIn('name', place_dict)
        self.assertIn('description', place_dict)
        self.assertIn('number_rooms', place_dict)
        self.assertIn('number_bathrooms', place_dict)
        self.assertIn('max_guest', place_dict)
        self.assertIn('price_by_night', place_dict)
        self.assertIn('latitude', place_dict)
        self.assertIn('longitude', place_dict)
        self.assertIn('amenity_ids', place_dict)

    def test_str_method(self):
        """Test the __str__ method of the Place class."""
        place_str = str(self.place)
        self.assertIn("[Place]", place_str)
        self.assertIn("'id':", place_str)
        self.assertIn("'created_at':", place_str)
        self.assertIn("'updated_at':", place_str)
        self.assertIn("'city_id':", place_str)
        self.assertIn("'user_id':", place_str)
        self.assertIn("'name':", place_str)
        self.assertIn("'description':", place_str)
        self.assertIn("'number_rooms':", place_str)
        self.assertIn("'number_bathrooms':", place_str)
        self.assertIn("'max_guest':", place_str)
        self.assertIn("'price_by_night':", place_str)
        self.assertIn("'latitude':", place_str)
        self.assertIn("'longitude':", place_str)
        self.assertIn("'amenity_ids':", place_str)


if __name__ == '__main__':
    unittest.main()
