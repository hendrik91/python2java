from Replacer import Replacer

class DoubleReplacer(Replacer):
	def __init__(self):
		Replacer.__init__(self, r'([a-z]\w*)\s*=\s*"(.*)"\s*', r'String \1 = "\2";')