'''Coin module testing'''

import pytest
from coin import Coin

@pytest.fixture
def object_generator():
    return Coin(1, 1)

def test_posx_getter(object_generator):
    assert object_generator.posx == 1

def test_posx_setter(object_generator):
    object_generator.posx += 3
    assert object_generator.posx == 4
