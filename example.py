from wordfind import WF

w = WF()
while True:
	w.set_letters(raw_input('\nLetters: '))
	word_list = w.pare_words()
	results = w.search(word_list)
	print('\n' + '-'*15)
	for word in results:
		print(word)
	print('-'*15 + '\n')

	again = raw_input('Further Narrow? [y/n]: ')
	if 'y' in again.lower():
		continue
	else:
		again = raw_input('\nStart new search? [y/n]: ')
		if 'y' in again.lower():
			w.re_init()
			continue
		else:
			break
