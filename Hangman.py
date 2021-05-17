#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Thomas
#
# Created:     11/05/2021
# Copyright:   (c) Thomas 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

from tkinter import *

def openGame ():

    #game (window)
    gameWindow = Toplevel(main)
    gameWindow.title ("Hangman's Turf")
    gameWindow.config (bg = "#9a9c91")
    gameWindow.geometry ("720x480")
    gameWindow.iconbitmap ("jeudupendufb.ico")
    gameWindow.minsize(720,480)



    theme = var.get()
    labeltheme = Label(gameWindow, text=theme, bg = "#9a9c91")
    labeltheme.grid(row = 0, column = 0)

    #keyboard
    ALPHA = "AZERTYUIOPQSDFGHJKLMWXCVBN"

    for premier in range(2):
            for second in range(10):
                btn = Button (gameWindow,text=ALPHA[10 * premier + second],relief=FLAT,font='times 20',bd = 1, highlightthickness = 1,bg = "#9a9c91",activebackground = "red")
                btn.grid(row=premier+2, column=second+2)


    for second in range(6):
        btn = Button(
        gameWindow, text=ALPHA[20 + second], relief=FLAT, font='Times 20',bg = "#9a9c91", activebackground = "red")
        btn.grid(row=4, column=second + 4)


    #quit button of the game window
    quitButton2 = Button (gameWindow, text = "Quit", bg = "#71716f", command = gameWindow.destroy, activebackground = "red", pady=10, padx = 30, bd = 1, fg="#bd2013", highlightthickness = 0)
    quitButton2.grid (row=8,column = 8)



#main window
main = Tk()
main.iconbitmap ("jeudupendufb.ico")
main.config (background = '#9a9c91')
main.title ("Hangman")
main.geometry("1360x760")
main.minsize(720,480)

#Dropdown menu list

var= StringVar(main)
var.set("Cinéma")
#DropDown menu
deroulant = OptionMenu(main, var, "Cinéma", "Sport", "Capitales")
deroulant.pack()





label = Label (main, text = "Welcome to Hangman's game",font =("courrier",20), bg ="#9a9c91", fg = "#bd2013")
label.pack (expand = YES)

quitBut = Button (text = "Quit", command = main.destroy, bg = "#71716f",pady = 10, padx = 30, activebackground = "red", fg="#bd2013")
quitBut.pack (side = "bottom", expand = YES)

but = Button (text = "Start", command = openGame, bg="#71716f", pady=10, padx = 30, bd = 1, activebackground = "red", fg="#bd2013")
but.pack (side = "bottom", expand = YES)

règles = Label(text = "Règles du jeu du Pendu :\n\nCliquez sur Start pour commencer une nouvelle partie \nCliquez sur les lettres en bas que vous souhaitez proposer dans le mot \nPour chaque lettre non présente dans le mot, le dessin du pendu s'affichera,le but étant de ne pas se faire pendre", bg = "#9a9c91", font = ("Courrier", 15), fg ="#bd2013")
règles.pack(side = "top", expand = YES)




main.mainloop()



















































