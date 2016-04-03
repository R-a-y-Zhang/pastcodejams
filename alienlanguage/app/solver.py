
class solver:
	def __init__(self, dict_, letterArray):
		self.dict_ = dict_
		self.letterArray = letterArray
	
	def solve():
		result = dict()
		recursive_solve(result, 0, 0)

	# params
	# candidates: dictionary containnig a word as a key and the value is the node in the tree
	# WApos: subarray of letterArray currently being operated upon
	# pos: index within subarray
	def solve(self, candidates, WApos, pos):
		for i in range(len(self.letterArray[0])):
			node = self.dict_.walk(self.letterArray[0][i]
			if node:
				candidates[self.letterArray[0][i]] = node
		while (WApos != len(self.letterArray)):
			newCandidates = dict()
			for key in candidates:
				continuable = False
				temp = dict()
				for i in range(len(self.letterArray[WApos])):
					node = self.dict_.walkFrom(candidates[key], self.letterArray[WApos][i])
					if node:
						temp[key + self.letterArray[WApos][i]] = node
						continable = True

				if not continuable:
					candidates.pop(key, None)
				else:

