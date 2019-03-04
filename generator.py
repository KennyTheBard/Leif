import random
import sys


def print_world_map(world):
	for i in range(len(world) - 1):
		for j in range(len(world[i]) - 1):
			sys.stdout.write(world[i][j])
		sys.stdout.write('\n')
	sys.stdout.write('\n')


WATER = ' '
GRASS = '^'
SAND = '.'
TALLGRASS = '/'
GRAVEL = '%'
STONE = 'n'
BUSHES = '~'

world = []
terrain = [WATER, GRASS, SAND, TALLGRASS, GRAVEL, STONE, BUSHES]
objects = ['Y', 'Q', '@', '&', '#']

width = 100
height = 75

for i in range(0, height - 1):
	world.append([])
	for j in range(0, width - 1):
		world[i].append('X')

zones = []
num_zones = random.randint(50, 100)
for i in range(num_zones):
	x = random.randint(10, width - 11)
	y = random.randint(10, height - 11)
	type = random.randint(0, len(terrain) - 1)
	zones.append((x, y, terrain[type]))

for i in range(0, width - 1, 20):
	zones.append((i, 0, WATER))
	zones.append((i, height - 1, WATER))

for i in range(0, height - 1, 20):
	zones.append((0, i, WATER))
	zones.append((width - 1, i, WATER))


for i in range(0, height - 1):
	for j in range(0, width - 1):
		min_dist = width * width * height * height
		min_val = 'X'

		for zone in zones:
			dist = (zone[1] - i) * (zone[1] - i) + (zone[0] - j) * (zone[0] - j)
			if dist < min_dist:
				min_dist = dist
				min_val = zone[2]

		world[i][j] = min_val

print_world_map(world)
