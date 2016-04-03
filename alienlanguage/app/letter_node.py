class letter_node:
	def __init__(self, letter):
		self.letter = letter
		self.children = dict()

	def add_children(self, letter, nextNode):
		self.children[letter] = nextNode
