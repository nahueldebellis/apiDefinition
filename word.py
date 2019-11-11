import nltk

class Word():
	def __init__(self):
		self.stop_words = nltk.corpus.stopwords.words('english')
	
	#word: string
	def synonyms(self, word):
		synonyms = nltk.corpus.wordnet.synsets(word)
		return synonyms

	#word: nltk object
	def definition(self, word):
		definition = word.definition()
		return definition

	def create_response(self, word):
		response = {}
		if word not in self.stop_words:
			syn = self.synonyms(word)
			response['synonyms'] = list(set([synonym.name().split('.')[0] for synonym in syn]))
			response['definition'] = self.definition(syn[0])
		
		return response
	
	
