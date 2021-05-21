'''Enemy module testing'''

import pytest
from enemy import Enemy

@pytest.fixture
def object_generator():
    return Enemy()

def test_movement(object_generator):
	initial_posy = object_generator.posy
	object_generator.inair = True
	object_generator.inairtime = 0
	for _ in range(5):
		object_generator.move()

	assert object_generator.posy == initial_posy - 5
	