#!/usr/bin/python3
"""The implementation of the Test User module"""

import unittest
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):
    """A class that implements test cases against the User module."""

    def setUp(self):
        """Set up the test environment before testing occurs."""
        self.user = User()

    def test_if_user_is_a_subclass_of_basemodel(self):
        """Check if User is a subclass of BaseModel."""
        u = User()
        self.assertTrue(issubclass(type(u), BaseModel))

    def test_if_attrs_are_class_attrs(self):
        """Check if the class attributes 'first_name' and 'last_name' are present."""
        u = User()
        self.assertTrue(hasattr(User, "first_name") and hasattr(User, "last_name"))

    def test_class_attrs(self):
        """Check if the class attributes 'first_name' and 'last_name' are valid."""
        u = User()
        self.assertIs(type(u.first_name), str)
        self.assertIs(type(u.last_name), str)
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")

