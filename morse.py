#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
import sys, os, time
duration = 0.2  # second
freq = 440  # Hz

alphabet = {'a': '._', 'b': '_...', 'c': '_._.', 'd': '_..', 'e': '.', 'f': '.._.', 'g': '__.', 'h': '....', 
			'i': '..', 'j': '.___', 'k': '_._', 'l': '._..', 'm': '__', 'n': '_.', 'o': '___', 'p': '.__.', 
			'q': '__._', 'r': '._.', 's': '...', 't': '_', 'u': '.._', 'v': '..._', 'w': '.__', 'x': '_.._', 
			'y': '_.__', 'z': '__..', '1': '.____', '2': '..___', '3': '...__', '4': '...._', '5': '.....', 
			'6': '_....', '7': '__...', '8': '___.', '9': '____.', '0': '_____', ' ': '/'}

while True:
	msg = str(input("Ecrivez du code morse ou un texte (/q pour quitter):\n")).replace('-','_').replace('  ', '/')
	morse = ''
	if msg != '/q':
		try:
			# A -> .-
			for c in msg:
				morse  += alphabet[c.lower()] + ' '
			#print(morse)
			code = ""
			for c in morse:
				code += c
				sys.stdout.write("\r{}".format(code))
				if c == str('.'):
					time.sleep(0.5)
					duration = 0.5
				elif c == str('_'):
					time.sleep(1)
					duration = 1
				else:
					continue
			print("\n")
				# os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
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
		sys.exit(0)