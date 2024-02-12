#!/usr/bin/python3
"""The implementation of the Test State module"""

import unittest
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):
    """A class that implements test cases against the State module."""

    def setUp(self):
        """Set up the test environment before testing occurs."""
        self.state = State()

    def test_if_state_is_a_subclass_of_basemodel(self):
        """Check if State is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_if_attr_is_a_class_attr(self):
        """Check if the 'name' attribute is a class attribute."""
        self.assertTrue(hasattr(self.state, "name"))

    def test_class_attrs(self):
        """Check if the 'name' class attribute is valid."""
        self.assertIs(type(self.state.name), str)
        self.assertFalse(bool(self.state.name))

