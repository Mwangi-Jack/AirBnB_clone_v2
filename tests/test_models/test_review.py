#!/usr/bin/python3

import unittest
import uuid
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def setUp(self):
        self.new_review = Review()
        self.new_review.place_id = ""
        self.new_review.user_id = str(uuid.uuid4())
        self.new_review.text = "Nice to be here"

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_constructor(self):
        """Test the constructor of the Review class."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_save_method(self):
        """Test the save method of the Review class."""
        review = Review()
        review.save()
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of the Review class."""
        review_dict = self.new_review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)
        self.assertIn('place_id', review_dict)
        self.assertIn('user_id', review_dict)
        self.assertIn('text', review_dict)

    def test_str_method(self):
        """Test the __str__ method of the Review class."""
        review_str = str(self.new_review)
        self.assertIn("[Review]", review_str)
        self.assertIn("'id':", review_str)
        self.assertIn("'created_at':", review_str)
        self.assertIn("'updated_at':", review_str)
        self.assertIn("'place_id':", review_str)
        self.assertIn("'user_id':", review_str)
        self.assertIn("'text':", review_str)


if __name__ == '__main__':
    unittest.main()
