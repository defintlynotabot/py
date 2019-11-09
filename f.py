#!/usr/bin/python
# vim: set fileencoding=utf-8 :
#Ducky
#09.November 2019
#Nützliche Funktionen fürs Hauptprogramm
from os import system, name #Name des Operating-Systems erhalten
def clear():
	if name == 'nt': #Wenn Windows, cls- Befehl ausführen
		_ = system('cls')
	else: #Unter anderen Plattformen (Linux), clear
		_ = system('clear')

from time import sleep #sleep(seconds) zulassen
