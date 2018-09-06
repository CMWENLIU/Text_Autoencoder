import glob
import os
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

files = glob.glob('*.org')
for f in files:
	with open (f, 'r', encoding = 'ISO-8859-1') as inf:
		count = 1
		for line in inf:
			fname = str(count) + '_' + f + '.txt'
			with open(fname, 'w', encoding = 'ISO-8859-1') as outf:
				outf.write(line)
			count += 1
