import sys
from os import path

filePath = sys.argv[1]

if path.exists(filePath):
	file = open(filePath,"r")
	out = open("out.txt", "w+")
	contents = file.read()
	rows = contents.split("\n")

	for row in rows:
		cols = row.split(",")
		for col in cols:
			col = col.ljust(25,' ')
			col = col.replace(' ', '&nbsp;')
			print(col)
			out.write(col)
		out.write("\n")

