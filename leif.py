
from random import randint
import sys
import loader
import generator as gen

# Commands
EXIT = "exit"
HELP = "help"
CLEAR = "clear"
PRINT_MAP = "print_map"
PRINT_SET = "print_set"
LOAD = "load"
SAVE = "save"
GENERATE = "gen"
SET = "set"
GET = "get"
SMOOTHEN = "smooth"

HELP_MESSAGE = "Use <" + HELP + "> for details about how to use the program"

world = []
terrain = []
vars = {"width": 50, "height" : 50}
cmd = ""

def help():
	print EXIT + "\t\tclose the program"
	print CLEAR + "\t\tclear the current map"
	print PRINT_MAP + "\tprint the current world map"
	print PRINT_SET + "\tprint the current terrain set"
	print LOAD + "\t\tload a new terrain set"
	print GENERATE + "\t\tgenerate a new world"
	print SET + "\t\tset the value of a variable"
	print GET + "\t\tget the value of a variable"
	print SMOOTHEN + "\t\tsmoothen the current map"


def clear():
	world = []


def print_set():
	print terrain


def load(path):
	global terrain
	(terrain, msg) = loader.load(path)
	print msg


def save(path):
	msg = loader.save(path, world)
	print msg


def generate():
	global world
	if len(terrain) > 0:
		world = gen.generate(vars["height"], vars["width"], terrain)
	else:
		print "Load a terrain set first!"


def smoothen(str):
	if len(world) > 0 and len(terrain) > 0:
		gen.smoothen(world, terrain, str)


def print_world():
	if len(world) > 0:
		gen.print_world_map(world)
	else:
		print "Generate a world first!"


def print_set():
	print terrain


def set(var_name, var_val):
	vars[var_name.lower()] = var_val
	print "Value of " + var_name.upper() + " has been updated to " + str(vars[var_name.lower()])


def get(var_name):
	if var_name.lower() in vars:
		print "Value of " + var_name.upper() + " is " + str(vars[var_name.lower()])
	else:
		print var_name.upper() + " has not been defined!"


def interogate_user():
	sys.stdout.write(">> ")
	sys.stdout.flush()
	return sys.stdin.readline().strip('\n')


while True:
	cmd = interogate_user().lower().strip().split(" ")
	if EXIT in cmd:
		break

	elif HELP in cmd:
		help()

	elif CLEAR in cmd:
		clear()

	elif PRINT_MAP in cmd:
		print_world()

	elif PRINT_SET in cmd:
		print_set()

	elif LOAD in cmd:
		if len(cmd) > 1:
			load(cmd[1])
		else:
			print HELP_MESSAGE

	elif SAVE in cmd:
		if len(cmd) > 1:
			save(cmd[1])
		else:
			print HELP_MESSAGE

	elif GENERATE in cmd:
		generate()

	elif SET in cmd:
		if len(cmd) > 2:
			set(cmd[1], int(cmd[2]))
		else:
			print HELP_MESSAGE

	elif GET in cmd:
		if len(cmd) > 1:
			get(cmd[1])
		else:
			print HELP_MESSAGE

	elif SMOOTHEN in cmd:
		if len(cmd) > 1:
			smoothen(int(cmd[1]))
		else:
			print HELP_MESSAGE

	else:
		print HELP_MESSAGE
		
	print ""
