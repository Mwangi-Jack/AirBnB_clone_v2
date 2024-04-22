#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        self.new_user = User()
        self.new_user.email = ('test@example.com',)
        self.new_user.password = 'password'
        self.new_user.first_name = 'John'
        self.new_user.last_name = 'Doe'

    def test_inheritance(self):
        """Test inheritance from BaseModel."""
        self.assertTrue(issubclass(User, BaseModel))

    def test_constructor(self):
        """Test the constructor of the User class."""
        self.assertEqual(self.new_user.email, ('test@example.com',))
        self.assertEqual(self.new_user.password, 'password')
        self.assertEqual(self.new_user.first_name, 'John')
        self.assertEqual(self.new_user.last_name, 'Doe')

    @patch('models.storage')
    def test_new(self, mock_storage):
        """Test the new method of the User class."""
        user = MagicMock(spec=User)
        user.__class__.__name__ = 'User'
        user.id = 'test_id'
        user.email = 'test@example.com'
        user.password = 'password'
        user.first_name = 'John'
        user.last_name = 'Doe'
        User.__init__(user)
        # mock_storage.new.assert_called_once_with(user)

    # def test_save(self):
    #     """Test the save method of the User class."""
    #     user = User()
    #     user.save()
    #     self.assertEqual(user.updated_at, user.created_at)
    #     # mock_storage.save.assert_called_once()

    def test_to_dict(self):
        """Test the to_dict method of the User class."""
        expected_dict = {
            'id': self.new_user.id,
            'created_at': self.new_user.created_at.isoformat(),
            'updated_at': self.new_user.updated_at.isoformat(),
            '__class__': 'User',
            'email': ('test@example.com',),
            'password': 'password',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        self.assertDictEqual(self.new_user.to_dict(), expected_dict)

    def test_str(self):
        """Test the __str__ method of the User class."""
        expected_obj = {
            'id': self.new_user.id,
            'created_at': self.new_user.created_at,
            'updated_at': self.new_user.updated_at,
            'email': ('test@example.com',),
            'password': 'password',
            'first_name': 'John',
            'last_name': 'Doe'
            }
        expected_str = f"[User] ({self.new_user.id}) {expected_obj}"
        self.assertEqual(str(self.new_user), expected_str)


if __name__ == '__main__':
    unittest.main()
