#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pep8


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value(state_id="123")
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value(name="California")
        self.assertEqual(type(new.name), str)

    def test_pep8(self):
        """Check console to be pep8 compliant"""
        fchecker = pep8.Checker("models/city.py", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)
