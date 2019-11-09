#!/usr/bin/python
# vim: set fileencoding=utf-8 :
#Ducky
#09.November 2019
#Nützliche Funktionen fürs Hauptprogramm
from os import system, name
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

from time import sleep
