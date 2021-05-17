#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      thais
#
# Created:     13.05.2021
# Copyright:   (c) thais 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import csv

def main():
    pass

if __name__ == '__main__':
    main()

DicCapitales = {}

def LireFichierCapitales(fichier):
    """Docstring: Function qui reçoit un fichier csv et le lit et écrit son contenu dans un dictionnaire"""
    with open(fichier, newline='', encoding="utf8", errors='ignore') as csvfile:
       reader = csv.DictReader(csvfile)
       for row in reader:
            #print(row['Capitale'], row['Pays'])
            CreationDictionnaire(row['Pays'], row['Capitale'])

    DicCapitales.keys()
    print(DicCapitales)


def CreationDictionnaire(dicKey, dicValue):
    """Docstring: Creation dans un dictionnaire a partir d'une clef et son valeur"""
    DicCapitales[dicKey] = dicValue

LireFichierCapitales("liste_des_capitales.csv")

#print(DicCapitales.get("Malte"))




