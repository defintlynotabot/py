#!/usr/bin/python
# vim: set fileencoding=utf-8 :
#Anon(Creator), Ducky
#09.November 2019
#Datenauswertung
#Changelog: Kopfzeile, 'Start', f.clear()
def number_input():
  number_list = []
  print("Gib alle Werte nacheinander ein!")
  print("Wenn du fertig bist gib finish ein!")
  while True:
    number = input()
    try:
      float(number)
    except ValueError:
      if number == "finish":
        break
      else:
        print("Gib eine Zahl ein!")
        continue
    number_list.append(float(number))
  number_list = bubble_sort(number_list)
  print ("------------------------------------------------------------")
  print("Die Liste ist:",number_list)
  return number_list

def main(number_list):
  while True:
    print ("------------------------------------------------------------")
    auswahl = input("Gib 0 ein um die Befehle anzeigen zu lassen: ")

    try:
      auswahl = int (auswahl)

    except ValueError:
      print ("Das ist kein gültiger Befehl!")
      continue

    if auswahl == 0:
        print ("""
1 = Beenden
2 = Alle Befehle
3 = Summe
5 = Spannweite
6 = Länge
7 = Durchschnitt
8 = Varianz
9 = Standartabweichung
10 = Median
11 = Modalwert
12 = mittlere liniare Abweichung
13 = unteres Quartil
14 = oberes Quartil
""")

    elif auswahl == 1:
      break

    elif auswahl == 2:
      value = Summe(number_list)
      print("Summe: "+str(value))
      value = minimum(number_list)
      print("Minimum: "+str(value))
      value = maximum(number_list)
      print("Maximum: "+str(value))
      value = Spannweite(number_list)
      print("Spannweite: "+str(value))
      value = Länge(number_list)
      print("Länge: "+str(value))
      value = Durchschnitt(number_list)
      print("Durchschnitt: "+str(value))
      value = Varianz(number_list)
      print("Varianz: "+str(value))
      value = Standartabweichung(number_list)
      print("Standartabweichung: "+str(value))
      value = Median(number_list)
      print("Median: "+str(value))
      value = Modalwert(number_list)
      print("Modalwert: "+str(value))
      value = mittlere_liniare_Abweichung(number_list)
      print("mittlere liniare Abweichung: "+str(value))
      value = unteres_Quartil(number_list)
      print("unteres Quartiel: "+str(value))
      value = oberes_Quartil(number_list)
      print("oberes Quartiel: "+str(value))

    elif auswahl == 3:
      value = Summe(number_list)
      print("Summe: "+str(value))

    elif auswahl == 4:
      value = minimum(number_list)
      print("Minimum: "+str(value))
      value = maximum(number_list)
      print("Maximum: "+str(value))

    elif auswahl == 5:
      value = Spannweite(number_list)
      print("Spannweite: "+str(value))
      
    elif auswahl == 6:
      value = Länge(number_list)
      print("Länge: "+str(value))
      
    elif auswahl == 7:
      value = Durchschnitt(number_list)
      print("Durchschnitt: "+str(value))
      
    elif auswahl == 8:
      value = Varianz(number_list)
      print("Varianz: "+str(value))

    elif auswahl == 9:
      value = Standartabweichung(number_list)
      print("Standartabweichung: "+str(value))

    elif auswahl == 10:
      value = Median(number_list)
      print("Median: "+str(value))

    elif auswahl == 11:
      value = Modalwert(number_list)
      print("Modalwert: "+str(value))

    elif auswahl == 12:
      value = mittlere_liniare_Abweichung(number_list)
      print("mittlere liniare Abweichung: "+str(value))

    elif auswahl == 13:
      value = unteres_Quartil(number_list)
      print("unteres Quartiel: "+str(value))

    elif auswahl == 14:
      value = oberes_Quartil(number_list)
      print("oberes Quartiel: "+str(value))

    elif auswahl == 100:
      number_list = number_input()
      number_list = bubble_sort(number_list)
      
    else:
      print("Das ist kein gültiger Befehl!")

def bubble_sort(number_list):
  for i in range(len(number_list)):
      for j in range(len(number_list)-i-1):
        if number_list[j] > number_list[j+1] :
          number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
  return number_list

def Summe (number_list):
  first_time = True
  for i in number_list:
    if first_time == True:
      summe = i
      first_time = False
    else:
      summe = summe + i
  return summe

def minimum (number_list):
  return number_list[0]

def maximum (number_list):
  return number_list[-1]

def Spannweite (number_list):
  value = number_list[-1] - number_list[0]
  return value

def Länge (number_list):
  return len(number_list)

def Durchschnitt (number_list):
  value = Summe(number_list)/len(number_list)
  return value

def Varianz (number_list):
  mittel = Durchschnitt(number_list)
  first_time = True
  for i in number_list:
    if first_time == True:
      summe = (i-mittel)**2
      first_time = False
    else:
      summe = summe + ((i-mittel)**2)
  value = summe/len(number_list)
  return value

def Standartabweichung (number_list):
  value = Varianz(number_list)**(1/2)
  return value

def Median (number_list):
  if len (number_list)%2 == 1:
    median = number_list[int(len(number_list)/2)]
    return median
  elif len (number_list)%2 == 0:
    median = (number_list[int(len(number_list)/2)-1] + number_list[int(len(number_list)/2)]) /2
    return median

def Modalwert (number_list):
  counter = 0
  backup_counter = 0
  zahl = []
  for i in range(len(number_list)-1):
    if number_list[i] == number_list[i+1]:
      counter = counter + 1
    else:
      if backup_counter < counter:
        zahl = []
        zahl.append(number_list[i])
        backup_counter = counter
      elif backup_counter == counter:
        zahl.append(number_list[i])
      counter = 0
  if backup_counter == 0:
    zahl.append(number_list[-1])
  return zahl

def mittlere_liniare_Abweichung (number_list):
  mittel = Durchschnitt(number_list)
  first_time = True
  for i in number_list:
    if first_time == True:
      summe = i-mittel
      first_time = False
    else:
      summe = summe + (i-mittel)
  value = summe/len(number_list)
  return value

def unteres_Quartil (number_list):
  quartiel_list = []
  if len(number_list)%2 == 1:
    for i in range(int(len(number_list)/2)+1):
      quartiel_list.append(number_list[i])

  elif len(number_list)%2 == 0:
    for i in range(int(len(number_list)/2)):
      quartiel_list.append(number_list[i])

  value = Median(quartiel_list)
  return value
    
def oberes_Quartil (number_list):
  quartiel_list = []
  if len(number_list)%2 == 1:
    for i in range(1,int(len(number_list)/2)+2):
      quartiel_list.append(number_list[-i])

  elif len(number_list)%2 == 0:
    for i in range(1,int(len(number_list)/2)+1):
      quartiel_list.append(number_list[-i])

  value = Median(quartiel_list)
  return value

def start():
	print(""" 
		 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
		 |D|a|t|e|n|a|u|s|w|e|r|t|u|n|g|
		 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
			             |b|y| |A|n|o|n|
			             +-+-+ +-+-+-+-+
		""")
	number_list = number_input()
	main(number_list)

if __name__ == "__main__":
  number_list = number_input()
  main(number_list)
