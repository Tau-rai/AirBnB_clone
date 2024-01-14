import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


class TestCity(unittest.TestCase):

    def setUp(self):
        # Instantiate a City object for testing
        self.city = City()

    def test_city_instance(self):
        # Ensure that the City instance is of the correct types
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_city_attributes(self):
        # Test various attributes of the City class
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

        # Set new values for attributes and check if they are updated correctly
        self.city.state_id = "456"
        self.city.name = "San Francisco"

        self.assertEqual(self.city.state_id, "456")
        self.assertEqual(self.city.name, "San Francisco")

    def test_city_inherited_attributes(self):
        # Test inherited attributes from the BaseModel class
        self.assertIsNotNone(self.city.id)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_city_to_dict(self):
        # Test the to_dict method of the City class
        self.city.state_id = "456"
        dict_representation = self.city.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertIn('__class__', dict_representation)
        self.assertIn('created_at', dict_representation)
        self.assertIn('updated_at', dict_representation)
        self.assertIn('state_id', dict_representation)
        self.assertIn('name', dict_representation)
       
        self.assertEqual(dict_representation['__class__'], 'City')

    def test_city_str_representation(self):
        # Test the string representation of the City class
        str_representation = str(self.city)
        self.assertIsInstance(str_representation, str)
        self.assertIn(self.city.id, str_representation)


if __name__ == '__main__':
    unittest.main()

