import random
import sys
import queue


# unfilled tiles default value
EMPTY = 'X'


# helper function that prints the world map
def print_world_map(world):
	for i in range(len(world) - 1):
		for j in range(len(world[i]) - 1):
			sys.stdout.write(world[i][j])
		sys.stdout.write('\n')
	sys.stdout.write('\n')


# returns the grid addresses of the neigbouring tiles
# (initial tile also for smoothening value)
def get_neighbours(pos, world, strength):
	y = pos[0]
	x = pos[1]
	neigh = []

	for i in range(y - strength, y + strength + 1):
		for j in range(x - strength, x + strength + 1):
			if i >= 0 and i < len(world) and j >= 0 and j < len(world[0]):
				neigh.append((i, j))
	return neigh


# reset the counter for each terrain to 0
def reset_counters(counters, terrain):
	for i in range(len(terrain)):
		counters[terrain[i]] = 0


# smoothens the worldmap given an area around each point
# with a given strength
def smoothen(world, terrain, strength):
	counters = {}

	for i in range(len(world)):
		for j in range(len(world[0])):
			# counts each neigbouring terrain
			reset_counters(counters, terrain)
			neigh = get_neighbours((j, i), world, strength)
			for n in neigh:
				counters[world[n[0]][n[1]]] += 1

			# pick the dominant terrain
			terr = terrain[0]
			max = 0
			for t in range(len(terrain)):
				if counters[terrain[t]] > max:
					max = counters[terrain[t]]
					terr = terrain[t]
			world[i][j] = terr


# the old implementation for PG algorithm
# DEPRECATED
def old_generate(height, width, terrain):
	# initiate the world
	world = []
	for i in range(0, height):
		world.append([])
		for j in range(0, width):
			world[i].append(EMPTY)

	# create some random voronoi dots
	zones = []
	num_zones = random.randint(30, 60)
	for i in range(num_zones):
		x = random.randint(10, width - 11)
		y = random.randint(10, height - 11)
		type = random.randint(1, len(terrain) - 1)
		zones.append((y, x, terrain[type]))

	# add water dots to the borders
	for i in range(0, width, 20):
		zones.append((i, 0, terrain[0]))
		zones.append((i, height - 1, terrain[0]))
	for i in range(0, height, 20):
		zones.append((0, i, terrain[0]))
		zones.append((width - 1, i, terrain[0]))

	# fill up the map with the terrain type
	# of the closest voronoi dot
	for i in range(0, height):
		for j in range(0, width):
			# initiate min distance
			min_dist = width * width * height * height
			min_val = 'X'

			# iterate through voronoi dots
			for zone in zones:
				dist = (zone[1] - i) * (zone[1] - i) + (zone[0] - j) * (zone[0] - j)
				if dist < min_dist:
					min_dist = dist
					min_val = zone[2]
			world[i][j] = min_val

	return world


# generates a world of height x width tiles with
# given elements of terrain
def generate(height, width, terrain):
	# initiate the world
	world = []
	for i in range(0, height):
		world.append([])
		for j in range(0, width):
			world[i].append(EMPTY)

	# create some random voronoi dots
	q = queue.Queue()
	num_zones = random.randint(30, 60)
	for i in range(num_zones):
		y = random.randint(10, height - 11)
		x = random.randint(10, width - 11)
		type = random.randint(1, len(terrain) - 1)
		q.push((y, x, terrain[type]))

	# add water dots to the borders
	for i in range(0, height, 20):
		q.push((i, 0, terrain[0]))
		q.push((i, width - 1, terrain[0]))
	for i in range(0, width, 20):
		q.push((0, i, terrain[0]))
		q.push((height - 1, i, terrain[0]))

	# add neighbouring tiles to the queue until the
	# entire map is filled up with terrain types
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
