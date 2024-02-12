#!/usr/bin/python3
"""The implementation of the Test Review module"""

import unittest
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):
    """A class that implements test cases against the Review module."""

    def setUp(self):
        """Set up the test environment before testing occurs."""
        self.review = Review()
        self.attr_list = [
            "place_id",
            "user_id",
            "text"
        ]

    def test_if_review_is_a_subclass_of_basemodel(self):
        """Check if Review is a subclass of BaseModel."""
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_if_attrs_are_class_attrs(self):
        """Check if the class attributes are present."""
        for attr in self.attr_list:
            self.assertTrue(hasattr(self.review, attr))

    def test_class_attrs(self):
        """Check if the class attributes are valid."""
        for attr in self.attr_list:
            self.assertIs(type(getattr(self.review, attr)), str)
            self.assertFalse(bool(getattr(self.review, attr)))

