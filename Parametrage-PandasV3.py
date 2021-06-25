#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      thais
#
# Created:     15.06.2021
# Copyright:   (c) thais 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pandas
import numpy
import matplotlib.pyplot as plt #librairie pour les graphiquess
# installer avec pip ou l'invite de commande (cmd) matplotlib: pip install matplotlib

from tkinter import *
import random
from PIL import Image, ImageTk
import tkinter.scrolledtext as scrolledtext
from pandas import DataFrame
import googlemaps
import gmplot
import webbrowser
import easygui
import os.path


def __main__():
    pass
class FenetrePrincipal(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master, width = largeur, height = hauteur)
        self.pack()
        self.grid_propagate(0)
        self.varAn = "TOUT"
        self.varAr = "TOUT"
        self.df = ""
        self.volmin = ""
        self.volmax = ""
        self.vars = []
        self.file = "map"
        picks= ['CODE POSTAL', 'SOUS TYPE DECLARATION', 'CONSEIL DE QUARTIER','DATE DECLARATION','OUTIL SOURCE', 'INTERVENANT', 'ID_DMR', 'geo_point_2d']
        ligne = 1
        #column = 20
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var, command=self.state)
            #chk.pack(side=side, anchor=anchor, expand=YES)
            ligne += 1
            chk.grid(row = ligne, column =30, sticky = W)
            self.vars.append(var)
        self.Affichage()

    def state(self):
      #lambda var: var.get()), self.vars
      #print(lambda var: var.get())
      return map((lambda var: var.get()), self.vars)

    def change_vol(self,_=None):
        self.volmin = self.vmin.get()
        self.volmax = self.vmax.get()
        #print(self.volmin)
        #print(self.volmax)

    def saveFile(self):
        #Dialogs asking users to save file, sanity checks for existence of file, etc.
        #extension is the file's extension (txt, png, etc). It will automatically be added
        #to the filename specified by the user.

        #The function returns the filename specified by the user if one is specified or
        #None if the user cancels the operation for any reason.
        
        #If user cancels it defaults to the FIRST choice. We want default to be NO so I reverse the default of choices here. 

        extension ="html" 
        filename = self.file   
        filename = filename + "." + extension 
        #print(self.file)
        #print(filename)
        #saveornot = easygui.buttonbox(msg="Do you want to save results to a file?", choices = ("No", "Yes") )
        #if saveornot == "Yes":
        filename = easygui.filesavebox(msg = "Où voulez vous saufegarder le fichier %s ." %(filename))
        if filename is None:
            return None
        print(filename)
        if os.path.exists(filename):
            ok_to_overwrite = easygui.buttonbox(msg="Ficher %s déjà existant. Vous voulez l'écraser?" %(filename), choices = ("No", "Yes") )
            if ok_to_overwrite == "Yes":
                return filename
            else:
                return None
        else:
            return filename


    def OpenCarte(self):

            #Validation des valeur self.volmin et self.volmax pour voir s'il sont coehants
            if self.volmin > self.volmax:
                ## message / information to be displayed on the screen
                message = "La quantité minimal d'anomalies doit être inferieur ou eguale à la quantité maximale. Modifiez avant de relancer 'Carte'."
                # title of the window
                title = "Quantité Anomalie - Erreur"
                # text of the Ok button
                ok_btn_txt = "OK"
                # creating a message box
                output = easygui.msgbox(message, title, ok_btn_txt)
                return None


            pandas.options.display.max_rows = 10

            arrondisssement = self.varAr.get()
            anomalies = self.varAn.get()
            #print(arrondisssement)
            #print(anomalies)

            #clé pour l'api de google maps
            gmap = googlemaps.Client(key='AIzaSyDZ9dCd6qGze68sFqJgcnOIdKE8lI8gTBk')

            #coordonnées de Paris, 12 arrondissement
            gmap = gmplot.GoogleMapPlotter(48.866667, 2.333333, 12)

            #ouvrir une coordonnés en particulie
            # Mark le centre de Paris - 12 arrondissement
            gmap.marker(48.866667, 2.333333, color='cornflowerblue', title = "Paris - Centre")


            #filtrage des coordonnés par l'arrondissement
            if arrondisssement != "TOUT" and anomalies != "TOUT":
                #print("1")
                arrondisssement = int(arrondisssement)
                newdf = self.df.loc[(self.df['ARRONDISSEMENT']== arrondisssement) & (self.df['TYPE DECLARATION']==anomalies) ,:]
            elif arrondisssement == "TOUT" and anomalies == "TOUT":
                #sans filtre, on prend TOUT les arrondissements et TOUT les anomalies
                newdf = self.df
                #print("2")
            elif anomalies == "TOUT":
                arrondisssement = int(arrondisssement)
                newdf = self.df.loc[(self.df['ARRONDISSEMENT']==arrondisssement) ,:]
                #print("3")
            else:
                newdf = self.df.loc[(self.df['TYPE DECLARATION']==anomalies) ,:]
                #print("4")

            #Si le data frame est vide on peut rien montre et on n'ouvre pas googlemaps
            if not newdf.empty:

                lieux = []
                tag = []

                #On vérifie quel checkboxes on été ajoutées pour avoir les champs correspondant dans le dataframe et l'afficher sur la carte
                # 1 = checked
                # 0 = not checked
                #picks= ['CODE POSTAL', 'SOUS TYPE DECLARATION', 'CONSEIL DE CARTIER','DATE DECLARATION','OUTIL SOURCE', 'INTERVENANT', 'ID_DMR', 'geo_point_2d']
                switcher={

                        'PY_VAR0':'CODE POSTAL',
                        'PY_VAR1':'SOUS TYPE DECLARATION',
                        'PY_VAR2':'CONSEIL DE QUARTIER',
                        'PY_VAR3':'DATE DECLARATION',
                        'PY_VAR4':'OUTIL SOURCE',
                        'PY_VAR5':'INTERVENANT',
                        'PY_VAR6':'ID_DMR',
                        'PY_VAR7':'geo_point_2d'
                    }

                champs = []
                for var in self.vars:
                    if var.get() == 1:
                        champs.append(switcher.get(str(var)))
                        #print(champs)


                for index, row in newdf.iterrows():
                    lat, lng = row['geo_point_2d'].split(",")
                    complement_tag = ""
                    for champ in champs:
                        complement_tag +=  " " + champ + ": " + str(row[champ]) #+ "\n"
                        #print(complement_tag)
                    tag.append(row['TYPE DECLARATION'] + "- "  + "Arrondissement: " + str(row['ARRONDISSEMENT']) + complement_tag)
                    lieux.append((float(lat), float(lng)))


                attractions_lats, attractions_lngs = zip(*lieux)

                gmap.scatter(attractions_lats, attractions_lngs, color='red', size=40, marker=True, title = tag)

                #Heatmaps are effective visualization tools for representing different values of data over a specific geographical area.
                heatmap_layer = gmap.heatmap(attractions_lats, attractions_lngs)

                #attractions_lats = zip(*lieux)
                #gmap.polygon(*attractions_lats, color='cornflowerblue', edge_width=10) #'cornflowerblue'

                #Draw the map to an HTML file:
                gmap.draw("map.html")
                webbrowser.open("map.html")
            else:
                print("Rien a afficher pour les données selectionées")

    def Affichage(self):
        self.df = pandas.read_csv("dans-ma-rue.csv",sep = ";" ,header = 0)

        #on montre en ordre alphabetique
        self.df = self.df.sort_values(by ='TYPE DECLARATION' , ascending=True)

        listeAnomalie = self.df['TYPE DECLARATION'].unique()

        #on montre les arrondissement en ondre ascendente
        self.df = self.df.sort_values(by ='ARRONDISSEMENT' , ascending=True)

        listeArrondissement = self.df['ARRONDISSEMENT'].unique()

        #on cree en dictionnaire avec arrondissement(key) et point geographique(lieux)

        labelframe = LabelFrame(self, text="Filtres" , fg="grey", font='Calibri 13')
        #labelframe.grid(row=2)

        titre = Label(labelframe, text="Arrondissement:", fg="grey", font='Calibri 13')     #Libelé
        titre.grid(row=3, sticky=W, columnspan=50)

        #DropDown menu
        self.varAr= StringVar(labelframe)
        self.varAr.set("TOUT")
        deroulant = OptionMenu(labelframe, self.varAr, *listeArrondissement )
        deroulant.config(font=('Calibri',13),fg="white", bd = '15' ,width=2,height=1,bg="#778899",activebackground="#708090",activeforeground="#708090",relief="groove")
        deroulant.grid(row=3, sticky=W, column =50) #, sticky=W

        titre1 = Label(labelframe, text="Anomalies:", fg="grey", font='Calibri 13')     #Libelé
        titre1.grid(row=4, sticky=W, columnspan=10)

        #DropDown menu
        self.varAn= StringVar(labelframe)
        #var.set(listeAnomalie[0])
        self.varAn.set("TOUT")
        self.varAn.trace_add('write', lambda *args:listeAnomalie)
        deroulant2 = OptionMenu(labelframe, self.varAn, *listeAnomalie)
        deroulant2.config(font=('Calibri',13),fg="white", bd = '15' ,width=5,height=1,bg="#778899",activebackground="#708090",activeforeground="#708090",relief="groove")
        deroulant2.grid(row=4, sticky=W, column =50)  #, sticky=W)

        labelframe.grid(row=2, column =0)

        #sélection par quantité d'anomalie
        labelframe2 = LabelFrame(self, text="Quantité Anomalie" , fg="grey", font='Calibri 13')

        titre3 = Label(labelframe2, text="Min.", fg="grey", font='Calibri 13')     #Libelé
        titre3.grid(row=5, sticky=W, columnspan=10)

        titre4 = Label(labelframe2, text="Max.", fg="grey", font='Calibri 13')     #Libelé
        titre4.grid(row=6, sticky=W, columnspan=10)

        labelframe2.grid(row=2, column =7)


        self.vmin = Scale(labelframe2,from_ = 1,to = 1000, orient = HORIZONTAL ,command=self.change_vol, resolution = 100)
        self.vmin.grid(row = 5, column = 10)
        self.vmax = Scale(labelframe2,from_ = 1,to = 1000, orient = HORIZONTAL ,command=self.change_vol, resolution = 100)
        self.vmax.grid(row = 6, column = 10)

        Button(self, text="Carte",font=('Calibri',13),fg="white", bd = '12' ,width=8,bg="#778899",activebackground="#708090",activeforeground="#708090",relief="groove", command = self.OpenCarte).grid(row = 15, column = 0)
        Button(self, text="Exporter",font=('Calibri',13),fg="white", bd = '12' ,width=8,bg="#778899",activebackground="#708090",activeforeground="#708090",relief="groove", command = self.saveFile).grid(row = 15, column = 1)
        Button(self, text="Quitter",font=('Calibri',13),fg="white", bd = '12' ,width=8,bg="#778899",activebackground="#708090",activeforeground="#708090",relief="groove", command = main.destroy).grid(row = 16, column = 0)

        #Button(self, text="Importer en CSV",font=('Calibri',13),fg="white", bd = '10' ,width=22,height=1,bg="#E80062",activebackground="#FFC200",activeforeground="#E0F7FF",relief="groove", command = print("Importer")).grid(row = 0, column =0)
        #var = StringVar()
        #var.set('Choisir  le graphe')
        #Menu = OptionMenu(self, var, *Liste)
        #Menu.config(font=('Calibri',13),fg="white", bd = '10' ,width=24,height=1,bg="#00D1CA",activebackground="#00A700",activeforeground="#3C3C3C",relief="groove",)
        #Menu.grid(row = 0, column = 1)
        #Button(self, text="Lancer",font=('Calibri',13),fg="white", bd = '10' ,width=22,bg="#FFC200",activebackground="#FEFAC7",activeforeground="#3C3C3C",relief="groove", command = print("lancer")).grid(row = 0, column = 2)
        #Button(self, text ="Quitter",font=('Calibri',13),fg="white", bd = '10',width=22,bg="#0081CA",activebackground="#00D1CA",activeforeground="#E0F7FF",relief="groove", command = main.destroy).grid(row=0, column = 3)
        #Button(self,text="Play",font=('Calibri',13),fg="white", bd = '10' ,width=13,bg="#00A700",activebackground="#0081CA",activeforeground="#E0F7FF",relief="groove",command=self.play).place(x=300, y= 370)
        #Button(self,text="Pause",font=('Calibri',13),fg="#3C3C3C", bd = '10' ,width=13,bg="#FEFAC7",activebackground="#E80062",activeforeground="#E0F7FF",relief="groove",command=self.pause).place(x=450, y= 370)


main = Tk()
main.geometry('950x450')
largeur = main.winfo_screenwidth()
hauteur = main.winfo_screenheight()
main.minsize(950, 450)
main.maxsize(950, 450)
main.title("Dans ma Rue - Carte")
main.iconbitmap("MaRuelogo.ico")
FenetrePrincipal(master = main)
main.mainloop()

