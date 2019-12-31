import unittest
from conf import Conf
from pathlib import Path
import os, json

class ConfTestCase(unittest.TestCase):

    _default_directory = Path.home().joinpath('.svsoft')
    _default_file_name = 'budgeton.cfg'

    @classmethod
    def setUpClass(self):
        self._cnf = Conf()

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def delete_all(self):
        try:
            # remove all files in directory .svsoft
            for current_file in os.listdir(self._default_directory):
                os.remove(self._default_directory.joinpath(current_file))
        except FileNotFoundError:
            pass

        try:
            # remove file
            os.rmdir(self._default_directory)
        except FileNotFoundError:
            pass

        pass

    def test_creation_file(self):
        # delete directory if exist
        self.delete_all()

        # test if deleted correctly
        self.assertEqual(self._default_directory.exists(), False)

        self._cnf = Conf()

        # test if created correctly
        self.assertEqual(self._default_directory.exists(), True)    # directory
        self.assertEqual(self._default_directory.joinpath(self._default_file_name).exists(), True)  #file

    def test_init_values(self):
        self.assertEqual(self._cnf.get('last_opened'), False)

    def test_if_property_not_exist_is_none(self):
        self.assertEqual(self._cnf.get("another_random_property"), None)

    def test_save_method(self):
        self._cnf.set('toto', True)
        self.assertEqual(self._cnf.get('toto'), True)

        f = open(self._default_directory.joinpath(self._default_file_name), 'r', encoding='utf-8')
        content = f.read()
        json_obj = json.loads(content)
        self.assertEqual(json_obj['toto'], True)

# main
if __name__ == '__main__':
    unittest.main()