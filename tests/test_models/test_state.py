#!/usr/bin/python3

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def setUp(self):
        self.new_state = State()
        self.new_state.name = 'Bahamas'

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_constructor(self):
        """Test the constructor of the State class."""
        state = State()
        self.assertEqual(state.name, "")

    def test_save_method(self):
        """Test the save method of the State class."""
        state = State()
        state.save()
        self.assertIsNotNone(state.created_at)
        self.assertIsNotNone(state.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of the State class."""
        state_dict = self.new_state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIn('id', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertIn('name', state_dict)

    def test_str_method(self):
        """Test the __str__ method of the State class."""
        state_str = str(self.new_state)
        self.assertIn("[State]", state_str)
        self.assertIn("'id':", state_str)
        self.assertIn("'created_at':", state_str)
        self.assertIn("'updated_at':", state_str)
        self.assertIn("'name':", state_str)


if __name__ == '__main__':
    unittest.main()
