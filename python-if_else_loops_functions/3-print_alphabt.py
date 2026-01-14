#!/usr/bin/python3
a = ord('a')
for i in range(a, (a+26)):
	if chr(i) != 'q' and chr(i) != 'e':
		print("{}".format(chr(i)), end="")
