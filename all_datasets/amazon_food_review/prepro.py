import glob
with open('foodpos.txt', 'r', encoding = 'ISO-8859-1') as inf:
 count = 1
 for line in inf:
  fname = str(count) + '.pos'
  with open (fname, 'w', encoding = 'ISO-8859-1') as outf:
   outf.write(line)
   count += 1 
