"""Importing Io class from classes_implementations"""
from classes_implementation import Io
import pytest


@pytest.mark.parametrize("input_file, expected", [("inp.txt", 145), ("inp2.txt", 0)])
def test_reading_files(input_file, expected):
    """This function tests various files as input and verifies output"""
    obj = Io(input_file)
    obj.read_file()
    assert len(obj.input_data) == expected
