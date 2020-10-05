import pytest
import allure
import os

@allure.feature('miuns')
def test_note(name=9):
    a = 2
    assert a > name


if __name__ == '__main__':
    pytest.main(['-vs', '--alluredir', 'report'])
    
