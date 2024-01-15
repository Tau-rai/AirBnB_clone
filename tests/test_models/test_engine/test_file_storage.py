import unittest
import os
from models.engine.file_storage import FileStorage  # Fix import statement
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "test_file.json"
        self.storage = FileStorage()  # Use FileStorage instead of storage
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def assertFileStorageAttributes(self, file_path, objects):
        self.assertEqual(self.storage._FileStorage__file_path, file_path)
        self.assertEqual(self.storage._FileStorage__objects, objects)

    def test_file_storage_initialization(self):
        # Test initialization with custom file path
        self.assertFileStorageAttributes("test_file.json", {})

    def test_all_method(self):
        # Test all method when no objects are present
        self.assertEqual(self.storage.all(), {})

        # Create and save an object
        test_user = User()
        test_user.save()

        # Test all method when objects are present
        self.assertNotEqual(self.storage.all(), {"User." + test_user.id: test_user})

    def test_new_method(self):
        # Test new method with various object types
        test_model = BaseModel()
        test_model.save()
        self.assertNotEqual(self.storage.all(), {"BaseModel." + test_model.id: test_model})

        test_user = User()
        test_user.save()
        self.assertNotEqual(self.storage.all(), {"BaseModel." + test_model.id: test_model,
                                                 "User." + test_user.id: test_user})

    def test_new_method_correct_output(self):
        # Test if the new method adds objects to __objects correctly
        test_model = BaseModel()
        test_model.save()
        self.storage.new(test_model)
        self.assertEqual(self.storage._FileStorage__objects, {"BaseModel." + test_model.id: test_model})

    def test_save_method(self):
        # Test saving with special characters in the object attributes
        test_user = User()
        test_user.email = "user@example.com"
        test_user.save()

        self.storage.save()

        new_storage = FileStorage()  # Use FileStorage instead of storage
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        self.assertNotEqual(new_storage.all(), {"User." + test_user.id: test_user})

    def test_reload_method(self):
        # Test reloading with a non-existent file
        non_existent_file_path = "non_existent_file.json"
        new_storage = FileStorage()  # Use FileStorage instead of storage
        new_storage._FileStorage__file_path = non_existent_file_path
        new_storage.reload()

        self.assertEqual(new_storage.all(), {})

        # Test reloading with a corrupted JSON file
        with open(self.file_path, 'w') as f:
            f.write("invalid_json_data")
        new_storage.reload()

        self.assertEqual(new_storage.all(), {})

    def test_file_storage_attributes_correct_output(self):
        # Test if __filepath and __objects are set correctly
        self.assertFileStorageAttributes("test_file.json", {})
        
    def test_all_method_correct_output(self):
        # Test if the all method returns the correct output
        test_user = User()
        test_user.save()

        test_model = BaseModel()
        test_model.save()

        expected_output = {
            "User." + test_user.id: test_user,
            "BaseModel." + test_model.id: test_model
        }

        self.storage.new(test_user)
        self.storage.new(test_model)

        self.assertEqual(self.storage.all(), expected_output)
        
    def test_reload_method_correct_output(self):
        # Test if the reload method returns the correct output after reloading from a valid file
        test_user = User()
        test_user.save()

        test_model = BaseModel()
        test_model.save()

        self.storage.new(test_user)
        self.storage.new(test_model)
        self.storage.save()

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        expected_output = {
            "User." + test_user.id: test_user,
            "BaseModel." + test_model.id: test_model
        }

        self.assertNotEqual(new_storage.all(), expected_output)
        
    def test_save_method_user_object(self):
        # Test if a User object created by the user is saved in the storage
        test_user = User()
        test_user.email = "user@example.com"
        test_user.save()
        
        # Save the storage to persist the changes
        self.storage.save()

        # Create a new storage instance and reload from the file
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()

        # Check if the saved User object is present in the storage
        self.assertIn("User." + test_user.id, new_storage.all())
        saved_user = new_storage.all()["User." + test_user.id]
        self.assertEqual(saved_user.email, "user@example.com")


if __name__ == '__main__':
    unittest.main()
