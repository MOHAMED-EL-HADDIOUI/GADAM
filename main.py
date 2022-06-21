from tkinter.messagebox import *
from date import get_date
from Registration import *
import PIL.Image
import PIL.ImageTk
from Télécharger import Télécharger
#***************************************Méthode Espace*****************************************************************

def Espace(personne):
    newFen = Tk()
    newFen.title("Ma Espace")
    newFen.geometry("900x620")
    newFen.resizable(width=0, height=0)
    newFen.configure(bg="#8C8F82")
    frameA = Frame(newFen, bg="#0B297B", width=900, height=80, bd=20, relief="sunken")
    frameA.place(x=0, y=0)
    Titre_Z = Label(newFen, text="   Ma Espace  ", fg="white", bg="#0B297B",
                    font=("Arial", 16, "bold")).place(x=300, y=30)
    frameC = Frame(newFen, bg="#8C8F82", width=900, height=530, bd=20, relief="sunken")
    frameC.place(x=0, y=90)
    Button(frameC, text=" Accueil ", fg="white", width=13, bg='#0B297B', bd=8, font=("calibre", 13, "bold")).place(x=10,
                                                                                                                   y=5)
    Button(frameC, text=" Mes Données ", fg="white", width=13, bg='#0B297B', bd=8,
            font=("calibre", 13, "bold")).place(x=185, y=5)
    Button(frameC, text=" Mes images ", fg="white", width=13, bg='#0B297B', bd=8,
           font=("calibre", 13, "bold")).place(x=360, y=5)
    Button(frameC, text=" Demandes ", fg="white", width=13, bg='#0B297B', bd=8,
           font=("calibre", 13, "bold")).place(x=535, y=5)
    Button(frameC, text=" Contact ", fg="white", width=13, bg='#0B297B', bd=8,
           font=("calibre", 13, "bold")).place(x=710, y=5)
    frameE = Frame(frameC, bg="#0B297B", width=850, height=70, bd=20, relief="sunken")
    frameE.place(x=10, y=60)
    Recharche_L = Label(frameE, text=" Recharche ", fg="white", width=12, bg='#0B297B', bd=8,
                        font=("calibre", 12, "bold"))
    Recharche_L.place(x=0, y=0)
    RecharcheB = StringVar()
    RecharcheB.set("Recharche ici ")
    Recharche = Entry(frameE, textvariable=RecharcheB, fg="#0B297B", width=25, bg='white', bd=8,
                      font=("calibre", 13, "bold"))
    Recharche.place(x=170, y=0)
    rej = PhotoImage(file="recharche.png")
    Button(frameE, image=rej, bg='#0B297B').place(x=430, y=1)
    newFen.mainloop()
#***********************************************************************************************************************
#***************************************Méthode Informations*****************************************************************

def Informations(PERSONNE):
    def Modifier():
        def Enregistrer():
            PERSONNE.nom = VALUE_NOM.get()
            PERSONNE.prenom = VALUE_PRENOM.get()
            PERSONNE.gmail = VALUE_Gmail.get()
            PERSONNE.adresse = VALUE_Adresse.get()
            PERSONNE.cin = VALUE_CIN.get()
            PERSONNE.cne = VALUE_CNE.get()
            PERSONNE.niveau_étude = VALUE_niveau_étude.get()
            PERSONNE.Occupation = VALUE_Occupation.get()
            PERSONNE.date_naissance = VALUE_date_naissance.get()
            showinfo(title="Enregistration reussie",
                     message="Les informations de " + VALUE_PRENOM.get() + " " + VALUE_NOM.get() + " a bien été enregistré.")

        # Nom
        VALUE_NOM = Entry(frameC, width=25, justify="center", font=("Arial", 14, "bold"), textvariable=variable_nom,
                          fg="white", bg="#0B297B", bd=10)
        VALUE_NOM.place(x=180, y=10)
        # Prenom
        VALUE_PRENOM = Entry(frameC, width=25, justify="center", font=("Arial", 14, "bold"),
                             textvariable=variable_prenom, fg="white", bg="#0B297B", bd=10)
        VALUE_PRENOM.place(x=180, y=60)
        # date de naissance
        VALUE_date_naissance = Entry(frameC, width=25, justify="center", font=("Arial", 14, "bold"),
                                     textvariable=variable_date_naissance, fg="white", bg="#0B297B", bd=10)
        VALUE_date_naissance.place(x=230, y=110)
        # CIN
        VALUE_CIN = Entry(frameC, width=25, justify="center", font=("Arial", 14, "bold"), textvariable=variable_CIN,
                          fg="white", bg="#0B297B", bd=10)
        VALUE_CIN.place(x=180, y=160)
        # CNE

        VALUE_CNE = Entry(frameC, width=25, justify="center", font=("Arial", 14, "bold"), textvariable=variable_CNE,
                          fg="white", bg="#0B297B", bd=10)
        VALUE_CNE.place(x=180, y=210)
        # Adresse
        VALUE_Adresse = Entry(frameC, font=("Arial", 14, "bold"), textvariable=variable_Adresse, fg="white",
                              bg="#0B297B", bd=10)
        VALUE_Adresse.place(x=230, y=260, width=340, height=80)
        # niveau_étude
        VALUE_niveau_étude = Entry(frameC, width=25, justify="center", font=("Arial", 14, "bold"),
                                   textvariable=variable_niveau_étude, fg="white", bg="#0B297B", bd=10)
        VALUE_niveau_étude.place(x=230, y=350)
        # Occupation
        VALUE_Occupation = Entry(frameC, width=25, justify="center", font=("Arial", 14, "bold"),
                                 textvariable=variable_Occupation, fg="white", bg="#0B297B", bd=10)
        VALUE_Occupation.place(x=230, y=400)
        # Gmail
        VALUE_Gmail = Entry(frameC, width=35, justify="center", font=("Arial", 14, "bold"), textvariable=variable_Gmail,
                            fg="white", bg="#0B297B", bd=10)
        VALUE_Gmail.place(x=180, y=450)
        Button(frameC, text=" Enregistrer ", fg="#0B297B", command=Enregistrer, width=12, bg='white', bd=6,
               font=("Arial", 13, "bold")).place(x=720, y=350)

    def Afficher():
        variable_nom.set(PERSONNE.nom)
        variable_prenom.set(PERSONNE.prenom)
        variable_date_naissance.set(PERSONNE.date_naissance)
        variable_CIN.set(PERSONNE.cin)
        variable_CNE.set(PERSONNE.cne)
        variable_Gmail.set(PERSONNE.gmail)
        variable_niveau_étude.set(PERSONNE.niveau_étude)
        variable_Adresse.set(PERSONNE.adresse)
        variable_Occupation.set(PERSONNE.Occupation)
        # *************************************************
        photoLab = Label(frameC)
        img = PIL.Image.open(PERSONNE.photo)
        img = img.resize((170, 220), PIL.Image.ANTIALIAS)
        photoLab.img = PIL.ImageTk.PhotoImage(img)
        photoLab.configure(image=photoLab.img)
        photoLab.place(x=660, y=20)
        # *************************************************

    newFen = Tk()
    newFen.title("MES INFORMATIONS")
    newFen.geometry("900x620")
    newFen.resizable(width=0, height=0)
    newFen.configure(bg="#8C8F82")
    frameA = Frame(newFen, bg="#0B297B", width=900, height=80, bd=20, relief="sunken")
    frameA.place(x=0, y=0)
    Titre_Z = Label(newFen, text="   MES INFORMATIONS  ", fg="white", bg="#0B297B",
                    font=("Arial", 16, "bold")).place(x=300, y=30)
    frameC = Frame(newFen, bg="#8C8F82", width=900, height=530, bd=20, relief="sunken")
    frameC.place(x=0, y=90)

    # Nom
    NOM = Label(frameC, width=10, font=("Arial", 14, "bold"), text=" Nom ", fg="white", bg="#0B297B", bd=10)
    NOM.place(x=30, y=10)
    variable_nom = StringVar()
    VALUE_NOM = Entry(frameC, width=25, justify="center", state=DISABLED, font=("Arial", 14, "bold"),
                      textvariable=variable_nom, fg="white", bg="#0B297B", bd=10)
    VALUE_NOM.place(x=180, y=10)
    # Prenom
    Prenom = Label(frameC, width=10, font=("Arial", 14, "bold"), text=" Prénom ", fg="white", bg="#0B297B", bd=10)
    Prenom.place(x=30, y=60)
    variable_prenom = StringVar()
    VALUE_PRENOM = Entry(frameC, width=25, justify="center", state=DISABLED, font=("Arial", 14, "bold"),
                         textvariable=variable_prenom, fg="white", bg="#0B297B", bd=10)
    VALUE_PRENOM.place(x=180, y=60)
    # date de naissance
    Date_Naissance = Label(frameC, width=14, font=("Arial", 14, "bold"), text=" Date de Naissance ", fg="white",
                           bg="#0B297B", bd=10)
    Date_Naissance.place(x=30, y=110)
    variable_date_naissance = StringVar()
    VALUE_date_naissance = Entry(frameC, width=25, justify="center", state=DISABLED, font=("Arial", 14, "bold"),
                                 textvariable=variable_date_naissance, fg="white", bg="#0B297B", bd=10)
    VALUE_date_naissance.place(x=230, y=110)
    # CIN
    CIN = Label(frameC, width=10, font=("Arial", 14, "bold"), text=" CIN ", fg="white", bg="#0B297B", bd=10)
    CIN.place(x=30, y=160)
    variable_CIN = StringVar()
    VALUE_CIN = Entry(frameC, width=25, state=DISABLED, justify="center", font=("Arial", 14, "bold"),
                      textvariable=variable_CIN, fg="white", bg="#0B297B", bd=10)
    VALUE_CIN.place(x=180, y=160)
    # CNE
    CNE = Label(frameC, width=10, font=("Arial", 14, "bold"), text=" CNE ", fg="white", bg="#0B297B", bd=10)
    CNE.place(x=30, y=210)
    variable_CNE = StringVar()
    VALUE_CNE = Entry(frameC, width=25, state=DISABLED, justify="center", font=("Arial", 14, "bold"),
                      textvariable=variable_CNE, fg="white", bg="#0B297B", bd=10)
    VALUE_CNE.place(x=180, y=210)
    # Adresse
    Adresse = Label(frameC, width=14, font=("Arial", 14, "bold"), text=" Adresse Personnel ", fg="white", bg="#0B297B",
                    bd=10)
    Adresse.place(x=30, y=260)
    variable_Adresse = StringVar()
    VALUE_Adresse = Entry(frameC, state=DISABLED, font=("Arial", 14, "bold"), textvariable=variable_Adresse, fg="white",
                          bg="#0B297B", bd=10)
    VALUE_Adresse.place(x=230, y=260, width=340, height=80)
    # niveau_étude
    niveau_étude = Label(frameC, width=14, font=("Arial", 14, "bold"), text=" Niveau D'étude ", fg="white",
                         bg="#0B297B", bd=10)
    niveau_étude.place(x=30, y=350)
    variable_niveau_étude = StringVar()
    VALUE_niveau_étude = Entry(frameC, width=25, justify="center", state=DISABLED, font=("Arial", 14, "bold"),
                               textvariable=variable_niveau_étude, fg="white", bg="#0B297B", bd=10)
    VALUE_niveau_étude.place(x=230, y=350)
    # Occupation
    Occupation = Label(frameC, width=14, font=("Arial", 14, "bold"), text=" Occupation ", fg="white", bg="#0B297B",
                       bd=10)
    Occupation.place(x=30, y=400)
    variable_Occupation = StringVar()
    VALUE_Occupation = Entry(frameC, width=25, state=DISABLED, justify="center", font=("Arial", 14, "bold"),
                             textvariable=variable_Occupation, fg="white", bg="#0B297B", bd=10)
    VALUE_Occupation.place(x=230, y=400)
    # Gmail
    Gmail = Label(frameC, width=10, font=("Arial", 14, "bold"), text=" Gmail ", fg="white", bg="#0B297B", bd=10)
    Gmail.place(x=30, y=450)
    variable_Gmail = StringVar()
    VALUE_Gmail = Entry(frameC, width=35, state=DISABLED, justify="center", font=("Arial", 14, "bold"),
                        textvariable=variable_Gmail, fg="white", bg="#0B297B", bd=10)
    VALUE_Gmail.place(x=180, y=450)
    Button(frameC, text=" Télécharger ", fg="#0B297B", command=lambda :Télécharger(PERSONNE), width=12, bg='white', bd=6,
           font=("Arial", 13, "bold")).place(x=640, y=300)
    Button(frameC, text=" Modifier ", fg="#0B297B", command=Modifier, width=12, bg='white', bd=6,
           font=("Arial", 13, "bold")).place(x=720, y=350)
    Button(frameC, text=" Afficher ", fg="#0B297B", command=Afficher, width=12, bg='white', bd=6,
           font=("Arial", 13, "bold")).place(x=560, y=350)

    Button(frameC, text=" Ma Espace ", fg="#0B297B", width=12, bg='white', bd=6,command=lambda :Espace(PERSONNE), font=("calibre", 12, "bold")).place(
        x=640, y=400)
    Button(frameC, text=" Exit ", command=lambda: Quitter(newFen), fg="#0B297B", width=12, bg='white', bd=6,
           font=("Arial", 13, "bold")).place(x=640, y=450)
    newFen.mainloop()

#***********************************************************************************************************************
#***************************************Les variables Principales*******************************************************

imageName, listePersonne,pn = '', [],1

#***********************************************************************************************************************
#***************************************Méthode quitter*****************************************************************

def Quitter(root):
	## Quitter le jeu
	reponse = askyesno("Terminer le jeu","Voulez-vous réellement quitter ? \n Cliquer « Oui » pour finir")
	if reponse :
         root.destroy()
         root.quit()

#***********************************************************************************************************************
#***************************************Méthode Registration************************************************************

def Registration(root):
    def Valider():
        global listePersonne, imageName ,pn
        photo = imageName
        if VALUE_PRENOM.get() and VALUE_NOM.get() and photo and VALUE_date_naissance.get() and VALUE_CIN.get() and VALUE_CNE.get() and VALUE_Adresse.get() and VALUE_niveau_étude.get() and VALUE_Occupation.get() and VALUE_Gmail.get() and VALUE_motpasse.get():
            pn = Personnage(VALUE_PRENOM.get(), VALUE_NOM.get(), photo,VALUE_date_naissance.get(), VALUE_CIN.get(),
                            VALUE_CNE.get(), VALUE_Gmail.get(), VALUE_motpasse.get(), VALUE_Adresse.get(),
                            VALUE_niveau_étude.get(), VALUE_Occupation.get())
            if appartient(listePersonne, pn):
                showerror(title="Erreur sur le formulaire", message="Cet utilisateur existe deja !")
            else:
                listePersonne.append(pn)
                showinfo(title="validation reussie",
                         message=VALUE_PRENOM.get() + " " + VALUE_NOM.get() + " a bien été ajouter.")
        else:
            showerror(title="Erreur sur le formulaire", message="Voyez renseigner tout les chants du formulaire !")
    def parcourir():
        global imageName
        imn = askopenfilename(initialdir="/", title="Selectionner une photo",
                              filetypes=(("png files", "*.png"), ("jpeg files", "*.jpg")))
        if imn:
            imageName = imn
        if imageName:
            texte = imageName.split()
            VALUE_Photo.configure(text=texte)
    root.destroy()
    fen = Tk()
    fen.geometry("980x700")
    fen.resizable(width=0, height=0)
    fen.configure(bg="#8C8F82")
    fen.title("Registration")
    frame1 = Frame(fen, bg="#0B297B", width=400, height=700, bd=20, relief="sunken")
    frame1.place(x=0, y=0)
    IMAGE_Registration = PhotoImage(file="Registration.png")
    registration = Label(frame1, image=IMAGE_Registration, bg="#0B297B")
    registration.place(x=60, y=180)
    frame2 = Frame(fen, bg="#8C8F82", width=580, height=700, bd=20, relief="sunken")
    frame2.place(x=400, y=0)
    Titre = Label(frame2,width=35,font=("Arial", 17, "bold"),text =" Remplir Le Formulaire ",fg="white", bg="#0B297B",bd=10)
    Titre.place(x=20, y=20)
    #Nom
    NOM = Label(frame2,width=10,font=("Arial", 14 , "bold"),text =" Nom ",fg="white", bg="#0B297B",bd=10)
    NOM.place(x=30, y=100)
    variable_nom = StringVar()
    VALUE_NOM = Entry(frame2,width=25,font=("Arial", 14 , "bold"),textvariable=variable_nom,fg="white", bg="#0B297B",bd=10)
    VALUE_NOM.place(x=180, y=100)
    # Prenom
    Prenom = Label(frame2,width=10,font=("Arial", 14 , "bold"),text =" Prénom ",fg="white", bg="#0B297B",bd=10)
    Prenom.place(x=30, y=150)
    variable_prenom = StringVar()
    VALUE_PRENOM = Entry(frame2, width=25, font=("Arial", 14, "bold"), textvariable=variable_prenom, fg="white", bg="#0B297B",bd=10)
    VALUE_PRENOM.place(x=180, y=150)
    # date de naissance
    Date_Naissance = Label(frame2, width=14, font=("Arial", 14, "bold"), text=" Date de Naissance ", fg="white", bg="#0B297B", bd=10)
    Date_Naissance.place(x=30, y=200)
    variable_date_naissance = StringVar()
    VALUE_date_naissance = Entry(frame2, width=25, font=("Arial", 14, "bold"), textvariable=variable_date_naissance, fg="white",bg="#0B297B", bd=10)
    VALUE_date_naissance.place(x=230, y=200)
    Button(frame2, text=" choisir ", command=lambda: get_date(variable_date_naissance), fg="#0B297B", bg='white', bd=6,font=("calibre", 11, "bold")).place(x=450, y=200)
    #CIN
    CIN = Label(frame2, width=10, font=("Arial", 14, "bold"), text=" CIN ", fg="white", bg="#0B297B",bd=10)
    CIN.place(x=30, y=250)
    variable_CIN = StringVar()
    VALUE_CIN = Entry(frame2, width=25, font=("Arial", 14, "bold"), textvariable=variable_CIN, fg="white",bg="#0B297B", bd=10)
    VALUE_CIN.place(x=180, y=250)
    # CNE
    CNE = Label(frame2, width=10, font=("Arial", 14, "bold"), text=" CNE ", fg="white", bg="#0B297B", bd=10)
    CNE.place(x=30,y=300)
    variable_CNE = StringVar()
    VALUE_CNE = Entry(frame2, width=25, font=("Arial", 14, "bold"), textvariable=variable_CNE, fg="white", bg="#0B297B",bd=10)
    VALUE_CNE.place(x=180, y=300)
    # Adresse
    Adresse = Label(frame2, width=14, font=("Arial", 14, "bold"), text=" Adresse Personnel ", fg="white", bg="#0B297B", bd=10)
    Adresse.place(x=30,y=350)
    variable_Adresse = StringVar()
    VALUE_Adresse = Entry(frame2, width=25, font=("Arial", 14, "bold"), textvariable=variable_Adresse, fg="white", bg="#0B297B",bd=10)
    VALUE_Adresse.place(x=230, y=350)
    # niveau_étude
    niveau_étude = Label(frame2, width=14, font=("Arial", 14, "bold"), text=" Niveau D'étude ", fg="white", bg="#0B297B", bd=10)
    niveau_étude.place(x=30,y=400)
    variable_niveau_étude = StringVar()
    VALUE_niveau_étude = Entry(frame2, width=25, font=("Arial", 14, "bold"), textvariable=variable_niveau_étude, fg="white", bg="#0B297B",bd=10)
    VALUE_niveau_étude.place(x=230, y=400)
    # Occupation
    Occupation = Label(frame2, width=14, font=("Arial", 14, "bold"), text=" Occupation ", fg="white",bg="#0B297B", bd=10)
    Occupation.place(x=30, y=450)
    variable_Occupation = StringVar()
    VALUE_Occupation = Entry(frame2, width=25, font=("Arial", 14, "bold"), textvariable=variable_Occupation,fg="white", bg="#0B297B", bd=10)
    VALUE_Occupation.place(x=230, y=450)
    #Gmail
    Gmail = Label(frame2, width=10, font=("Arial", 14, "bold"), text=" Gmail ", fg="white", bg="#0B297B", bd=10)
    Gmail.place(x=30, y=500)
    variable_Gmail = StringVar()
    VALUE_Gmail = Entry(frame2, width=25, font=("Arial", 14, "bold"), textvariable=variable_Gmail, fg="white", bg="#0B297B",bd=10)
    VALUE_Gmail.place(x=180, y=500)
    # motpasse
    motpasse = Label(frame2, width=14, font=("Arial", 14, "bold"), text=" Mot Passe ", fg="white", bg="#0B297B", bd=10)
    motpasse.place(x=30, y=550)
    variable_motpasse = StringVar()
    VALUE_motpasse = Entry(frame2, width=25, font=("Arial", 14, "bold"), textvariable=variable_motpasse, fg="white",bg="#0B297B", bd=10)
    VALUE_motpasse.place(x=230, y=550)
    # Photo
    Photo = Label(frame2, width=10, font=("Arial", 14, "bold"), text=" Photo ", fg="white", bg="#0B297B", bd=10)
    Photo.place(x=30, y=600)
    VALUE_Photo = Label(frame2, width=25, font=("Arial", 12, "bold"),text="Aucune Photo selection", fg="white", bg="#0B297B", bd=10)
    VALUE_Photo.place(x=180, y=600)
    Button(frame2, text=" choisir Photo ", command=parcourir, fg="#0B297B", bg='white', bd=6,font=("calibre", 11, "bold")).place(x=410, y=603)

    Button(fen, text=" Valide ", fg="#0B297B",command=Valider, width=12, bg='white', bd=6, font=("Arial", 13, "bold")).place(x=130,y=560)

    Button(fen, text=" Retour ", command=lambda: RETOUR(fen), fg="#0B297B", width=12, bg='white', bd=6,
           font=("calibre", 12, "bold")).place(x=40, y=620)
    Button(fen, text=" Exit ", command=lambda: Quitter(fen), fg="#0B297B", width=12, bg='white', bd=6,
           font=("Arial", 13, "bold")).place(x=220, y=620)
    fen.mainloop()

#***********************************************************************************************************************
#***************************************Méthode connection**************************************************************

def connection(ENTRE_nom_utilisateur,ENTRE_mot_passe,root1):
    def vrai():
        liste_reponce = [False,""]
        for i in range(len(listePersonne)):
            if ENTRE_nom_utilisateur.get() == listePersonne[i].nom and ENTRE_mot_passe.get() == listePersonne[i].motpasse:
                liste_reponce[0]=True
                liste_reponce[1] = listePersonne[i]
        return liste_reponce

    if vrai()[0]==True:
        Informations(vrai()[1])
    else:
        showerror(title="Erreur", message="Le Utilisateur qui Vous avez saisir n'existe pas !")

#***********************************************************************************************************************
#***************************************Méthode RETOUR******************************************************************

def RETOUR(root1):
    root1.destroy()
    Principal()

#***********************************************************************************************************************
#***************************************Méthode LOGIN*******************************************************************

def LOGIN(root):
    root1 = Tk()
    root1.geometry("720x480")
    root1.resizable(width=0, height=0)
    root1.configure(bg="#8C8F82")
    root1.title("Login")
    frame2 = Frame(root1, bg="#0B297B", width=720, height=80, bd=20, relief="sunken")
    frame2.place(x=0, y=0)
    TITILE1 = Label(root1, text="Login", fg="white", bg="#0B297B",font=("Arial", 17, "bold")).place(x=300, y=30)
    frame1 = Frame(root1, bg="#8C8F82", width=720, height=380, bd=20, relief="sunken")
    frame1.place(x=0, y=90)
    nom_utilisateur = Label(root1, text=" Nom Utilisateur ",bd=6, fg="white", bg="#0B297B",font=("calibre",16, "bold")).place(x=150, y=150)
    ENTRE_nom_utilisateur =Entry(root1, bd=6, width=15, fg='white', bg='#0B297B', font=('calibre', 16, 'bold'))
    ENTRE_nom_utilisateur.place(x=380, y=150)
    mot_passe = Label(root1, text=" Mot Passe ",bd=6, fg="white", bg="#0B297B",font=("calibre",16, "bold")).place(x=150, y=200)
    ENTRE_mot_passe =Entry(root1, bd=6, width=15,show='*', fg='white', bg='#0B297B', font=('calibre', 16, 'bold'))
    ENTRE_mot_passe.place(x=380, y=200)
    Button(root1, text=" Connection ",command=lambda :connection(ENTRE_nom_utilisateur,ENTRE_mot_passe,root1), fg="#0B297B", bg='white', bd=6, font=("calibre", 15, "bold")).place(x=320,y=350)
    Button(root1, text=" Retour ",command=lambda :RETOUR(root1), fg="#0B297B", bg='white', bd=6, font=("calibre", 12, "bold")).place(x=100,y=380)
    Button(root1, text=" Exit ", command=lambda :Quitter(root1), fg="#0B297B", bg='white', bd=6, font=("Arial", 13, "bold")).place(x=600,y=380)
    root.destroy()
    root1.mainloop()

#***********************************************************************************************************************
#***************************************Méthode Principale**************************************************************

def Principal():
    root = Tk()
    root.geometry("720x480")
    root.resizable(width=0, height=0)
    root.configure(bg="#8C8F82")
    root.title("WINDOW")
    frame22 = Frame(root, bg="#0B297B", width=720, height=80, bd=20, relief="sunken")
    frame22.place(x=0, y=0)
    TITILE = Label(root, text="SCHOOL MANAGEMENT SYSTEM v1.0", fg="white", bg="#0B297B",
                   font=("Arial", 16, "bold")).place(x=140, y=30)
    frame12 = Frame(root, bg="#8C8F82", width=720, height=380, bd=20, relief="sunken")
    frame12.place(x=0, y=90)
    image_utilisateur = PhotoImage(file="utilisateur.png")
    image_login = PhotoImage(file="login.png")
    image_exit = PhotoImage(file="exit.png")
    registration = Label(root, image=image_utilisateur, bg="#8C8F82")
    registration.place(x=40, y=140)
    login = Label(root, image=image_login, bg="#8C8F82")
    login.place(x=280, y=140)
    exit = Label(root, image=image_exit, bg="#8C8F82")
    exit.place(x=530, y=180)
    Button(root, text=" Registration ",width=12,command=lambda :Registration(root) , fg="#0B297B", bg='white', bd=6, font=("Arial", 13, "bold")).place(x=50, y=370)
    Button(root, text=" Login ",width=12, command=lambda: LOGIN(root), fg="#0B297B", bg='white', bd=6,font=("Arial", 13, "bold")).place(x=300, y=370)

    Button(root, text=" Exit ",width=12, command=lambda :Quitter(root), fg="#0B297B", bg='white', bd=6, font=("Arial", 13, "bold")).place(x=520,y=370)
    root.mainloop()

#***********************************************************************************************************************
#-----------------------------------------------------------------------------------------------------------------------

Principal()

#-----------------------------------------------------------------------------------------------------------------------
