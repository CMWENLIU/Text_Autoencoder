import glob
import os

files = glob.glob('rt*')
for f in files:
	with open (f, 'r', encoding='ISO-8859-1') as inf:
		count = 1
		for line in inf:
			fname = str(count) + '_' + f + '.txt'
			with open(fname, 'w', encoding='utf-8') as outf:
				outf.write(line)
			count += 1
