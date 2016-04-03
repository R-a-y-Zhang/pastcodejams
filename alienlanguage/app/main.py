from dictionary_builder import alien_dict
import input_parser as ip
in_file = 'A-small-practice.in.txt'
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

full_dict = all_lines[1:2+dictSize]
cases = all_lines[2+dictSize:]
	
word_graph = alien_dict(full_dict, wordsize)

for i in range(len(cases)):
	print(ip.parse_raw(cases[i]))
	print('\n')

