#!/usr/bin/python3
"""The implementation of the Test Amenity module"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """A class that implements test cases against the Amenity module."""

    def setUp(self):
        """Set up the test environment before testing occurs."""
        self.amenity = Amenity()

    def test_if_amenity_is_a_subclass_of_basemodel(self):
        """Check if Amenity is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_if_attr_is_a_class_attr(self):
        """Check if the 'name' attribute is a class attribute."""
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_class_attr(self):
        """Check if the 'name' class attribute is valid."""
        self.assertIs(type(self.amenity.name), str)
        self.assertFalse(bool(getattr(self.amenity, "name")))

