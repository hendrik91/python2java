import re

class Replacer:
	__regex = None
	__replace = None
	__used = 0

	def __init__(self, regex, replace):
		self.__regex = regex
		self.__replace = replace

	def simpleReplace(self, input):
		return re.sub(self.__regex, self.__replace, input, re.I)

	def replace(self, input):
		return self.simpleReplace(input)

