#https://www.tecmint.com/convert-files-to-utf-8-encoding-in-linux/
#!/bin/bash
#enter input encoding here
FROM_ENCODING="ASCII"
#output encoding(UTF-8)
TO_ENCODING="UTF-8"
#convert
CONVERT=" iconv  -f   $FROM_ENCODING  -t   $TO_ENCODING"
#loop to convert multiple files 
for  file  in  *.pos; do
$CONVERT   "$file"   -o  "${file%.txt}.utf8.converted"
done
exit 0