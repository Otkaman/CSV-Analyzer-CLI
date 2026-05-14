import pytest
from parser import readFile
from exceptions import ParseError


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        readFile('File doesn`t exist.csv')

def test_wrong_extension():
    with pytest.raises(ParseError):
        readFile('../report.txt')

def test_returns_list():
    assert readFile('./tests/tests_data/file_exist.csv') == ['3','7','6']






