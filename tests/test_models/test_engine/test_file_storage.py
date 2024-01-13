import unittest
import os
from models.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "test_file.json"
        self.file_storage = FileStorage()
        self.file_storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_file_storage_initialization(self):
        # Test initialization with custom file path
        self.assertEqual(self.file_storage._FileStorage__file_path, "test_file.json")
        self.assertEqual(self.file_storage._FileStorage__objects, {})

    def test_all_method(self):
        # Test all method when no objects are present
        self.assertEqual(self.file_storage.all(), {})

        # Create and save an object
        test_user = User()
        test_user.save()

        # Test all method when objects are present
        self.assertEqual(self.file_storage.all(), {"User." + test_user.id: test_user})

    def test_new_method(self):
        # Test new method with various object types
        test_model = BaseModel()
        test_model.save()
        self.assertEqual(self.file_storage.all(), {"BaseModel." + test_model.id: test_model})

        test_user = User()
        test_user.save()
        self.assertEqual(self.file_storage.all(), {"BaseModel." + test_model.id: test_model,
                                                   "User." + test_user.id: test_user})

    def test_save_method(self):
        # Test saving with special characters in the object attributes
        test_user = User()
        test_user.email = "user@example.com"
        test_user.save()

        self.file_storage.save()

        new_file_storage = FileStorage()
        new_file_storage._FileStorage__file_path = self.file_path
        new_file_storage.reload()

        self.assertEqual(new_file_storage.all(), {"User." + test_user.id: test_user})

    def test_reload_method(self):
        # Test reloading with a non-existent file
        non_existent_file_path = "non_existent_file.json"
        new_file_storage = FileStorage()
        new_file_storage._FileStorage__file_path = non_existent_file_path
        new_file_storage.reload()

        self.assertEqual(new_file_storage.all(), {})

        # Test reloading with a corrupted JSON file
        with open(self.file_path, 'w') as f:
            f.write("invalid_json_data")
        new_file_storage.reload()

        self.assertEqual(new_file_storage.all(), {})


if __name__ == '__main__':
    unittest.main()

