import unittest
from models.base_model import BaseModel
from datetime import datetime, timedelta

class TestBaseModel(unittest.TestCase):
    def test_base_model_creation(self):
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_base_model_str_representation(self):
        my_model = BaseModel()
        model_str = str(my_model)
        self.assertIn("[BaseModel]", model_str)
        self.assertIn(str(my_model.id), model_str)

    def test_base_model_save(self):
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_base_model_to_dict(self):
        my_model = BaseModel()
        model_dict = my_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], my_model.updated_at.isoformat())

    def test_base_model_kwargs_init(self):
        # Test initializing with kwargs
        data = {
            "id": "123",
            "created_at": "2022-01-01T00:00:00.000",
            "updated_at": "2022-01-01T01:00:00.000",
            "custom_attribute": "test"
        }
        my_model = BaseModel(**data)
        self.assertEqual(my_model.id, "123")
        self.assertEqual(my_model.created_at, datetime(2022, 1, 1))
        self.assertEqual(my_model.updated_at, datetime(2022, 1, 1, 1, 0))
        self.assertEqual(getattr(my_model, "custom_attribute", None), "test")

if __name__ == '__main__':
    unittest.main()
