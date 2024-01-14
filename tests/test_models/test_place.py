import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime


class TestPlace(unittest.TestCase):

    def setUp(self):
        # Instantiate a Place object for testing
        self.place = Place()

    def test_place_instance(self):
        # Ensure that the Place instance is of the correct types
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place, BaseModel)

    def test_place_attributes(self):
        # Test various attributes of the Place class
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertNotEqual(self.place.amenity_ids, "")

        # Set new values for attributes and check if they are updated correctly
        self.place.city_id = "789"
        self.place.user_id = "101"
        self.place.name = "Cozy Cottage"
        self.place.description = "A charming place to stay"
        self.place.number_rooms = 2
        self.place.number_bathrooms = 1
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 37.7749
        self.place.longitude = -122.4194
        self.place.amenity_ids = "1,2,3"

        self.assertEqual(self.place.city_id, "789")
        self.assertEqual(self.place.user_id, "101")
        self.assertEqual(self.place.name, "Cozy Cottage")
        self.assertEqual(self.place.description, "A charming place to stay")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 37.7749)
        self.assertEqual(self.place.longitude, -122.4194)
        self.assertEqual(self.place.amenity_ids, "1,2,3")

    def test_place_inherited_attributes(self):
        # Test inherited attributes from the BaseModel class
        self.assertIsNotNone(self.place.id)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_place_str_representation(self):
        # Test the string representation of the Place class
        str_representation = str(self.place)
        self.assertIsInstance(str_representation, str)
        self.assertIn(self.place.id, str_representation)


if __name__ == '__main__':
    unittest.main()
