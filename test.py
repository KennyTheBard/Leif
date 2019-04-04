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

aux1 = world
aux2 = world
aux3 = world

generator.print_world_map(aux1)

generator.smoothen(aux2, terrain, 1)
generator.smoothen(aux2, terrain, 1)
generator.print_world_map(aux2)

generator.smoothen(aux3, terrain, 2)
generator.smoothen(aux3, terrain, 2)
generator.print_world_map(aux3)
