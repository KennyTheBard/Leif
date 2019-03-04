
from random import randint
import sys
import loader

# Commands
HELP = "help"
LOAD = "load"
GENERATE = "gen"
PRINT = "print"
SET = "set"
GET = "get"
LIST = "list"
EXIT = "exit"

sets = loader.read_sets()

world = []
param = {"W_RADIUS": 5, "H_RADIUS" : 5, ""}
cmd = ""

def help():
	print LIST + "\t\tlist all the available word sets"
	print LOAD + " <word_set>\tload the requested load set"
	print GENERATE + " <max_len>\tcreate a random word out of the previous loaded\n\t\tword set. A word set has to be already loaded.\n\t\tA maximum word length must be selected."
	print
	print EXIT + "\t\tclose the program"


def list():
	print "Available sets are:"
	for set in sets:
		print "\t" + set

def load(set):
	global words
	(words, msg) = loader.load(set)
	print msg


def generate():



def set(var_name, var_val):
	constants[var_name] = var_val
	print "Valoarea variabilei " + var_name + " a fost updatat la " + var_val

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
	elif LIST in cmd:
		list()
	elif LOAD in cmd:
		load(cmd.split(" ")[1])
	elif GENERATE in cmd:
		if len(cmd.split(" ")) > 1:
			generate(int(cmd.split(" ")[1]))
		else:
			generate(constants["STD_MAX"])
	elif DEFINE in cmd:
		if len(cmd.split(" ")) > 2:
			define(cmd.split(" ")[1], int(cmd.split(" ")[2]))
		else:
			print
	else:
		print "Use <" + HELP + "> for details about how to use the program"
	print ""
