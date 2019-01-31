import unittest
from functionalities import *         #There are some servers that are configured to look for packages in your base python packages. This may not work when you're hosting externally
from location_functions import *



class Database_tests(unittest.TestCase):
    #------------ Testing connection to database --------------#
    def test_db_exists(self):
        self.assertTrue(checks_db('phonebook_database.db'))
        self.assertTrue(getDB()) #Checks connection

        #------------ Testing data retrieval --------------#
    def test_get_businesses(self):
        self.assertTrue(get_businesses()), 'Error retrieving data'

    def test_get_people(self):
        self.assertTrue(get_businesses()), 'Error retrieving data'

    def test_get_user_postcode(self):
        self.assertInInstance(get_user_postcode('ph2 7hu'), str)

        #------------ Testing user input functions --------------#
    def test_person_input(self):
        self.assertTrue(find_person_by_name('Erika'))
        self.assertIsInstance(find_person_by_name('Butch'), str)

    def test_find_person_by_postcode(self):
        self.assertIsInstance(find_person_by_postcode(8698), str) #input_postcode automatically converts input to a string - this is to catch any bugs that pop up later
        self.assertTrue(find_person_by_postcode('ti48sp'))

    def test_get_postcode_api(self):
        self.assertEqual(get_postcode_api())

if __name__ == "__main__":
    unittest.main()
