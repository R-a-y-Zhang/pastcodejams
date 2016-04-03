from letter_node import letter_node
class alien_dict:
	
	def construct_dictionary(self):
		for i in range(len(self.wordList)):
			word = self.wordList[i].strip()
			node = self.root
			for j in range(len(word)):
				try:
					node = node.children[word[j]]
				except KeyError:
					newNode = letter_node(word[j])
					node.add_children(word[j], newNode)

	def __init__(self, wordList, depth):
		self.root = letter_node('0')
		self.wordList = wordList
		self.depth = depth
		self.construct_dictionary()
	
	
	def walk(self, word):
		try:
			currentNode = self.root
			for i in range(len(word)):
				currentNode = currentNode.children[word[i]]

			return currentNode

		except KeyError:
			return None
	
	# walk from a certain node
	def walkFrom(self, startNode, word):
		try:
			currentNode = startNode
			for i in range(len(word)):
				currentNode = currentNode.children[word[i]]

			return currentNode

		except KeyError:
			return None
