# exitExample.py
# AtBS - Chapter 2
# Code by Darrell Dudics

import sys

while True:
	print('Type exit to exit.')
	response = input()
	
	if response == 'exit':
		sys.exit()
		
	print('You typed ' + response + '.')
