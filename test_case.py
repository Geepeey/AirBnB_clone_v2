import unittest
import MySQLdb

class TestAddState(unittest.TestCase):
    def setUp(self):
        # Connect to the database
        self.db = MySQLdb.connect(host="localhost", user="testuser", passwd="testpass", db="testdb")
        self.cursor = self.db.cursor()

    def test_add_state(self):
        # Get the number of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Add a new state to the table
        self.cursor.execute("INSERT INTO states (name) VALUES ('California')")
        self.db.commit()

        # Get the new count of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        new_count = self.cursor.fetchone()[0]

        # Verify that the count increased by 1
        self.assertEqual(new_count, initial_count + 1)

    def tearDown(self):
        # Close the database connection
        self.db.close()

if __name__ == '__main__':
    unittest.main()

