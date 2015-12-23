class WF:

	def __init__(self):
		with open('words.txt') as f:
			self.words = [line.strip() for line in f.readlines()]
		self.w_copy = self.words[:]
		self.letters = {'+':[], '-':[]}
		self.candidates = {}
		self.mode = '+'
		self.min_len = 8
		self.max_len = 8
		for word in self.words:
			self.candidates[word] = word

	def re_init(self):
		self.words = self.w_copy[:]
		self.letters = {'+':[], '-':[]}
		self.candidates = {}
		for word in self.words:
			self.candidates[word] = word

	def negative_letter_check(self, word, letters):
		for letter in letters:
			if letter in word:
				return False
		return True

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

	def search(self, word_list):
		matched_words = []
		for word in word_list:
			if len(word) <= self.max_len and len(word) >= self.min_len:
				matched_words.append(word)
		return matched_words
