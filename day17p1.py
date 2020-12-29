

from itertools import product


INPUT = """
##......
.##...#.
.#######
..###.##
.#.###..
..#.####
##.####.
##..#.##
""".strip()


class Cube:
	def __init__(self, active):
		self.active = active
		self.state_on_update = None

	def decide_new_state(self, active_n_count):
		""" sets self.state_on_update """
		if self.active:
			self.state_on_update = self.active and active_n_count in (2, 3)
		else:
			self.state_on_update = active_n_count == 3
		# return value is used to determine if anything changed by other methods
		return self.state_on_update

	def update(self):
		assert self.state_on_update is not None
		self.active = self.state_on_update
		self.state_on_update = None

def active_neighbours(pos, cubes, add_new_cubes):
	c = 0
	for offset in (set(product([-1, 0, 1], repeat=3)) - {(0, 0, 0)}):
		index = tuple([i + j for i, j in zip(pos, offset)])
		if index in cubes:
			if cubes[index].active:
				c += 1
		else:
			# no neighbour found
			if add_new_cubes:
				cubes[index] = Cube(False)
	
	return c

def iterate_cubes(cubes):
	for pos, cube in {**cubes}.items():
		# determine new state for cube
		cube.decide_new_state(active_neighbours(pos, cubes, True))

	for pos, cube in cubes.items():
		# determine new state for new cubes as well
		cube.decide_new_state(active_neighbours(pos, cubes, False))

	# every cube knows what it's new state is, update them all
	for cube in cubes.values():
		cube.update()


def main():
	cubes = {}
	for x, row in enumerate(INPUT.split()):
		for y, c in enumerate(row):
			cubes[x, y, 0] = Cube(c == "#")

	for i in range(6):
		iterate_cubes(cubes)
	
	print(len([c for c in cubes.values() if c.active]))


if __name__ == '__main__':
	main()
