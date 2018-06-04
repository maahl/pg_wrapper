#! /usr/bin/env python3

import os
import shutil
import unittest
from pg_wrapper import *


TMP_DIR = os.path.abspath('test_data')
PG_VENV = 'test_pg_venv'


def setUpModule():
    '''
    Set environment vars necessary for running the tests, and create the
    directory that will contain the test data.
    '''
    os.makedirs(TMP_DIR)
    os.environ['PG_VIRTUALENV_HOME'] = TMP_DIR


def tearDownModule():
    '''
    Remove test data
    '''
    shutil.rmtree(TMP_DIR)


class CreateVirtualenv(unittest.TestCase):
    '''
    Test all the actions required to create a postgres virtualenv
    '''
    def test_00_retrieve_postgres_source(self):
        retrieve_postgres_source(PG_VENV)
        # check that at least a file is actually there
        print(get_pg_src(PG_VENV))
        assert(os.path.isfile(os.path.join(get_pg_src(PG_VENV), 'README')))



if __name__ == '__main__':
    unittest.main(buffer=True)
