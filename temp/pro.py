import glob
import os
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

files = glob.glob('*.txt')

for f in files:
	os.remove(f)
'''
for f in files:
	with open (f, 'r', encoding = 'ISO-8859-1') as inf:
		fname = f + '.new'
		with open(fname, 'w', encoding = 'ISO-8859-1') as outf:
			for line in inf:			
				outf.write(line)'''
