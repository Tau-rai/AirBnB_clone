

import unittest
from models.user import User

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

if __name__ == '__main__':
    unittest.main()

