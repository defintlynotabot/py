#!/usr/bin/python
# vim: set fileencoding=utf-8 :
#Ducky
#09.November 2019
#Davids Top-Programm
import f, vigenere, wartezimmer
while 1:
    print("""
     ____    __  _  _  ____  ____    /___   
    (  _ \  /__\( \/ )(_  _)(  _ \   / __)  
     )(_) )/(__)\\  /  _)(_  )(_) )  \__ \  
    (____/(__)(__)\/  (____)(____/   (___/  
     ____  _  _  ____  _   _  _____  _  _   
    (  _ \( \/ )(_  _)( )_( )(  _  )( \( )  
     )___/ \  /   )(   ) _ (  )(_)(  )  (   
    (__)   (__)  (__) (_) (_)(_____)(_)\_)  
     _    _  _____  ____  __    ____        
    ( \/\/ )(  _  )(  _ \(  )  (  _ \       
     )    (  )(_)(  )   / )(__  )(_) )      
    (__/\__)(_____)(_)\_)(____)(____/     
      
    """)
    print("""
    (1) Vigenere Ver- und Entschlüsselung
    (2) Virtuelles Wartezimmer
    (x) Exit
    """)
    eingabe=input("Wählen Sie ein Programm aus :")
    if eingabe is "1":
        f.clear()
        vigenere.start()
        f.clear()
###############################################
    if eingabe is "2":
        f.clear
        wartezimmer.start()
        f.clear()
###############################################
    if eingabe is "x":
        f.clear()
        print("goodbye")
        break
