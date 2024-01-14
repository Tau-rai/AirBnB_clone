import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        # Set up any necessary resources or instances needed for tests
        self.instance = BaseModel()

    def tearDown(self):
        # Clean up any resources after each test
        del self.instance

    def test_initialization(self):
        # Test initialization with default values
        self.assertIsNotNone(self.instance.id)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

        # Test initialization with keyword arguments
        instance_with_args = BaseModel(id="custom_id", created_at="2022-01-01T12:00:00.000")
        self.assertEqual(instance_with_args.id, "custom_id")
        self.assertIsInstance(instance_with_args.created_at, datetime)

    def test_method_functionality(self):
        # Test each public method
        initial_updated_at = self.instance.updated_at
        self.instance.save()  # Test the save method
        self.assertNotEqual(initial_updated_at, self.instance.updated_at)

        dict_representation = self.instance.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertIn("__class__", dict_representation)
        self.assertEqual(dict_representation["__class__"], "BaseModel")

    def test_attribute_behavior(self):
        # Test attribute behavior by setting and retrieving values
        self.instance.id = "custom_id"
        self.assertEqual(self.instance.id, "custom_id")

    def test_boundary_conditions(self):
        # Test with input values at boundaries
        self.instance.id = "a" * 36  # Maximum length for UUID
        self.assertEqual(len(self.instance.id), 36)

        self.instance.id = ""
        self.assertEqual(len(self.instance.id), 0)

    def test_name_attribute(self):
        # Test setting and retrieving the 'name' attribute
        self.instance.name = "My First Model"
        self.assertEqual(self.instance.name, "My First Model")

    def test_my_number_attribute(self):
        # Test setting and retrieving the 'my_number' attribute
        self.instance.my_number = 89
        self.assertEqual(self.instance.my_number, 89)

    def test_string_representation(self):
        # Test the string representation of the object
        self.instance.name = "My First Model"
        self.instance.my_number = 89

        str_representation = str(self.instance)
        self.assertIn("[BaseModel] (", str_representation)
        self.assertIn("My First Model", str_representation)
        self.assertIn("89", str_representation)

    def test_save_method(self):
        # Test the save method
        initial_id = self.instance.id
        self.instance.save()
        self.assertEqual(initial_id, self.instance.id)

    def test_to_dict_method(self):
        # Test the to_dict method
        self.instance.name = "My First Model"
        self.instance.my_number = 89

        instance_json = self.instance.to_dict()
        self.assertIn("name", instance_json)
        self.assertIn("my_number", instance_json)
        self.assertEqual(instance_json["name"], "My First Model")
        self.assertEqual(instance_json["my_number"], 89)

    def test_create_instance_from_json(self):
        # Test creating a new instance from the JSON representation
        self.instance.name = "My First Model"
        self.instance.my_number = 89

        instance_json = self.instance.to_dict()
        new_instance = BaseModel(**instance_json)

        self.assertEqual(new_instance.id, self.instance.id)
        self.assertEqual(new_instance.name, self.instance.name)
        self.assertEqual(new_instance.my_number, self.instance.my_number)

    def test_object_identity(self):
        # Test object identity
        new_instance = BaseModel()
        self.assertFalse(self.instance is new_instance)

    def test_create_new_object(self):
        # Test creating a new object
        another_instance = BaseModel()
        another_instance.name = "My_second_Model"
        another_instance.my_number = 79
        initial_another_id = another_instance.id
        another_instance.save()
        self.assertEqual(initial_another_id, another_instance.id)

    def test_additional_attributes(self):
        """Test setting and accessing additional attributes"""
        self.instance.name = "My_First_Model"
        self.instance.my_number = 89

        self.assertEqual(self.instance.name, "My_First_Model")
        self.assertEqual(self.instance.my_number, 89)

    def test_id_generation(self):
        """Test if unique IDs are generated for each instance"""
        another_model = BaseModel()
        self.assertNotEqual(self.instance.id, another_model.id)

    def test_str(self):
        """Test the string representation of the instance"""
        expected_str = "[BaseModel] ({}) {}".format(self.instance.id, self.instance.__dict__)
        self.assertEqual(str(self.instance), expected_str)

    def test_created_at_type(self):
        """Test the type of the created_at attribute"""
        self.assertIsInstance(self.instance.created_at, datetime)

    def test_save_updates_updated_at(self):
        """Test if calling save updates the updated_at attribute"""
        original_updated_at = self.instance.updated_at
        self.instance.save()
        self.assertNotEqual(original_updated_at, self.instance.updated_at)

    def test_to_dict_structure(self):
        """Test the structure of the dictionary returned by to_dict"""
        self.instance.name = "My_First_Model"
        self.instance.my_number = 89

        model_dict = self.instance.to_dict()

        self.assertIn("__class__", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIn("name", model_dict)
        self.assertIn("my_number", model_dict)

        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertIsInstance(datetime.fromisoformat(model_dict["created_at"]), datetime)
        self.assertIsInstance(datetime.fromisoformat(model_dict["updated_at"]), datetime)
        self.assertEqual(model_dict["name"], "My_First_Model")
        self.assertEqual(model_dict["my_number"], 89)

    def test_to_dict_values(self):
        """Test the values in the dictionary returned by to_dict"""
        model_dict = self.instance.to_dict()

        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], self.instance.id)
        self.assertEqual(model_dict["created_at"], self.instance.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.instance.updated_at.isoformat())

    def test_json_output(self):
        """Test JSON output format"""
        my_model_json = self.instance.to_dict()

        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))


if __name__ == '__main__':
    unittest.main()
