import io

def load(path):
	words = []
	msg = "Set loaded."

	print path

	try:
		with open(path, 'r') as fin:
			for line in fin:
				for c in list(line.strip('\n')):
					words.append(c)
	except IOError:
		msg = "File could not be opened!"

	return (words, msg)
