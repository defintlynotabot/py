#!/usr/bin/python
# vim: set fileencoding=utf-8 :
#Ducky
#09.11.2019
#Wartezimmer
#Einbindung in Top-Programm
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
        logo()
        eingabe=input("""
(a) Leutis hinzufügen.
(b) Leutis aufrufen.
(c) Liste anzeigen.
(d) Person suchen.
(e) Allah, ich kann nicht mehr zu meinem Termin erscheinen
(f) Ich will hier raus!

""")
        if eingabe == "a":
            print()
            name=input("Geben sie einen Namen ein :")
            waslos=input("Geben sie einen Grund ein :")
            tupel=(name,waslos)
            liste.append(tupel)
        elif eingabe == "b":
            print()
            print("Patient", liste[0][0], "mit", liste[0][1],
                  "wird aufgerufen und aus der Warteschlange entfernt.")
            print()
            del liste[0]
        elif eingabe == "c":
            count=1
            for i in liste:
                print(count, ":", i[0], "mit", i[1])
                count=count+1
        elif eingabe == "d":
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
        elif eingabe == "e":
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
        elif eingabe == "f":
            break
        else:
            print()
            print("FALSCHE EINGABE!")
        
            
