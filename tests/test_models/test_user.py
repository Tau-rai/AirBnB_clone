

import unittest
from models.user import User
from datetime import datetime

class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Set up a sample user instance for testing.
        """
        self.sample_user = User(
            email="test@example.com",
            password="securepassword",
            first_name="John",
            last_name="Doe"
        )

    def test_initialization(self):
        """
        Test if the instance is initialized properly.
        """
        self.assertIsInstance(self.sample_user, User)

    def test_attributes_setting(self):
        """
        Test if attributes are set correctly during initialization.
        """
        self.assertEqual(self.sample_user.email, "test@example.com")
        self.assertEqual(self.sample_user.password, "securepassword")
        self.assertEqual(self.sample_user.first_name, "John")
        self.assertEqual(self.sample_user.last_name, "Doe")

    def test_default_values(self):
        """
        Test if default values are applied when no arguments are provided.
        """
        default_user = User()
        self.assertEqual(default_user.email, "")
        self.assertEqual(default_user.password, "")
        self.assertEqual(default_user.first_name, "")
        self.assertEqual(default_user.last_name, "")

    def test_check_type(self):
        self.assertEqual(type(self.sample_user.id), str)
        self.assertEqual(type(self.sample_user.created_at), datetime)
        self.assertEqual(type(self.sample_user.updated_at), datetime)

    def test_str_representation(self):
        expected = "[User] ({}) {}".format(self.sample_user.id, self.sample_user.__dict__)
        self.assertEqual(str(self.sample_user), expected)

    def test_save(self):
        self.sample_user.save()
        self.assertNotEqual(self.sample_user.created_at, self.sample_user.updated_at)

    def test_to_dict(self):
        user_dict = self.sample_user.to_dict()
        self.assertEqual(type(user_dict), dict)
        self.assertTrue('id' in user_dict)
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)
        self.assertEqual(user_dict['__class__'], 'User')

if __name__ == '__main__':
    unittest.main()

