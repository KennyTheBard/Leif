import generator

WATER = ' '
GRASS = '^'
SAND = '.'
TALLGRASS = '/'
GRAVEL = '%'
STONE = 'n'
BUSHES = '~'

terrain = [WATER, GRASS, SAND, TALLGRASS, GRAVEL, STONE, BUSHES]

width = 35
height = 35

world = generator.old_generate(height, width, terrain)

generator.print_world_map(world)

for i in range(1):
	generator.smoothen(world, terrain)

generator.print_world_map(world)
