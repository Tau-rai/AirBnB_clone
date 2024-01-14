import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


class TestAmenity(unittest.TestCase):

    def setUp(self):
        # Instantiate an Amenity object for testing
        self.amenity = Amenity()

    def test_amenity_instance(self):
        # Ensure that the Amenity instance is of the correct types
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenity_attributes(self):
        # Test various attributes of the Amenity class
        self.assertEqual(self.amenity.name, "")

        # Set a new value for the attribute and check if it's updated correctly
        self.amenity.name = "WiFi"

        self.assertEqual(self.amenity.name, "WiFi")

    def test_amenity_inherited_attributes(self):
        # Test inherited attributes from the BaseModel class
        self.assertIsNotNone(self.amenity.id)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    
    def test_amenity_str_representation(self):
        # Test the string representation of the Amenity class
        str_representation = str(self.amenity)
        self.assertIsInstance(str_representation, str)
        self.assertIn(self.amenity.id, str_representation)


if __name__ == '__main__':
    unittest.main()

