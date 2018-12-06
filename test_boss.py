'''Boss module testing'''

import pytest
from boss import Boss

@pytest.fixture
def object_generator():
    return Boss()

def test_horizontal_movement(object_generator):
	initial_posx = object_generator.posX
	initial_posy = object_generator.posY
	for _ in range(20):
		object_generator.moveleft()

	assert object_generator.posY == initial_posy - 20
	assert object_generator.posX == initial_posx

	object_generator.moveright()
	object_generator.moveright()
	assert object_generator.posY == initial_posy - 18
	assert object_generator.posX == initial_posx

def test_vertical_movement(object_generator):
	initial_posx = object_generator.posX
	object_generator.movejump()
	assert object_generator.posX == initial_posx - 1
	assert object_generator.inair == True

def test_shoot(object_generator):
	for _ in range(5):
		object_generator.shoot()

	assert len(object_generator.bulletarr) == 5