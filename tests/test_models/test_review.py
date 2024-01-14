import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime


class TestReview(unittest.TestCase):

    def setUp(self):
        # Instantiate a Review object for testing
        self.review = Review()

    def test_review_instance(self):
        # Ensure that the Review instance is of the correct types
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)

    def test_review_place_id(self):
        # Test the place_id attribute of the Review class
        self.assertEqual(self.review.place_id, "")

        # Set a new place_id and check if it's updated correctly
        new_place_id = "123"
        self.review.place_id = new_place_id
        self.assertEqual(self.review.place_id, new_place_id)

    def test_review_user_id(self):
        # Test the user_id attribute of the Review class
        self.assertEqual(self.review.user_id, "")

        # Set a new user_id and check if it's updated correctly
        new_user_id = "456"
        self.review.user_id = new_user_id
        self.assertEqual(self.review.user_id, new_user_id)

    def test_review_text(self):
        # Test the text attribute of the Review class
        self.assertEqual(self.review.text, "")

        # Set a new text and check if it's updated correctly
        new_text = "A great experience!"
        self.review.text = new_text
        self.assertEqual(self.review.text, new_text)

    def test_review_inherited_attributes(self):
        # Test inherited attributes from the BaseModel class
        self.assertIsNotNone(self.review.id)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)



    def test_review_str_representation(self):
        # Test the string representation of the Review class
        str_representation = str(self.review)
        self.assertIsInstance(str_representation, str)
        self.assertIn(self.review.id, str_representation)


if __name__ == '__main__':
    unittest.main()

