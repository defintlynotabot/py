#!/usr/bin/python
# vim: set fileencoding=utf-8 :
#Ducky
#09.November 2019
#Davids Top-Programm
#Changelog: Banner, Datenauswertung
import f, vigenere, wartezimmer, datenAuswertung
while 1:
    print("""
     ____  _  _  ____  _   _  _____  _  _   
    (  _ \( \/ )(_  _)( )_( )(  _  )( \( )  
     )___/ \  /   )(   ) _ (  )(_)(  )  (   
    (__)   (__)  (__) (_) (_)(_____)(_)\_)  
     _    _  _____  ____  __    ____        
    ( \/\/ )(  _  )(  _ \(  )  (  _ \       
     )    (  )(_)(  )   / )(__  )(_) )      
    (__/\__)(_____)(_)\_)(____)(____/     
                                    Ducky, Anon
    """)
    print("""
    (1) Vigenere Ver- und Entschlüsselung
    (2) Virtuelles Wartezimmer
    (3) Datenauswertung
    (x) Exit
    """)
    eingabe=input("Wählen Sie ein Programm aus :")
    if eingabe is "1":
        f.clear()
        vigenere.start()
        f.clear()
##############################################
    if eingabe is "2":
        f.clear()
        wartezimmer.start()
        f.clear()
###############################################
    if eingabe is "3":
        f.clear()
        datenAuswertung.start()
        f.clear()
###############################################
    if eingabe is "x":
        f.clear()
        print("goodbye")
        break
