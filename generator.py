import random
import sys

def print_world_map(world):
	for i in range(len(world) - 1):
		for j in range(len(world[i]) - 1):
			sys.stdout.write(world[i][j])
		sys.stdout.write('\n')
	sys.stdout.write('\n')


def get_neighbours(pos, world, strength):
	x = pos[0]
	y = pos[1]
	neigh = []

	for i in range(y - strength, y + strength + 1):
		for j in range(x - strength, x + strength + 1):
			if i >= 0 and i < len(world) and j >= 0 and j < len(world[0]):
				neigh.append(world[i][j])
	return neigh


def set_counters_zero(counters, terrain):
	for i in range(len(terrain)):
		counters[terrain[i]] = 0


def smoothen(world, terrain, strength):
	counters = {}

	for i in range(len(world)):
		for j in range(len(world[0])):
			set_counters_zero(counters, terrain)
			neigh = get_neighbours((j, i), world, strength)
			for n in neigh:
				counters[n] += 1

			terr = terrain[1]
			max = 0
			for t in range(len(terrain)):
				if counters[terrain[t]] > max:
					max = counters[terrain[t]]
					terr = terrain[t]


			world[i][j] = terr


def old_generate(height, width, terrain):
	world = []
	for i in range(0, height - 1):
		world.append([])
		for j in range(0, width - 1):
			world[i].append('X')

	zones = []
	num_zones = random.randint(30, 60)
	for i in range(num_zones):
		x = random.randint(10, width - 11)
		y = random.randint(10, height - 11)
		type = random.randint(1, len(terrain) - 1)
		zones.append((x, y, terrain[type]))

	for i in range(0, width - 1, 20):
		zones.append((i, 0, terrain[0]))
		zones.append((i, height - 1, terrain[0]))

	for i in range(0, height - 1, 20):
		zones.append((0, i, terrain[0]))
		zones.append((width - 1, i, terrain[0]))


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
	return world
