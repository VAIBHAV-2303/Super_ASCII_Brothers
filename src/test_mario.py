'''Mario module testing'''

from mario import Mario
import pytest

@pytest.fixture
def object_generator():
    return Mario()

def test_shoot(object_generator):
	object_generator.shoot()
	assert len(object_generator.bulletarr) == 1

	object_generator.supershoot()
	assert len(object_generator.bulletarr) == 4

def test_Superjump(object_generator):
	initial_posx = object_generator.posx
	object_generator.Superjump()
	assert object_generator.posx == initial_posx - 4
