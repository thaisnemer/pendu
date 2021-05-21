#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Thomas
#
# Created:     18/05/2021
# Copyright:   (c) Thomas 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

from tkinter import *



def openGame ():
    lang = varL.get()

    if  lang == "Fr":

        #gameEN (window)
        gameWindow = Toplevel(main)
        gameWindow.title ("Hangman's Turf")
        gameWindow.config (bg = couleurBack)
        gameWindow.geometry ("1360x760")
        gameWindow.iconbitmap ("jeudupendufb.ico")
        gameWindow.minsize(largeurfinal,hauteurfinal)
        gameWindow.maxsize(largeurfinal,hauteurfinal)


        #Frame on the right side
        rightFrame = Frame(gameWindow,height = hauteurfinal, width = largeurfinal/4*3)
        rightFrame.grid(row = 0, column = 1, sticky = E)
        rightFrame.grid_propagate(0)

        #Frame on the left side
        leftFrame = Frame(gameWindow, bg = couleurBack, height = hauteurfinal, width=largeurfinal/4)
        leftFrame.grid(row = 0, column = 0)
        leftFrame.grid_propagate(0)


        testFrame= Frame(rightFrame, bg = couleurBack,height = hauteurfinal/2, width = largeurfinal/4*3)
        testFrame.grid(row = 0, column = 0)
        testFrame.grid_propagate(0)

        #Keyboard Frame placed in the bottom right corner
        keyboardFrame= Frame(rightFrame, bg = couleurBack,height = hauteurfinal/2, width = largeurfinal/4*3)
        keyboardFrame.grid(row = 1, column = 0)
        keyboardFrame.grid_propagate(0)



        theme = var.get()
        labeltheme = Label(leftFrame, text=theme, bg = couleurBack,fg =couleurFg)
        labeltheme.grid(row = 0, column = 0)
        labeltheme.grid_propagate(0)




        #keyboard
        ALPHA = "AZERTYUIOPQSDFGHJKLMWXCVBN"

        for premier in range(2):
                for second in range(10):
                    btn = Button (keyboardFrame,text=ALPHA[10*premier + second],font='times 35',bg = couleurBut,fg =couleurFg, activebackground = "red")
                    btn.grid(row=premier+2, column=second+2)


        for second in range(6):
            btn = Button(keyboardFrame, text=ALPHA[20 + second], font='Times 35',bg = couleurBut,fg =couleurFg, activebackground = "red")
            btn.grid(row=4, column=second + 4)


        #quit button of the game window
        quitButton2 = Button (keyboardFrame, text = "Quit", bg = couleurBut, font = 'Times 30',command = gameWindow.destroy, activebackground = "red", pady=10, padx = 30, bd = 1, fg=couleurFg, highlightthickness = 0)
        quitButton2.grid ( row = 5, column = 20)

    elif lang == "En":

        #gameEN (window)
        gameWindow = Toplevel(main)
        gameWindow.title ("Hangman's Turf")
        gameWindow.config (bg = couleurBack)
        gameWindow.geometry ("1360x760")
        gameWindow.iconbitmap ("jeudupendufb.ico")
        gameWindow.minsize(largeurfinal,hauteurfinal)
        gameWindow.maxsize(largeurfinal,hauteurfinal)


        #Frame on the right side
        rightFrame = Frame(gameWindow,height = hauteurfinal, width = largeurfinal/4*3)
        rightFrame.grid(row = 0, column = 1, sticky = E)
        rightFrame.grid_propagate(0)

        #Frame on the left side
        leftFrame = Frame(gameWindow, bg = couleurBack, height = hauteurfinal, width=largeurfinal/4)
        leftFrame.grid(row = 0, column = 0)
        leftFrame.grid_propagate(0)


        testFrame= Frame(rightFrame, bg = couleurBack,height = hauteurfinal/2, width = largeurfinal/4*3)
        testFrame.grid(row = 0, column = 0)
        testFrame.grid_propagate(0)

        #Keyboard Frame placed in the bottom right corner
        keyboardFrame= Frame(rightFrame, bg = couleurBack,height = hauteurfinal/2, width = largeurfinal/4*3)
        keyboardFrame.grid(row = 1, column = 0)
        keyboardFrame.grid_propagate(0)



        theme = var.get()
        labeltheme = Label(leftFrame, text=theme, bg = couleurBack,fg =couleurFg)
        labeltheme.grid(row = 0, column = 0)
        labeltheme.grid_propagate(0)




        #keyboard
        ALPHA = "QWERTYUIOPASDFGHJKLZXCVBNM"

        for premier in range(2):
                for second in range(10):
                    btn = Button (keyboardFrame,text=ALPHA[10*premier + second],font='times 35',bg = couleurBut,fg =couleurFg, activebackground = "red")
                    btn.grid(row=premier+2, column=second+2)


        for second in range(7):
            btn = Button(keyboardFrame, text=ALPHA[20 + second], font='Times 35',bg = couleurBut,fg =couleurFg, activebackground = "red")
            btn.grid(row=4, column=second + 4)


        #quit button of the game window
        quitButton2 = Button (keyboardFrame, text = "Quit", bg = couleurBut, font = 'Times 30',command = gameWindow.destroy, activebackground = "red", pady=10, padx = 30, bd = 1, fg=couleurFg, highlightthickness = 0)
        quitButton2.grid ( row = 5, column = 20)

def rules():
    lang = varL.get()
    if lang == "Fr":

        règlesEn.config(fg =couleurBack )
        règles.config(fg =couleurFg )
    else:
        règles.config(fg = couleurBack)
        règlesEn.config(fg=couleurFg)

def credits():


    creditswindow = Toplevel(main)
    creditswindow.geometry("720x480")
    creditswindow.minsize(int(largeurfinal/2),int(hauteurfinal/2))
    creditswindow.maxsize(int(largeurfinal/2),int(hauteurfinal/2))
    creditswindow.config(bg=couleurBack)
    creditswindow.iconbitmap ("jeudupendufb.ico")


    creditsLabel = Label(creditswindow, text="créé par:\n\nAdam\nAzadeh\nThais\nHanan\nThomas", fg=couleurFg, bg = couleurBack)
    creditsLabel.pack()

    quitButCredits = Button(creditswindow,text = "Quit", command = creditswindow.destroy, bg = couleurBut, fg = couleurFg, activebackground = "red", pady = 10, padx = 30)
    quitButCredits.pack(side = "bottom")


couleurBack = '#9a9c91'
couleurBut = "#71716f"
couleurFg = "#bd2013"


#main window
main = Tk()
main.iconbitmap ("jeudupendufb.ico")
main.config (background = couleurBack)
main.title ("Hangman")
main.geometry("1360x760")
largeur = main.winfo_screenwidth()
hauteur = main.winfo_screenheight()
largeurfinal = int(largeur / 4 * 3)
hauteurfinal = int(hauteur / 4 * 3)
main.minsize(largeurfinal,hauteurfinal)
main.maxsize(largeurfinal,hauteurfinal)


#detecteur de fenetre ouverte
##windowGame = False
##windowRules = False
##windowCredits = False






label = Label (main, text = "Welcome to Hangman's game",font =("courrier",20), bg =couleurBack, fg = couleurFg)
label.pack (expand = YES)


quitBut = Button (main, text = "Quit", command = main.destroy, bg = couleurBut,pady = 10, padx = 30, activebackground = "red", fg=couleurFg)
quitBut.pack (side = "bottom", expand = YES)

butCredits = Button(main, text = "Credits",command = credits, bg = couleurBut, fg =couleurFg,pady = 10, padx = 26, activebackground = "red")
butCredits.pack(side="bottom", expand = YES)

butRules = Button(main, command = rules, text = "Rules", pady = 10, padx = 30, activebackground = "red", fg=couleurFg, bg = couleurBut)
butRules.pack(side = "bottom", expand = YES)

but = Button (main, text = "Start", command = openGame, bg=couleurBut, pady=10, padx = 30, bd = 1, activebackground = "red", fg=couleurFg)
but.pack (side = "bottom", expand = YES)

règles = Label(main, text = "Règles du jeu du Pendu :\n\nCliquez sur Start pour commencer une nouvelle partie. \nCliquez sur les lettres en bas que vous souhaitez proposer dans le mot. \nPour chaque lettre non présente dans le mot, le dessin du pendu s'affichera.\nLe but étant de ne pas se faire pendre.", bg = couleurBack, font = ("Courrier", 15), fg =couleurBack)
règles.pack(side = "top", expand = YES)


règlesEn = Label(main, text = "Hangman Rules :\n\nPress start to begin. \nChoose a letter to see if the letter appears in the word.\nIf the letter does not appear in the word, a part of the hangman appears.\nThe goal is to guess the word and avoid being hanged.", bg = couleurBack, font = ("Courrier", 15), fg =couleurBack)
règlesEn.pack(side = "top", expand = YES)


#dropdown for language
varL=StringVar(main)
varL.set("Fr")
déroulantL= OptionMenu(main, varL,"Fr","En")
déroulantL.config(bg = couleurBack,bd = 0,highlightthickness=1, activebackground = couleurBack, fg = couleurFg, justify = "center",highlightbackground = couleurBut)
déroulantL.pack(side="bottom")




var= StringVar(main)
var.set("Cinéma")
#DropDown menu
deroulant = OptionMenu(main, var, "Cinéma", "Sport", "Capitales")
deroulant.config(bg = couleurBack,bd = 0,highlightthickness=1, activebackground = couleurBack, fg = couleurFg, justify = "center",highlightbackground = couleurBut)
deroulant.pack(side = "bottom")

labelTheme = Label(main, text = "Thêmes:", bg=couleurBack, fg = couleurFg, font = 'times 15')
labelTheme.pack(side = "bottom")


main.mainloop()







