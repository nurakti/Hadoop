

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None


for line in sys.stdin:

	line = line.strip()

	word, count = line.split("\t", 1)

	try:
		say = int(count)
	except ValueError:
		
		continue


	if current_word == word:
		current_count += count # type: ignore
	else:
		if current_word:

			print '%s\t%s' % (current_word, current_count) # type: ignore
		current_count = count
		current_word = word

if current_word == word:
	print '%s\t%s' % (current_word, current_count) # type: ignore
