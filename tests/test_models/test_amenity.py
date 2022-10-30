#!/usr/bin/python3

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # return super().setUpClass()
        cls.amenity1 = Amenity()
        cls.amenity1.name = "Swimming Pool"

    @classmethod
    def tearDownClass(cls) -> None:
        # return super().tearDownClass()
        del cls.amenity1
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def is_subclass(self):
        self.assertTrue(issubclass(self.amenity1.__class__, BaseModel))

    def test_checking_for_functions(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.amenity1.__dict__)
        self.assertTrue('created_at' in self.amenity1.__dict__)
        self.assertTrue('updated_at' in self.amenity1.__dict__)
        self.assertTrue('name' in self.amenity1.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.amenity1.name), str)

    def test_save(self):
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.amenity1), True)


if __name__ == '__main__':
    unittest.main()
