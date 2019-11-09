#!/usr/bin/python
# vim: set fileencoding=utf-8 :
#Ducky
#9.November 2019
# En- and Decoding with Vigenere-Chiffre
import f
text1="" #Output
def logo():
                        print("""
     **      ** **                                                
    /**     /**//   *****                                         
    /**     /** ** **///**  *****  *******   *****  ******  ***** 
    //**    ** /**/**  /** **///**//**///** **///**//**//* **///**
     //**  **  /**//******/******* /**  /**/******* /** / /*******
      //****   /** /////**/**////  /**  /**/**////  /**   /**//// 
       //**    /**  ***** //****** ***  /**//******/***   //******
        //     //  /////   ////// ///   //  ////// ///     ////// 
    """)

def start():
    global text1
    global txt
    global key
    logo()
    firstinput()
    f.clear
    exit=0
    while exit == 0:
            f.clear()
            logo()
            print("""
            Verschlüsseln               (1)
            Entschlüsseln               (2)
            Zwischenspeicher anzeigen   (3)
            Ergebnis als Text benutzten (4)
            Zwischenspeicher exportieren(5)
            Text(.txt) einlesen         (6)
            Neu                         (7)
            Exit                        (8)

            """)
            eingabe=input()
            if eingabe is "1":
                encode()
                input()
            elif eingabe is "2":
                decode()
                input()
            elif eingabe is "3":
                printoutput()
                input()
            elif eingabe is "4":
                switch()
                input()
            elif eingabe is "5":
                export()
                print("Erflogreich als vigenereExport.txt exportiert.")
                input()
            elif eingabe is "6":
                filename=input("Geben Sie den Dateinamen im Verzeichnis an :")
                imprt(filename)
            elif eingabe is "7":
                firstinput()
            elif eingabe is "8":
                break
def firstinput():
    global key
    global txt
    global text1
    key=input("Geben Sie den Schlüssel ein :")
    txt=input("Geben Sie den zu Ver-/Entschlüsselnden Text ein :")
    text1="" #Output
    
def clear(): #Output löschen
    global text1
    if text1 is not "":
        ask=input("Wollen sie den Zwischenspeicher leeren (y/n) :")
        if ask is "y" or ask is "Y":
            text1=""
            print("Der Zwischenspeicher wurde gelöscht.")
        elif ask is "n" or ask is "N":
            print("Dann halt nicht.")



def encode(): #Verschlüsselung
    global text1
    global txt
    clear()
    count=0 #Counter für den wiederholenden Schlüssel
    for i in range(0, len(txt)): #Wiederholung für jede Stelle des Textes
        
        if count == len(key): #Wenn der Schlüssel an letzter Stelle benutzt wurde
            count=0
        a=key[count] #a ist der Schlüssel an einer Stelle count
        b=txt[i]    #b der Text an einer Stelle i
        if ord(a)>90: #wenn der Buchstabe klein ist, mach ihn groß
            a=chr(ord(a)-32)
        if ord(b)>90: #"
            b=chr(ord(b)-32)
        c=ord(a)-64+ord(b)#addiere beide Großbuchstaben, ziehe 64 ab
        if c > 90: #Wenn Ergebnis über "z", ziehe 26 ab
            c=c-26
        text1=text1+chr(c) #Füge das Ergebnis dem Output hinzu
        count+=1
    print("Zwischenspeicher :", text1)
    
def decode(): #Entschlüsselung
    count=0
    global text1
    global txt
    global key
    clear()
    for i in range(0, len(txt)): #Wiederholung len(txt)-mal
        if count == len(key): #Wenn Schlüssel vollständig genutzt, setze counter zurück
            count=0
        a=key[count] #a ist der Schlüssel an Stelle [count]
        b=txt[i]    #b ist der Text an Stelle [i] (des Durchlaufs)
        if ord(a)>90: #wenn der Buchstabe klein ist, mach ihn groß
            a=chr(ord(a)-32)
        if ord(b)>90: #"
            b=chr(ord(b)-32)
        c=ord(b)-ord(a)+64 #Subtrahiere a von b; den Schlüssel vom Text
        if c < 65: #Wenn Ergebnis kleiner als "A", addiere 26
            c=c+26
        text1=text1+chr(c) #Füge das Ergebnis dem Output hinzu
        count+=1
    print("Zwischenspeicher :", text1)
    
def printoutput(): #Output ausgeben
    global text1
    print("Output :")
    print(text1)
    
def switch(): #Den Output als Text definieren
    global txt
    txt=text1
    print("Der Zwischenspeicher ist jetzt der Text.")
    
def export():
    global text1
    exp=open("vigenereExport.txt", "a")
    exp.write(text1)
    
def imprt(filename):
    global text1
    imp=open(filename, "r")
    text1=imp.read()
