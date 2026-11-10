import unittest
import todo

class TestTodo(unittest.TestCase):
    def setUp(self):
        todo.tasks.clear()

    def test_add_task(self):
        self.assertIn("Study", todo.add_task("Study"))

    def test_remove_task(self):
        todo.add_task("Study")
        todo.remove_task("Study")
        self.assertEqual(todo.list_tasks(), [])

if __name__ == "__main__":
    unittest.main()
