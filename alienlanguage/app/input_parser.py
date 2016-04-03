# returns 2x2 array of letters
def parse_raw(line):
	line = line.strip()
	parsed_input = []
	tempArray = []
	toBuffer = False
	
	for i in range(len(line)):
		if line[i] == '(':
			toBuffer = True
		elif line[i] == ')':
			toBuffer = False
			parsed_input.append(tempArray)
			tempArray = []
		else:
			if (toBuffer):
				tempArray.append(line[i])
			else:
				parsed_input.append([line[i]])
	
	return parsed_input
