#!/usr/bin/python3
"""The implementation of the Test City module"""

import unittest
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):
    """A class that implements test cases against the City module."""

    def setUp(self):
        """Set up the test environment before testing occurs."""
        self.city = City()
        self.attr_list = ["state_id", "name"]

    def test_if_city_is_a_subclass_of_basemodel(self):
        """Check if City is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_if_attrs_are_class_attrs(self):
        """Check if the class attributes are present and initialized as empty strings."""
        for attr in self.attr_list:
            self.assertIs(type(getattr(self.city, attr)), str)
            self.assertEqual(getattr(self.city, attr), "")

