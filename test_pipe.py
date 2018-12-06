'''Pipe module testing'''

from pipe import Pipe
import pytest

@pytest.fixture
def object_generator():
    return Pipe(1, 1)

def test_posx_getter(object_generator):
    assert object_generator.posx == 1

def test_posx_setter(object_generator):
    object_generator.posx += 3
    assert object_generator.posx == 4
