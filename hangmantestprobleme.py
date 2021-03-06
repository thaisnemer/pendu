from tkinter import *
from PIL import Image, ImageTk
import random
import importFile as iFile
import csv

liste = []
#----------------------------------------------------------------------------------------------------------------------------------------------------
#command linked to keyboard
def btn_command(btn):
    if btn in liste:
        pass
    else:
        liste.append(btn)
    labelRe = StringVar()
    labelRe.set(liste)
    labelReponse = Label(testFrame, textvariable = labelRe, bg = couleurBack, fg = couleurFg)
    labelReponse.grid(row=1, column = 0)
    return btn
#----------------------------------------------------------------------------------------------------------------------------------------------------
#second window(game window)
def openGame ():  
    dico = iFile.LireFichierCapitales("C:/Users/Thomas/Desktop/exercice du jour/pendu/liste_des_capitales.csv")
    print(dico[0])




    # word = random.choice(list(DicCapitales.values()))
    # print(word)


    # dico = iFile.LireFichierCapitales("C:/Users/Thomas/Desktop/exercice du jour/pendu/liste_des_capitales")
    # a = random.randint(0,len(dico)-1)
    # motchoisi=dico[(a)]
    global testFrame
    lang = varL.get()
#---------------------------------------------------------------------------------Fr-----------------------------------------------------------------    
    if  lang == "Fr":

        #gameEN (window)
        gameWindow = Toplevel(main)
        gameWindow.title ("Hangman's Turf")
        gameWindow.config (bg = couleurBack)
        gameWindow.geometry ("1360x760")
        gameWindow.iconbitmap ("C:/Users/Thomas/Desktop/exercice du jour/pendu/jeudupendufb.ico")
        gameWindow.minsize(largeurfinal,hauteurfinal)
        gameWindow.maxsize(largeurfinal,hauteurfinal)

        
        #Frame right
        rightFrame = Frame(gameWindow,height = hauteurfinal, width = largeurfinal/2)
        rightFrame.grid(row = 0, column = 1)
        rightFrame.grid_propagate(0)

        #Frame left
        leftFrame = Frame(gameWindow, bg = couleurBack, height = hauteurfinal, width=largeurfinal/2)
        leftFrame.grid(row = 0, column = 0)
        leftFrame.grid_propagate(0)

        #Frame top right
        testFrame= Frame(rightFrame, bg = couleurBack,height = hauteurfinal/3*2, width = largeurfinal/2)
        testFrame.grid(row = 0, column = 0)
        testFrame.grid_propagate(0)

        #Frame bottom right
        keyboardFrame= Frame(rightFrame, bg = couleurBack,height = hauteurfinal/3, width = largeurfinal/2)
        keyboardFrame.grid(row = 1, column = 0)
        keyboardFrame.grid_propagate(0)

        #Theme
        theme = var.get()
        labeltheme = Label(testFrame, text ="Th??me : " + theme, bg = couleurBack, fg = couleurFg, font = "Times 30")
        labeltheme.grid(row = 0, column = 0)
        labeltheme.grid_propagate(0)

        image = Image.open("C:/Users/Thomas/Desktop/exercice du jour/pendu/41Kt59CjXmL.png")
        photo = ImageTk.PhotoImage(image)

        canvasHangman = Label(leftFrame,padx=512,pady = 512, image = photo, bg=couleurBack)
        label.image=photo
        canvasHangman.grid(row = 1, column = 0)

        labeldic= StringVar()
        labeldico = Label(testFrame, textvariable = labeldic, font = "times 30")
        labeldico.place(x = 200, y = 300)
        
        
        listetmpdico = []
        if var.get() == "Capitales":
            for i in motchoisi:
                listetmpdico.append(i)
                for j in range(len(listetmpdico)):
                    labeldic.set("__ "*(j+1))
            

    
        #keyboard
        ALPHA = "AZERTYUIOPQSDFGHJKLMWXCVBN"

        for premier in range(2):
                for second in range(10):
                    btn = Button (keyboardFrame,text=ALPHA[10*premier + second],font='times 30',bg = couleurBut,fg =couleurFg, activebackground = couleurFg,width = 2, command =lambda a=ALPHA[10*premier+second]:btn_command(a))
                    btn.grid(row=premier+2, column=second+2)

        for second in range(6):
            btn = Button(keyboardFrame, text=ALPHA[20 + second], font='Times 30',bg = couleurBut,fg =couleurFg, activebackground = couleurFg,width = 2,command = lambda a=ALPHA[20+second]:btn_command(a))
            btn.grid(row=4, column=second + 4)
       

        #quit button of the game window
        quitButton2 = Button (keyboardFrame, text = "Quit", bg = couleurBut, font = 'Times 20',command = gameWindow.destroy, activebackground = couleurFg, pady=10, padx = 30, bd = 1, fg=couleurFg, highlightthickness = 0)
        quitButton2.grid ( row = 4, column = 20)
        
#---------------------------------------------------------------------------------En-----------------------------------------------------------------
    elif lang == "En":

        #gameEN (window)
        gameWindow = Toplevel(main)
        gameWindow.title ("Hangman's Turf")
        gameWindow.config (bg = couleurBack)
        gameWindow.geometry ("1360x760")
        gameWindow.iconbitmap ("C:/Users/Thomas/Desktop/exercice du jour/pendu/jeudupendufb.ico")
        gameWindow.minsize(largeurfinal,hauteurfinal)
        gameWindow.maxsize(largeurfinal,hauteurfinal)


        #Frame right
        rightFrame = Frame(gameWindow,height = hauteurfinal, width = largeurfinal/2)
        rightFrame.grid(row = 0, column = 1, sticky = E)
        rightFrame.grid_propagate(0)

        #Frame left
        leftFrame = Frame(gameWindow, bg = couleurBack, height = hauteurfinal, width=largeurfinal/2)
        leftFrame.grid(row = 0, column = 0)
        leftFrame.grid_propagate(0)

        #frame top right
        testFrame= Frame(rightFrame, bg = couleurBack,height = hauteurfinal/3*2, width = largeurfinal/2)
        testFrame.grid(row = 0, column = 0)
        testFrame.grid_propagate(0)

        #Frame bottom right
        keyboardFrame= Frame(rightFrame, bg = couleurBack,height = hauteurfinal/3, width = largeurfinal/2)
        keyboardFrame.grid(row = 1, column = 0)
        keyboardFrame.grid_propagate(0)


        #Theme
        theme = var.get()
        labeltheme = Label(testFrame, text="Theme : " + theme, bg = couleurBack,fg =couleurFg, font = "Times 30")
        labeltheme.grid(row = 0, column = 0)
        labeltheme.grid_propagate(0)

        #Keyboard
        Alpha = "QWERTYUIOP"
        for premier in range(10):
            btnP = Button (keyboardFrame,text=Alpha[premier],font='times 30',bg = couleurBut,fg =couleurFg, activebackground = couleurFg, width=2, command = lambda a=Alpha[premier]:btn_command(a))
            btnP.grid(row = 0,column = premier)

        Beta = "ASDFGHJKL"
        for second in range(9):
            btnS = Button (keyboardFrame,text=Beta[second],font='times 30',bg = couleurBut,fg =couleurFg, activebackground = couleurFg, width=2, command = lambda a=Beta[second]:btn_command(a))
            btnS.grid(row=1,column = second)

        Gamma = "ZXCVBNM"
        for tri in range(7):
            btnT = Button (keyboardFrame,text=Gamma[tri],font='times 30',bg = couleurBut,fg =couleurFg, activebackground = couleurFg, width=2, command = lambda a=Gamma[tri]:btn_command(a))
            btnT.grid(row = 2, column = tri+2)


        #quit button of the game window
        quitButtonEn = Button (keyboardFrame, text = "Quit", bg = couleurBut, font = 'Times 20',command = gameWindow.destroy, activebackground = couleurFg, pady=10, padx = 30, bd = 1, fg=couleurFg, highlightthickness = 0)
        quitButtonEn.grid ( row = 2, column = 20)

        image = Image.open("C:/Users/Thomas/Desktop/exercice du jour/pendu/41Kt59CjXmL.png")
        photo = ImageTk.PhotoImage(image)

        canvasHangman = Label(leftFrame,padx=512,pady = 512, image = photo, bg =couleurBack)
        label.image=photo
        canvasHangman.grid(row = 1, column = 0)


#----------------------------------------------------------------------------------------------------------------------------------------------------
def rules():
    lang = varL.get()
    if lang == "Fr":

        r??glesEn.config(fg =couleurBack )
        r??gles.config(fg =couleurFg )
    else:
        r??gles.config(fg = couleurBack)
        r??glesEn.config(fg=couleurFg)


#----------------------------------------------------------------------------------------------------------------------------------------------------
def credits():


    creditswindow = Toplevel(main)
    creditswindow.geometry("720x480")
    creditswindow.minsize(int(largeurfinal/2),int(hauteurfinal/2))
    creditswindow.maxsize(int(largeurfinal/2),int(hauteurfinal/2))
    creditswindow.config(bg=couleurBack)
    creditswindow.iconbitmap ("C:/Users/Thomas/Desktop/exercice du jour/pendu/jeudupendufb.ico")


    creditsLabel = Label(creditswindow, text="cr???? par:\n\nAdam\nAzadeh\nThais\nHanan\nThomas", fg=couleurFg, bg = couleurBack)
    creditsLabel.pack()

    quitButCredits = Button(creditswindow,text = "Quit", command = creditswindow.destroy, bg = couleurBut, fg = couleurFg, activebackground = couleurFg, pady = 10, padx = 30)
    quitButCredits.pack(side = "bottom")

#----------------------------------------------------------------------------------------------------------------------------------------------------
couleurBack = '#9a9c91'
couleurBut = "#71716f"
couleurFg = "#bd2013"


#main window
main = Tk()
main.iconbitmap ("C:/Users/Thomas/Desktop/exercice du jour/pendu/jeudupendufb.ico")
main.config (background = couleurBack)
main.title ("Hangman")
main.geometry("1360x760")
largeur = main.winfo_screenwidth()
hauteur = main.winfo_screenheight()
largeurfinal = int(largeur / 4 * 3)
hauteurfinal = int(hauteur / 4 * 3)
main.minsize(largeurfinal,hauteurfinal)
main.maxsize(largeurfinal,hauteurfinal)




label = Label (main, text = "Welcome to Hangman's game",font =("courrier",20), bg =couleurBack, fg = couleurFg)
label.pack (expand = YES)


quitBut = Button (main, text = "Quit", command = main.destroy, bg = couleurBut,pady = 10, padx = 30, activebackground = couleurFg, fg=couleurFg)
quitBut.pack (side = "bottom", expand = YES)

butCredits = Button(main, text = "Credits",command = credits, bg = couleurBut, fg =couleurFg,pady = 10, padx = 26, activebackground = couleurFg)
butCredits.pack(side="bottom", expand = YES)

butRules = Button(main, command = rules, text = "Rules", pady = 10, padx = 30, activebackground = couleurFg, fg=couleurFg, bg = couleurBut)
butRules.pack(side = "bottom", expand = YES)

startbut = Button (main, text = "Start", command = openGame, bg=couleurBut, pady=10, padx = 30, bd = 1, activebackground = couleurFg, fg=couleurFg)
startbut.pack (side = "bottom", expand = YES)

r??gles = Label(main, text = "R??gles du jeu du Pendu :\n\nCliquez sur Start pour commencer une nouvelle partie. \nCliquez sur les lettres en bas que vous souhaitez proposer dans le mot. \nPour chaque lettre non pr??sente dans le mot,??le dessin du pendu s'affichera.\nLe but ??tant de ne pas se faire pendre.", bg = couleurBack, font = ("Courrier", 15), fg =couleurBack)
r??gles.pack(side = "top", expand = YES)


r??glesEn = Label(main, text = "Hangman Rules :\n\nPress start to begin. \nChoose a letter to see if the letter appears in the word.\nIf the letter does not appear in the word, a part of the hangman appears.\nThe goal is to guess the word and avoid being hanged.", bg = couleurBack, font = ("Courrier", 15), fg =couleurBack)
r??glesEn.pack(side = "top", expand = YES)


#dropdown for language
varL=StringVar(main)
varL.set("Fr")
d??roulantL= OptionMenu(main, varL,"Fr","En")
d??roulantL.config(bg = couleurBack,bd = 0,highlightthickness=1, activebackground = couleurBack, fg = couleurFg, justify = "center",highlightbackground = couleurBut)
d??roulantL.pack(side="bottom")

#DropDown menu
var= StringVar(main)
var.set("Cin??ma")

deroulant = OptionMenu(main, var, "Cin??ma", "Sport", "Capitales")
deroulant.config(bg = couleurBack,bd = 0,highlightthickness=1, activebackground = couleurBack, fg = couleurFg, justify = "center",highlightbackground = couleurBut)
deroulant.pack(side = "bottom")

labelTheme = Label(main, text = "Th??mes:", bg=couleurBack, fg = couleurFg, font = 'times 15')
labelTheme.pack(side = "bottom")


main.mainloop()



























