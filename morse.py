#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

from sys import stdout, exit
from time import sleep
duration = 0.3  # second
freq = 440  # Hz

dot = duration
dash = 3 * dot

alphabet = {'a': '._', 'b': '_...', 'c': '_._.', 'd': '_..', 'e': '.', 'f': '.._.', 'g': '__.', 'h': '....', 
			'i': '..', 'j': '.___', 'k': '_._', 'l': '._..', 'm': '__', 'n': '_.', 'o': '___', 'p': '.__.', 
			'q': '__._', 'r': '._.', 's': '...', 't': '_', 'u': '.._', 'v': '..._', 'w': '.__', 'x': '_.._', 
			'y': '_.__', 'z': '__..', '1': '.____', '2': '..___', '3': '...__', '4': '...._', '5': '.....', 
			'6': '_....', '7': '__...', '8': '___.', '9': '____.', '0': '_____', ' ': '/'}

replaceMap = [('-', '_'), ('–', '_'), ('—', '_'), ('•', '.'), ('  ', '/')]

while True:
	msg = str(input("Ecrivez du code morse ou un texte (/q pour quitter):\n"))

	for c, r in replaceMap:
		msg = msg.replace(c, r)
	morse = ''

	if msg != '/q':
		try:
			# A -> .-
			for c in msg:
				morse  += alphabet[c.lower()] + ' '
			code = ""
			for c in morse:
				code += c
				stdout.write("\r{}".format(code))
				if c == str('.'):
					sleep(dot)
					duration = dot
				elif c == str('_'):
					sleep(dash)
					duration = dash
				elif c == str(' '):
					sleep(dash)
					duration = dash
				elif c == str('/'):
					sleep(dot)
					duration = dot
				else:
					continue
			print('\n')

		except KeyError:
			# .- -> A
			for word in msg.split('/'):
				for c in word.split(' '):
					for key, value in alphabet.items():
						if value == c:
							morse += key
				morse += ' '
			print(morse)
	else:
		exit(0)
