from tkinter import *
from PIL import Image, ImageTk
import random
import importFile as iFile
import csv

liste = []


def ModifierImage(step):
    global leftFrame

    switcher={
                1:'C:/Users\Thomas\Desktop\exercice du jour\pendu\pendu-main\Photos pendus - Modifiées/2.png',
                2:'C:/Users\Thomas\Desktop\exercice du jour\pendu\pendu-main\Photos pendus - Modifiées/3.png',
                3:'C:/Users\Thomas\Desktop\exercice du jour\pendu\pendu-main\Photos pendus - Modifiées/4.png',
                4:'C:/Users\Thomas\Desktop\exercice du jour\pendu\pendu-main\Photos pendus - Modifiées/5.png',
                5:'C:/Users\Thomas\Desktop\exercice du jour\pendu\pendu-main\Photos pendus - Modifiées/6.png',
                6:'C:/Users\Thomas\Desktop\exercice du jour\pendu\pendu-main\Photos pendus - Modifiées/7.png',
                7: 'C:/Users\Thomas\Desktop\exercice du jour\pendu\pendu-main\Photos pendus - Modifiées/perdu.png',
                8:'C:/Users\Thomas\Desktop\exercice du jour\pendu\pendu-main\Photos pendus - Modifiées/gagnier.png'
             }

    test = switcher.get(step)
    #print(test)

    image = Image.open(test)
    photo = ImageTk.PhotoImage(image)
    canvasHangman = Label(leftFrame,padx=512,pady = 512, image = photo, bg=couleurBack)
    label.image=photo
    canvasHangman.grid(row = 1, column = 0)


#----------------------------------------------------------------------------------------------------------------------------------------------------
#command linked to keyboard
def btn_command(btn):
    global motchoisi
    global labeldico
    global labeldic
    global motPartiel
    global tempMot
    global leftFrame
    global testFrame
    global gagnier

    if btn in liste:
        #pass
        return btn

    #else:

    #On force la maiuscule pour éviter des differances
    motchoisi = motchoisi.upper()

    countTemp = len(motchoisi)
    #Verification si la lettre partian au Mot secret:
    #On verifie combiens d'occurence de lettre existe dans Mot(motchoisi)
    count = motchoisi.count(btn)

    labeldic = StringVar()
    motPartiel = labeldic.get()

    if count > 0:
        start = 0
        index = start
        #for i in range(count):
        while index != -1:
            index = motchoisi.find(btn, start, len(motchoisi)) #recupère l'index de la lettre correct
            if index !=-1:
                start = index + 1
                #Montré dans le frame du __ __ __ l'index trouvé
                tempMot[index] =  btn + "  "
                #on increment la variable gagnier
                gagnier += 1
                print(gagnier)

        labeldico = Label(testFrame, textvariable = labeldic, font = "times 30")
        labeldico.place(x = 100, y = 300)
        #converstion de la list en chaine et remotion des , et []
        tempMotString = "".join(tempMot)
        labeldic.set(tempMotString)

        #on verifier s'il a gagnier et on change l'image du leftframe
        if gagnier == len(motchoisi):
            ModifierImage(8)

    else:
        #on ajoute dans la liste superieur, les lettres qui ne font pas parties du mot choisi
        print("append-list")
        liste.append(btn)
        labelRe = StringVar()
        labelRe.set(liste)
        labelReponse = Label(testFrame, textvariable = labelRe, bg = couleurBack, fg = couleurFg)
        labelReponse.grid(row=1, column = 0)

        #on change l'image du leftframe
        if len(liste) > 7:
           ModifierImage(7) #le jouer a perdu
        else:
            ModifierImage(len(liste))


    return btn
#----------------------------------------------------------------------------------------------------------------------------------------------------
#second window(game window)
def openGame ():


    # dico = iFile.LireFichierCapitales("C:/Users/Thomas/Desktop/exercice du jour/pendu/liste_des_capitales")
    # a = random.randint(0,len(dico)-1)
    # motchoisi=dico[(a)]
    global testFrame
    global leftFrame
    global motchoisi
    global labeldic
    global labeldico
    global tempMot
    global gagnier


    lang = varL.get()
#---------------------------------------------------------------------------------Fr-----------------------------------------------------------------
    if  lang == "Fr":

        #gameEN (window)
        gameWindow = Toplevel(main)
        gameWindow.title ("Hangman's Turf")
        gameWindow.config (bg = couleurBack)
        gameWindow.geometry ("1360x760")
        gameWindow.iconbitmap ("C:/Users\Thomas\Desktop\exercice du jour\pendu\pendu-main\jeudupendufb.ico")
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
        labeltheme = Label(testFrame, text ="Thème : " + theme, bg = couleurBack, fg = couleurFg, font = "Times 30")
        labeltheme.grid(row = 0, column = 0)
        labeltheme.grid_propagate(0)

        image = Image.open("C:/Users\Thomas\Desktop\exercice du jour\pendu\pendu-main\Photos pendus - Modifiées/1.png")
        photo = ImageTk.PhotoImage(image)

        canvasHangman = Label(leftFrame,padx=512,pady = 512, image = photo, bg=couleurBack)
        label.image=photo
        canvasHangman.grid(row = 1, column = 0)

        labeldic= StringVar()
        labeldico = Label(testFrame, textvariable = labeldic, font = "times 30")
        labeldico.place(x = 100, y = 300)



        #lecture du fichier des capitales et creation dictionnaire
        dico = iFile.LireFichierCapitales("liste_des_capitales.csv")
        #print(dico[0])

        #choix aleatoire du Mot
        motchoisi = random.choice(list(dico.values()))
        #motchoisi = random.choice(dico.values())
        print(motchoisi)

        listetmpdico = []

        if var.get() == "Capitales":
            for i in motchoisi:
                listetmpdico.append(i)
                for j in range(len(listetmpdico)):
                    labeldic.set("__ "*(j+1))
                    #tempMot.insert(j, "__ ")

        #Thais: garde les espace __ dans une liste pour l'utiliser après
        print(len(motchoisi))
        tempMot = []
        for i in range(len(motchoisi)):
            tempMot.insert(i, "__ ")

        #on inicialise la variable gagnier avec 0. C'est un compteur pour informer si le jouer a gagné =)
        gagnier = 0
        #fin---

        #keyboard
        ALPHA = "AZERTYUIOPQSDFGHJKLMWXCVBN"

        for premier in range(2):
                for second in range(10):
                    btn = Button (keyboardFrame,text=ALPHA[10*premier + second],font='times 15',width = largeurBut, height = hauteurBut,bg = couleurBut,fg =couleurFg, activebackground = couleurFg, command =lambda q=ALPHA[10*premier+second]:btn_command(q))
                    btn.grid(row=premier+2, column=second+2)


        for second in range(6):
            btn = Button(keyboardFrame, text=ALPHA[20 + second],width = largeurBut, height = hauteurBut, font='Times 15',bg = couleurBut,fg =couleurFg, activebackground = couleurFg,command = lambda q=ALPHA[20+second]:btn_command(q))
            btn.grid(row=4, column=second + 4)


        #quit button of the game window
        quitButton2 = Button (keyboardFrame, text = "Quit", bg = couleurBut, font = 'Times 15',command = gameWindow.destroy, activebackground = couleurFg, width = largeurBut, height = hauteurBut, bd = 1, fg=couleurFg, highlightthickness = 0)
        quitButton2.grid ( row = 4, column = 20)

#---------------------------------------------------------------------------------En-----------------------------------------------------------------
    elif lang == "En":

        #gameEN (window)
        gameWindow = Toplevel(main)
        gameWindow.title ("Hangman's Turf")
        gameWindow.config (bg = couleurBack)
        gameWindow.geometry ("1360x760")
        gameWindow.iconbitmap ("jeudupendufb.ico")
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

        #image = Image.open("41Kt59CjXmL.png")
        image = Image.open("1.png")
        photo = ImageTk.PhotoImage(image)

        canvasHangman = Label(leftFrame,padx=512,pady = 512, image = photo, bg =couleurBack)
        label.image=photo
        canvasHangman.grid(row = 1, column = 0)




#----------------------------------------------------------------------------------------------------------------------------------------------------
def rules():


    lang = varL.get()
    if lang == "Fr":

        règlesEn.config(fg =couleurBack )
        règles.config(fg =couleurFg )
    else:
        règles.config(fg = couleurBack)
        règlesEn.config(fg=couleurFg)


#----------------------------------------------------------------------------------------------------------------------------------------------------
def credits():


    creditswindow = Toplevel(main)
    creditswindow.geometry("720x480")
    creditswindow.minsize(int(largeurfinal/2),int(hauteurfinal/2))
    creditswindow.maxsize(int(largeurfinal/2),int(hauteurfinal/2))
    creditswindow.config(bg=couleurBack)
    creditswindow.iconbitmap ("jeudupendufb.ico")


    creditsLabel = Label(creditswindow, text="créé par:\n\nAdam\nAzadeh\nThais\nHanan\nThomas", fg=couleurFg, bg = couleurBack)
    creditsLabel.pack()

    quitButCredits = Button(creditswindow,text = "Quit", command = creditswindow.destroy, bg = couleurBut, fg = couleurFg, activebackground = couleurFg, pady = 10, padx = 30)
    quitButCredits.pack(side = "bottom")

#----------------------------------------------------------------------------------------------------------------------------------------------------
couleurBack = '#9a9c91'
couleurBut = "#71716f"
couleurFg = "#bd2013"


#main window
main = Tk()
main.iconbitmap ("C:/Users\Thomas\Desktop\exercice du jour\pendu\pendu-main\jeudupendufb.ico")
main.config (background = couleurBack)
main.title ("Hangman")
main.geometry("1360x760")
largeur = main.winfo_screenwidth()
hauteur = main.winfo_screenheight()
largeurfinal = int(largeur / 4 * 3)
hauteurfinal = int(hauteur / 4 * 3)
largeurBut = int(largeurfinal/250)
hauteurBut = int(hauteurfinal/250)
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

#DropDown menu
var= StringVar(main)
var.set("Capitales")

deroulant = OptionMenu(main, var, "Cinéma", "Sport", "Capitales")
deroulant.config(bg = couleurBack,bd = 0,highlightthickness=1, activebackground = couleurBack, fg = couleurFg, justify = "center",highlightbackground = couleurBut)
deroulant.pack(side = "bottom")

labelTheme = Label(main, text = "Thêmes:", bg=couleurBack, fg = couleurFg, font = 'times 15')
labelTheme.pack(side = "bottom")


main.mainloop()



























