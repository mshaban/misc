

import math
import sys

BASE = 62
LOWER_CASE_OFFSET = 61
UPPER_CASE_OFFSET = 55
NUMBER_OFFSET = 48

def getChar(remainder):
	if 0 <= remainder <= 9:
		return chr(remainder + NUMBER_OFFSET)
	elif 10 <= remainder <= 35:
		return chr(remainder+UPPER_CASE_OFFSET)
	elif 36 <= remainder < 62:
		return chr(remainder + LOWER_CASE_OFFSET)
	else:
		raise ValueError ("value {} is not a possible remainder of base {}".format(remainder, BASE))

def getString(number):
	if number == 0:
		return '0'
	string = ""
	while number > 0:
		remainder = number % BASE
		string = getChar(remainder) + string
		number /= BASE
	return string

def getID(string):
	val = 0;
	string = string [::-1]
	for pw, char in enumerate(string):
		val += getOrder(char) * int(math.pow(BASE, pw))
	return val

def getOrder(char):
	if char.isdigit():
		return ord(char) - NUMBER_OFFSET
	elif 'A' <= char <= 'Z':
		return ord(char) - UPPER_CASE_OFFSET
	elif 'a' <= char <= 'z':
		return ord(char) - LOWER_CASE_OFFSET
	else:
		raise ValueError ("this char %d is not an ASCII character" % char)
		

if __name__ == '__main__':
	try:
		if(sys.argv[1] == '-g'):
			print getString(int(sys.argv[2]))
		elif(sys.argv[1] == '-r'):
			print getID(sys.argv[2])
		elif(sys.argv[1] == '-t'):
			file = open(sys.argv[2], 'r')
			passed = True
			for line in file:
				passed &= getID(getString(int(line))) == int(line)
				print getString(int(line))
			print passed 
			file.close()
		else:
			print 'unknow command'
	except ValueError as e:
		print e
