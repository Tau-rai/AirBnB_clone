import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        # Clean up
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_initialization(self):
        self.assertIsInstance(self.storage, FileStorage)
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertDictEqual(self.storage._FileStorage__objects, {})

    def test_all(self):
        self.assertDictEqual(self.storage.all(), {})
        obj = BaseModel()
        self.storage.new(obj)
        self.assertDictEqual(self.storage.all(), {'BaseModel.' + obj.id: obj})

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        store = self.storage._FileStorage__objects
        self.assertIn('BaseModel.' + obj.id, store)

    def test_save(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        with open(self.storage._FileStorage__file_path, 'r') as file:
            content = file.read()
            self.assertIn('BaseModel.' + obj.id, content)

    def test_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        self.assertDictEqual(new_storage.all(), {'BaseModel.' + obj.id: obj})

    def test_integration_with_base_model(self):
        obj = BaseModel()
        obj.save()
        new_storage = FileStorage()
        new_storage.reload()

        self.assertDictEqual(new_storage.all(), {'BaseModel.' + obj.id: obj})


if __name__ == '__main__':
    unittest.main()
