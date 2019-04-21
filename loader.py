import io

def load(path):
	words = []
	msg = "Set loaded."

	try:
		with open(path, 'r') as fin:
			for line in fin:
				for c in list(line.strip('\n')):
					words.append(c)
	except IOError:
		msg = "File could not be opened!"

	return (words, msg)

def save(path, world):
	msg = "World saved."

	try:
		with open(path, 'w') as fout:
			for line in world:
				for c in line:
					fout.write(c)
				fout.write('\n')
	except IOError:
		msg = "File could not be opened!"

	return msg
