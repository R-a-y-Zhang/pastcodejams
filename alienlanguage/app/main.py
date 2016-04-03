from dictionary_builder import alien_dict
import input_parser as ip
import solver as sv
in_file = 'mockInput.txt'
wordsize = 0
dictSize = 0
tests = 0

all_lines = []
full_dict = []
cases = []

with open(in_file) as f:
	all_lines = f.readlines()

params = all_lines[0]
params = params.split(" ");
wordsize = int(params[0])
dictSize = int(params[1])
tests = int(params[2])

full_dict = all_lines[1:1+dictSize]
cases = all_lines[1+dictSize:]
	
word_graph = alien_dict(full_dict, wordsize)

for i in range(len(cases)):
	cases[i] = ip.parse_raw(cases[i])

result = dict()

for i in range(len(cases)):
	result[i+1] = sv.solver(word_graph, cases[i]).solve()

for key, val in result.items():
	print('Case {}: {}'.format(key, val))
