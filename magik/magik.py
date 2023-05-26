#!/usr/bin/python3
from basic_execute import BasicExecute
from basic_lexer import BasicLexer
from basic_parser import BasicParser

if __name__ == '__main__':
	lexer = BasicLexer()
	parser = BasicParser()
	print('OpenMagik')
	env = {}
	
	while True:
		
		try:
			text = input('OpenMagik> ')
		
		except EOFError:
			break
		
		if text:
			tree = parser.parse(lexer.tokenize(text))
			BasicExecute(tree, env)
