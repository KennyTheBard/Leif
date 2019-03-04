import io
from os import listdir
from os.path import isfile, join

STATES_FOLDER = "words_sets"


def read_sets():
	sets = []
	my_path = STATES_FOLDER + "/"

	files = listdir(my_path)
	for f in files:
		sets.append(f)

	return sets


def load(set):
	words = []
	my_path = STATES_FOLDER + "/"
	msg = "Set loaded."

	try:
		with open(my_path + set, 'r') as fin:
			for line in fin:
				words.append(line.strip('\n'))
	except IOError:
		msg = "File could not be opened!"

	return (words, msg)


if __name__ == "__main__":
	print load()
