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

        new_name = "Bulawayo"
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
        

if __name__ == '__main__':
    unittest.main()

