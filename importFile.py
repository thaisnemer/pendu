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
DicPlanetes = {}

def LireFichierPlanetes(fichier):
    """Function qui reçoit un fichier text, le lit et écrit son contenu dans une liste"""
    f = open(fichier,'r')
    # utilisez readline() pour lire la première ligne
    line = f.readline()
    index = 0
    while line:
        #enleves les \n de chaque fin de ligne
        line = line.rstrip()
        #on cree notre diccionnaire avec key = index et value = planete
        DicPlanetes[index] = line
        # utilisez readline() pour lire la ligne suivante
        index += 1
        line = f.readline()
    f.close()
    return DicPlanetes


def LireFichierCapitales(fichier):
    """Function qui reçoit un fichier csv, le lit et écrit son contenu dans un dictionnaire"""
    with open(fichier, newline='', encoding="utf8", errors='ignore') as csvfile:
       reader = csv.DictReader(csvfile)
       for row in reader:
            #print(row['Capitale'], row['Pays'])
            CreationDictionnaire(row['Pays'], row['Capitale'])

    return DicCapitales

def CreationDictionnaire(dicKey, dicValue):
    """Docstring: Creation dans un dictionnaire a partir d'une clef et son valeur"""

    #si il y a des espace dans la Capitale(dicValue) on n'ajoute pas au dictionnaire
    index = dicValue.find(" ")

    indexCar = dicValue.find("?")
    #si ça retourne -1 ça veut dire qu'il n'a pas d'espace y on peut ajouter la capitale aux dictionnaire

    #si le Mot a plus de 10 characters, c'est trop grand pour être afficher(la fin est coupé), alors on les enleves de notre dictonnaire des capitales
    if len(dicValue) < 11 and index == -1 and indexCar ==-1:
        DicCapitales[dicKey] = dicValue


#print(LireFichierCapitales("liste_des_capitales.csv"))
#print(LireFichierPlanetes("Planetes.txt"))

