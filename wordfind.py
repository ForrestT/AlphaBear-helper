class WF:

	def __init__(self):
		with open('words.txt') as f:
			self.words = [line.strip() for line in f.readlines()]
		self.w_copy = self.words[:]
		self.letters = ['c', 'h', 'o', 'i', 'r', 'i']
		self.candidates = {}
		self.mode = 'positive'
		for word in self.words:
			self.candidates[word] = word

	def set_mode(self, sign):
		if sign == '+':
			self.mode = 'positive'
		elif sign == '-':
			self.mode = 'negative'

	def re_init(self):
		self.words = self.w_copy[:]
		self.letters = []
		self.candidates = {}
		for word in self.words:
			self.candidates[word] = word

	def pare_words(self):
		for letter in self.letters:
			if letter in '+-':
				self.set_mode(letter)
				continue
			words_to_remove = []
			for word in self.words:
				if letter in self.candidates[word]:
					if self.mode == 'positive':
						i = self.candidates[word].index(letter)
						self.candidates[word] = self.candidates[word][:i] + self.candidates[word][i+1:]
					elif self.mode == 'negative':
						words_to_remove.append(word)
				else:
					if self.mode == 'positive':
						words_to_remove.append(word)
					elif self.mode == 'negative':
						continue
			for word in words_to_remove:
				self.words.remove(word)

	def reset_letters(self, letter_str):
		self.letters = [letter for letter in letter_str]

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
