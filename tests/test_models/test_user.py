import unittest
from models.user import User
from datetime import datetime
import datetime 


class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Set up a sample user instance for testing.
        """
        self.created_at = datetime.datetime(2022, 1, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)
        self.updated_at = datetime.datetime(2022, 1, 2, 12, 0, 0, tzinfo=datetime.timezone.utc)

        self.sample_user = User(
            email="test@example.com",
            password="securepassword",
            first_name="John",
            last_name="Doe",
            created_at=created_at,
            updated_at=updated_at,
            id="unique_id"
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

    def test_str_representation(self):
        """Tests for string representation"""
        expected = "[User] ({}) {}".format(self.sample_user.id, self.sample_user.__dict__)
        self.assertEqual(str(self.sample_user), expected)

    def test_to_dict(self):
        """Tests the to_dict method on User class"""
        user_dict = self.sample_user.to_dict()
        self.assertEqual(type(user_dict), dict)
        self.assertTrue('id' in user_dict)
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)
        self.assertEqual(user_dict['__class__'], 'User')


if __name__ == '__main__':
    unittest.main()
