class solver:
	def __init__(self, dict_, letterArray):
		self.dict_ = dict_
		self.letterArray = letterArray

	def solve_(self, candidates, WApos):
		for i in range(len(self.letterArray[0])):
			node = self.dict_.walk(self.letterArray[0][i])
			if node:
				candidates[self.letterArray[0][i]] = node

		WApos += 1
		while (WApos != len(self.letterArray)):
			newCandidates = dict()
			for key in candidates:
				continuable = False
				temp = dict()
				for i in range(len(self.letterArray[WApos])):
					node = self.dict_.walkFrom(candidates[key], self.letterArray[WApos][i])
					if node:
						print(candidates[key].letter, node.letter)
					if node:
						temp[key + self.letterArray[WApos][i]] = node
						continable = True

				if continuable:
					newCandidates.update(temp)
			candidates = newCandidates
			WApos += 1
		count = 0
		for key in candidates.items():
			count += 1
		return count

	def solve(self):
		result = dict()
		return self.solve_(result, 0)
