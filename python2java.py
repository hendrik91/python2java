import sys
import os

import Replacer.IntegerReplacer as IntegerReplacer
import Replacer.DoubleReplacer as DoubleReplacer
import Replacer.BlockReplacer as BlockReplacer
import Replacer.LoopReplacer as LoopReplacer
import Replacer.SyntaxReplacer as SyntaxReplacer


def openClass(outFile, name):
	outFile.write("""public class %s {
	public static void main(String[] args){
		""" % name)

def closeClass(outFile):
	outFile.write("\t}\n}")


replacers = []
replacers.append(IntegerReplacer.IntegerReplacer())
replacers.append(DoubleReplacer.DoubleReplacer())
replacers.append(LoopReplacer.LoopReplacer())
replacers.append(SyntaxReplacer.SyntaxReplacer())

javaCode = ""

if os.path.isfile(sys.argv[1]):
	pythonFile = open(sys.argv[1])
	pythonCode = pythonFile.read()
	pythonFile.close()

	javaMainClass = sys.argv[1].split(".py")[0]
	javaFile = open(javaMainClass + ".java", "w")

	openClass(javaFile, javaMainClass)

	javaCode = BlockReplacer.BlockReplacer().replace(pythonCode)
	tmp = ""
	for line in javaCode.split("\n"):
		for replacer in replacers:
			line = replacer.replace(line)
		javaFile.write(line + '\n')

	closeClass(javaFile)
	javaFile.close()


else:
	print(1)
