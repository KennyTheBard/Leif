import random
import sys
import queue

EMPTY = 'X'

def print_world_map(world):
	for i in range(len(world) - 1):
		for j in range(len(world[i]) - 1):
			sys.stdout.write(world[i][j])
		sys.stdout.write('\n')
	sys.stdout.write('\n')


def get_neighbours(pos, world, strength):
	y = pos[0]
	x = pos[1]
	neigh = []

	for i in range(y - strength, y + strength + 1):
		for j in range(x - strength, x + strength + 1):
			if i >= 0 and i < len(world) and j >= 0 and j < len(world[0]):
				neigh.append((i, j))
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
				counters[world[n[0]][n[1]]] += 1

			terr = terrain[1]
			max = 0
			for t in range(len(terrain)):
				if counters[terrain[t]] > max:
					max = counters[terrain[t]]
					terr = terrain[t]


			world[i][j] = terr


def old_generate(height, width, terrain):
	world = []
	for i in range(0, height):
		world.append([])
		for j in range(0, width):
			world[i].append(EMPTY)

	zones = []
	num_zones = random.randint(30, 60)
	for i in range(num_zones):
		x = random.randint(10, width - 11)
		y = random.randint(10, height - 11)
		type = random.randint(1, len(terrain) - 1)
		zones.append((y, x, terrain[type]))

	for i in range(0, width, 20):
		zones.append((i, 0, terrain[0]))
		zones.append((i, height - 1, terrain[0]))

	for i in range(0, height, 20):
		zones.append((0, i, terrain[0]))
		zones.append((width - 1, i, terrain[0]))


	for i in range(0, height):
		for j in range(0, width):
			min_dist = width * width * height * height
			min_val = 'X'

			for zone in zones:
				dist = (zone[1] - i) * (zone[1] - i) + (zone[0] - j) * (zone[0] - j)
				if dist < min_dist:
					min_dist = dist
					min_val = zone[2]

			world[i][j] = min_val
	return world


def generate(height, width, terrain):
	world = []
	for i in range(0, height):
		world.append([])
		for j in range(0, width):
			world[i].append(EMPTY)

	q = queue.Queue()
	num_zones = random.randint(30, 60)
	for i in range(num_zones):
		y = random.randint(10, height - 11)
		x = random.randint(10, width - 11)
		type = random.randint(1, len(terrain) - 1)
		q.push((y, x, terrain[type]))

	for i in range(0, height, 20):
		q.push((i, 0, terrain[0]))
		q.push((i, width - 1, terrain[0]))

	for i in range(0, width, 20):
		q.push((0, i, terrain[0]))
		q.push((height - 1, i, terrain[0]))


	while not q.empty():
		y, x, terr = q.pop()
		if world[y][x] == EMPTY:
			world[y][x] = terr
			neigh = get_neighbours((y, x), world, 1)
			for pos in neigh:
				if world[pos[0]][pos[1]] == EMPTY:
					if pos[0] != y or pos[1] != x:
						q.push((pos[0], pos[1], terr))

	return world
