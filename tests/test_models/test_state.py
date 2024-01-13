import unittest
from datetime import datetime
from models import state
from models.state import State


class TestState(unittest.TestCase):

    def test_inheritance(self):
        # Test if State class inherits from BaseModel
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))

    def test_initialization_with_args(self):
        # Test if initialization with arguments sets attributes correctly
        state_id = "test_state_id"
        created_at = datetime(2022, 1, 1, 12, 0, 0)
        updated_at = datetime(2022, 1, 2, 12, 0, 0)
        state = State(id=state_id, created_at=created_at, updated_at=updated_at, name="TestState")

        self.assertEqual(state.id, state_id)
        self.assertEqual(state.created_at, created_at)
        self.assertEqual(state.updated_at, updated_at)
        self.assertEqual(state.name, "TestState")

    def test_initialization_with_kwargs(self):
        # Test if initialization with keyword arguments sets attributes correctly
        state_dict = {
            'id': "test_state_id",
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-02T12:00:00.000000',
            'name': "TestState"
        }
        state = State(**state_dict)

        self.assertEqual(state.id, state_dict['id'])
        self.assertEqual(state.created_at, datetime.strptime(state_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(state.updated_at, datetime.strptime(state_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(state.name, state_dict['name'])

    def test_to_dict(self):
        # Test if to_dict method returns a dictionary with expected keys and values
        state = State()
        state_dict = state.to_dict()

        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertTrue('id' in state_dict)
        self.assertTrue('created_at' in state_dict)
        self.assertTrue('updated_at' in state_dict)
        self.assertTrue('name' in state_dict)

    def test_str(self):
        # Test if the string representation of the State object is valid
        state = State(name="TestState")
        self.assertEqual(str(state), "[State] ({}) {}".format(state.id, state.__dict__))


if __name__ == '__main__':
    unittest.main()

