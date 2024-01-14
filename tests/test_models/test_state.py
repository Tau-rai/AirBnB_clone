import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_state_instance(self):
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)

    def test_state_name(self):
        self.assertEqual(self.state.name, "")

        new_name = "California"
        self.state.name = new_name
        self.assertEqual(self.state.name, new_name)

    def test_state_inherited_attributes(self):
        self.assertIsNotNone(self.state.id)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)

    
    def test_state_str_representation(self):
        str_representation = str(self.state)
        self.assertIsInstance(str_representation, str)
        self.assertIn(self.state.id, str_representation)
        
        
    def test_to_dict_method(self):
        """
        Test the to_dict method of State
        """
        state = State()
        state_dict = state.to_dict()
        self.assertIn("__class__", state_dict)
        self.assertEqual(state_dict["__class__"], "State")
        self.assertIn("id", state_dict)
        self.assertEqual(state_dict["id"], state.id)
        self.assertIn("created_at", state_dict)
        self.assertEqual(
            state_dict["created_at"], state.created_at.isoformat()
        )
        self.assertIn("updated_at", state_dict)
        self.assertEqual(
            state_dict["updated_at"], state.updated_at.isoformat()
        )
        self.assertIn("name", state_dict)
        self.assertEqual(state_dict["name"], state.name)


if __name__ == '__main__':
    unittest.main()

