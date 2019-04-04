
from random import randint
import sys
import loader

# Commands
HELP = "help"
LOAD = "load"
GENERATE = "gen"
SMOOTHEN = "smooth"
PRINT_MAP = "print_map"
PRINT_SET = "print_set"
SET = "set"
GET = "get"
EXIT = "exit"

sets = loader.read_sets()

world = []
terrain = []
param = {"width": 50, "height" : 50, "strength" : 1}
cmd = ""

def help():
	print LIST + "\t\tlist all the available word sets"
	print LOAD + " <word_set>\tload the requested load set"
	print GENERATE + " <max_len>\tcreate a random word out of the previous loaded\n\t\tword set. A word set has to be already loaded.\n\t\tA maximum word length must be selected."
	print
	print EXIT + "\t\tclose the program"


def print_set():
	print terrain


def load(set):
	global words
	(words, msg) = loader.load(set)
	print msg


def generate():
	if len(terrain) > 0:
		world = gen.generate(param["height"], param["width"], terrain)


def print_world():
	gen.print_world_map(world)


def set(var_name, var_val):
	constants[var_name.lower()] = var_val
	print "Valoarea variabilei " + var_name.upper() + " a fost updatat la " + var_val


def get(var_name):
	if var_name.upper() in constants:
		print "Valoarea variabilei " + var_name.upper() + " a fost updatat la " + constants[var_name.lower()]
	else:
		print "Variabile " + var_name.upper() + " nu a fost setata!"


def interogate_user():
	sys.stdout.write(">> ")
	sys.stdout.flush()
	return sys.stdin.readline().strip('\n')


while True:
	cmd = interogate_user().lower().strip()
	if EXIT in cmd:
		break
	elif HELP in cmd:
		help()
	elif PRINT in cmd:
		print_world()
	elif LOAD in cmd:
		load(cmd.split(" ")[1])
	elif GENERATE in cmd:
		generate()
	elif DEFINE in cmd:
		if len(cmd.split(" ")) > 2:
			define(cmd.split(" ")[1], int(cmd.split(" ")[2]))
		else:
			print
	else:
		print "Use <" + HELP + "> for details about how to use the program"
	print ""
