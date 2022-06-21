from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror,showinfo
import time
from tkinter import *
import random
from tkinter.simpledialog import *
from tkinter import messagebox

class Personnage():
  def __init__(self, prenom, nom, photo,date_naissance,cin,cne,gmail,motpasse,adresse,niveau_étude,Occupation):
    self.prenom = prenom
    self.nom = nom
    self.photo = photo
    self.date_naissance=date_naissance
    self.cin = cin
    self.cne = cne
    self.gmail = gmail
    self.motpasse = motpasse
    self.adresse = adresse
    self.niveau_étude = niveau_étude
    self.Occupation = Occupation
  def __eq__(self, other):
    return (self.prenom==other.prenom and self.nom==other.nom and self.gmail ==other.gmail)

def appartient(liste,val):
    for i in range(len(liste)):
      if liste[i].__eq__(val):
        return 1
    return 0
