class WordTrigger(Trigger):
	def __init__(self, word):
		self.word = word.lower()

	def isWordIn(self, text):
		import string
		punc = string.punctuation
		for i in punc:
			if i in text:
				text = text.replace(i, ' ')
		wordList = text.split(' ')
		print wordList
		if self.word in wordList:
			return True
		else:
			return False

class TitleTrigger(WordTrigger):
	def evaluate(self, story):
		if self.isWordIn(story.getTitle()):
			return True


class SummaryTrigger(WordTrigger):
	def evaluate(self, story):
		if self.isWordIn(story.getSummary()):
			return True

class SubjectTrigger(WordTrigger):
	def evaluate(self, story):
		if self.isWordIn(story.getSubject()):
			return True




