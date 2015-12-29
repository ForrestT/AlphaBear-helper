from wordfind import WF
from sys import exit

def display_menu():
	print """
	0) display filter results
	1) set letters to filter by
	2) set minimum word length
	3) set maximum word length
	4) view current filters
	5) reset
	6) exit
	"""

def display_results():
	results = w.filter()
	print('\n' + '-'*15)
	for word in results:
		print(word)
	print('-'*15 + '\n')

def parse_input(c):
	if c == '0':
		display_results()
	elif c == '1':
		w.set_letters(raw_input('\nLetters: '))
	elif c == '2':
		w.min_len = int(raw_input('\nMin Word Length: '))
	elif c == '3':
		w.max_len = int(raw_input('\nMax Word Length: '))
	elif c == '4':
		print w
	elif c == '5':
		w.re_init()
	elif c == '6':
		exit()
	else:
		parse_input(raw_input('\nInvalid Input\nChoose another Option: '))

w = WF()
while True:
	display_menu()
	parse_input(raw_input('\nChoose Option: '))
# while True:
# 	w.set_letters(raw_input('\nLetters: '))
# 	word_list = w.pare_words()
# 	results = w.search(word_list)
# 	print('\n' + '-'*15)
# 	for word in results:
# 		print(word)
# 	print('-'*15 + '\n')
#
# 	again = raw_input('Further Narrow? [y/n]: ')
# 	if 'y' in again.lower():
# 		continue
# 	else:
# 		again = raw_input('\nStart new search? [y/n]: ')
# 		if 'y' in again.lower():
# 			w.re_init()
# 			continue
# 		else:
# 			break
