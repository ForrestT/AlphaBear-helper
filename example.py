from wordfind import WF

w = WF()
while True:
	w.reset_letters(raw_input('\nLetters: '))
	w.pare_words()
	results = w.search(int(raw_input('\nMin Length: ')), int(raw_input('\nMax Length: ')))
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
