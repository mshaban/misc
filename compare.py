# import filecmp

# print filecmp.cmp('file.html', 'file.html')

import sys

from difflib import context_diff

import difflib
from difflib import Differ

s1 = ['bacon\n', 'eggs\n', 'ham\n', 'guido\n']
s2 = ['python\n', 'eggy\n', 'hamster\n', 'guido\n']

with open ("file.html", "r") as file:
	s1 = file.read()

with open ("file2.html", "r") as file2:
	s2 = file2.read()

# # print s1
# for line in context_diff(s1, s2, fromfile='before.py', tofile='after.py'):
# 	sys.stdout.write(line)

dif = list(Differ().compare(s1, s2))
print dif