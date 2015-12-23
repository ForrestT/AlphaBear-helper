class WF:

	def __init__(self):
		with open('words.txt') as f:
			self.words = [line.strip() for line in f.readlines()]
		self.w_copy = self.words[:]
		self.letters = {'+':[], '-':[]}
		self.candidates = {}
		self.mode = '+'
		for word in self.words:
			self.candidates[word] = word

	def set_mode(self, sign):
		if sign == '+':
			self.mode = '+'
		elif sign == '-':
			self.mode = '-'

	def re_init(self):
		self.words = self.w_copy[:]
		self.letters = {'+':[], '-':[]}
		self.candidates = {}
		for word in self.words:
			self.candidates[word] = word

	def negative_letter_check(self, word, letters):
		for letter in letters:
			if letter in word:
				return True
		return False

	def positive_letter_check(self, word, letters):
		w_list = [l for l in word]
		for letter in letters:
			if letter in w_list:
				w_list.remove(letter)
			else:
				return False
		return True

	def pare_words(self):
		matched_words = []
		for word in self.words:
			if self.negative_letter_check(word, self.letters['-']):
				if self.positive_letter_check(word, self.letters['+']):
					matched_words.append(word)
		return matched_words

		# for letter in self.letters:
		# 	if letter in '+-':
		# 		self.set_mode(letter)
		# 		continue
		# 	words_to_remove = []
		# 	for word in self.words:
		# 		if letter in self.candidates[word]:
		# 			if self.mode == 'positive':
		# 				i = self.candidates[word].index(letter)
		# 				self.candidates[word] = self.candidates[word][:i] + self.candidates[word][i+1:]
		# 			elif self.mode == 'negative':
		# 				words_to_remove.append(word)
		# 		else:
		# 			if self.mode == 'positive':
		# 				words_to_remove.append(word)
		# 			elif self.mode == 'negative':
		# 				continue
		# 	for word in words_to_remove:
		# 		self.words.remove(word)

	def set_letters(self, letter_str):
		self.mode = '+'
		l = []
		for letter in letter_str:
			if letter in '-+':
				self.mode = letter
			else:
				self.letters[self.mode].append(letter)

	def reset_letters(self, letter_str):
		self.letters = {'+':[], '-':[]}
		self.set_letters(letter_str)

	def add_letters(self, letter_str):
		temp = [letter for letter in letter_str]
		self.letters += temp

	def search(self, min_len, max_len, add_letter=''):
		results = []
		for word in self.words:
			if len(word) <= max_len and len(word) >= min_len:
				if add_letter == '' or add_letter in word:
					results.append(word)
		return results
