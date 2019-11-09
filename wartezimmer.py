#!/usr/bin/python
# vim: set fileencoding=utf-8 :
#Ducky
#10.11.2019
#Wartezimmer
#Einbindung in Top-Programm
import f
def logo():
    print("""

 **       **                    **                
/**      /**                   /**                
/**   *  /**  ******   ****** ******  *****       
/**  *** /** //////** //**//*///**/  **///** *****
/** **/**/**  *******  /** /   /**  /*******///// 
/**** //**** **////**  /**     /**  /**////       
/**/   ///**//********/***     //** //******      
//       //  //////// ///       //   //////       
        **                                        
       //                                         
 ****** ** **********  **********   *****  ****** 
////** /**//**//**//**//**//**//** **///**//**//* 
   **  /** /** /** /** /** /** /**/******* /** /  
  **   /** /** /** /** /** /** /**/**////  /**    
 ******/** *** /** /** *** /** /**//******/***    
////// // ///  //  // ///  //  //  ////// ///     
""")
def start():
    liste=[]
    while 1:
        f.clear()
        logo()
        eingabe=input("""
(1) Leute hinzufügen
(2) Leutis aufrufen
(3) Liste anzeigen
(4) Person suchen
(5) Aus Liste streichen
(x) Exit

""")
        if eingabe == "1":
            print()
            name=input("Geben sie einen Namen ein :")
            waslos=input("Geben sie einen Grund ein :")
            tupel=(name,waslos)
            liste.append(tupel)
        elif eingabe == "2":
            print()
            print("Patient", liste[0][0], "mit", liste[0][1],
                  "wird aufgerufen und aus der Warteschlange entfernt.")
            print()
            del liste[0]
        elif eingabe == "3":
            count=1
            for i in liste:
                print(count, ":", i[0], "mit", i[1])
                count=count+1
            input()
        elif eingabe == "4":
            suche=input("Geben sie ihren zu suchenden Namen KORREKT ein :")
            counter=0
            for i in liste:
                if suche == liste[counter][0]:
                    print()
                    print("Gefunden!")
                    print("Die Person ist im Wartezimmer mit", liste[counter][1])
                    break
                elif suche != liste[counter][0]:
                    counter=counter+1
        elif eingabe == "5":
            suche=input("Geben sie ihren zu suchenden Namen KORREKT ein :")
            counter=0
            for i in liste:
                if suche == liste[counter][0]:
                    print()
                    print("Gefunden und gelöscht.")
                    del liste[counter]
                    break
                elif suche != liste[counter][0]:
                    counter=counter+1
                print("Der angegebene Name wurde nicht gefunden.")
                input()
        elif eingabe == "x":
            break
        else:
            print()
            print("FALSCHE EINGABE!")
        
            
