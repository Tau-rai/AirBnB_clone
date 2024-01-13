#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        # Test if the BaseModel initializes with expected attributes
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_str(self):
        # Test if the string representation of the model is valid
        model = BaseModel()
        self.assertIsInstance(str(model), str)

    def test_save(self):
        # Test if calling save updates the 'updated_at' attribute
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(initial_updated_at, model.updated_at)

    def test_to_dict(self):
        # Test if to_dict() returns a dictionary with expected keys and values
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertTrue('id' in model_dict)
        self.assertTrue('created_at' in model_dict)
        self.assertTrue('updated_at' in model_dict)

    def test_from_dict(self):
        # Test if a new model can be created from a dictionary
        model = BaseModel()
        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.created_at, new_model.created_at)
        self.assertEqual(model.updated_at, new_model.updated_at)

    def test_custom_attributes(self):
        # Test if custom attributes can be added to the model
        model = BaseModel()
        model.name = "TestModel"
        model.my_number = 42
        self.assertEqual(model.name, "TestModel")
        self.assertEqual(model.my_number, 42)

    def test_created_at_isoformat(self):
        # Test if created_at isoformat() method returns a string
        model = BaseModel()
        self.assertIsInstance(model.created_at.isoformat(), str)

    def test_save_and_reload(self):
        # Test if saving a model and reloading retrieves the same attributes
        model = BaseModel()
        model.name = "TestModel"
        model.my_number = 42
        model.save()

        # Save the model ID for later comparison
        model_id = model.id

        # Reload the objects using the storage module
        storage.reload()

        # Get the reloaded model
        reloaded_model 

        # Assert that attributes are equal
        self.assertIsNotNone(reloaded_model)
        self.assertEqual(model.name, reloaded_model.name)
        self.assertEqual(model.my_number, reloaded_model.my_number)



    def test_update_attributes(self):
        # Test if attributes can be updated dynamically
        model = BaseModel()
        model.name = "OriginalName"
        model.my_number = 42

        # Update attributes
        model.name = 'UpdatedName'
        model.my_number = 99

        # Check if attributes are updated
        self.assertEqual(model.name, 'UpdatedName')
        self.assertEqual(model.my_number, 99)


if __name__ == '__main__':
    unittest.main()
