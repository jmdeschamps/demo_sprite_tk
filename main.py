from tkinter import *
from tkinter import filedialog as fd
import random
###########    VUE    ################
class Vue():
    def __init__(self,parent,modele):
        self.parent=parent
        self.modele=modele
        self.root=Tk()
        btngo=Button(self.root,text="Nouveau gif",command=self.ouvrir_gif)
        self.canevas=Canvas(self.root,width=self.modele.largeur,height=self.modele.hauteur,bg="black")
        btngo.pack()
        self.canevas.pack()

    def afficher_anim(self):
        self.canevas.delete(ALL)
        for i in self.modele.animations:
            i=self.modele.animations[i]
            self.canevas.create_image(i.x,i.y,image=i.images[i.indice])

    def ouvrir_gif(self):
        rep=self.charger_gifs()
        if rep:
            self.parent.creer_anim(rep)


    ###
    def charger_gifs(self):
        nom_gif=fd.askopenfilename(title="Fichier GIF svp",filetypes=[("gif","gif")])
        if nom_gif:
            listeimages = []
            testverite = 1
            noindex = 0
            while testverite:
                try:
                    img = PhotoImage(file=nom_gif, format="gif -index " + str(noindex))
                    listeimages.append(img)
                    noindex += 1
                except Exception:
                    testverite = 0
            return [nom_gif,listeimages]

###############  MODELE   ###############
class Anim():
    def __init__(self,parent,listeimages):
        self.parent=parent
        self.images=listeimages
        self.x=random.randrange(self.parent.largeur)
        self.y=random.randrange(self.parent.hauteur)
        self.max_image=len(self.images)
        self.indice=0

    def jouer_tour(self):
        self.indice+=1
        if self.indice == self.max_image:
            self.indice=0

class Modele():
    def __init__(self,parent):
        self.parent=parent
        self.largeur=800
        self.hauteur=600
        self.animations={}

    def jouer_tour(self):
        for i in self.animations:
            self.animations[i].jouer_tour()

    def creer_anim(self,info_gif):
        nom_gif,listeimages=info_gif
        self.animations[nom_gif]=Anim(self,listeimages)

############   CONTROLEUR     #########
class Controleur():
    def __init__(self):
        self.modele=Modele(self)
        self.vue=Vue(self,self.modele)
        self.vue.root.after(50,self.jouer_animations)
        self.vue.root.mainloop()

    def jouer_animations(self):
        self.modele.jouer_tour()
        self.vue.afficher_anim()
        self.vue.root.after(50,self.jouer_animations)

    def creer_anim(self,info_gif):
        self.modele.creer_anim(info_gif)

if __name__ == '__main__':
    c=Controleur()
    print("L'application se termine")