import tkinter
from tkinter import *
import time
import math
from helper import Helper as HP

class Vue:
    def __init__(self, parent, modele):
        self.parent = parent
        self.modele = modele
        self.root = Tk()  # Cet objet est responsable de tout l'interface graphique
        self.creer_page_jeu()
        self.creeps = []
        self.id = 0



    def creer_page_jeu(self):
        self.cadre_jeu = Frame(self.root)
        self.cadre_jeu.pack()
        self.canevas = Canvas(self.cadre_jeu, width=self.modele.largeur_grille * self.modele.taille_case,
                              height=self.modele.hauteur_grille * self.modele.taille_case)
        self.canevas.pack()

        # Dessiner le sentier
        self.sentier = [
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS",
             "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS",
             "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CS",
             "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CS",
             "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CC", "CV", "CV", "CC", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CC", "CC", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CS",
             "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CC", "CC", "CV", "CV"],
            ["CV", "CV", "CV", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CV", "CV", "CV", "CV", "CS", "CS", "CS",
             "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CS", "CC", "CC", "CV", "CV"],
            ["CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"],
            ["CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV",
             "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV", "CV"]]

        for p in range(self.modele.hauteur_grille):
            for i in range(self.modele.largeur_grille):
                x = i * self.modele.taille_case
                y = p * self.modele.taille_case
                if self.sentier[p][i] == "CV":
                    self.canevas.create_rectangle(x, y, x + self.modele.taille_case, y + self.modele.taille_case,
                                                  fill="palegreen4", )

                elif self.sentier[p][i] == "CS":
                    self.canevas.create_rectangle(x, y, x + self.modele.taille_case, y + self.modele.taille_case,
                                                  fill="wheat1", )

                elif self.sentier[p][i] == "CC":
                    self.canevas.create_rectangle(x, y, x + self.modele.taille_case, y + self.modele.taille_case,
                                                  fill="darkgray", outline="gold")
        # buttons et labels
        self.label_chrono = Label(self.cadre_jeu, text="Chrono", font=("Arial", 13))
        self.label_chrono.place(x=self.modele.taille_case * 2, y=self.modele.taille_case * 20,
                                height=self.modele.taille_case * 2 - 1, width=self.modele.taille_case * 2)

        self.label_vague = Label(self.cadre_jeu, text="Vague", font=("Arial", 13))
        self.label_vague.place(x=self.modele.taille_case * 2, y=self.modele.taille_case * 22,
                               height=self.modele.taille_case * 2, width=self.modele.taille_case * 2)

        # self.label_choix_tour = tkinter.LabelFrame(self.cadre_jeu, text="Choix de tours", font=("Arial", 13))
        # self.label_choix_tour.pack(fill="both", expand="yes")
        # self.label_choix_tour.place(x=self.modele.taille_case * 5, y=self.modele.taille_case * 20)

        self.boutton_pro = Button(self.cadre_jeu, text="Projectile", font=("Arial", 13))
        self.boutton_pro.place(x=self.modele.taille_case * 7, y=self.modele.taille_case * 21.5,
                               height=self.modele.taille_case * 1.5, width=self.modele.taille_case * 3)

        self.boutton_ecl = Button(self.cadre_jeu, text="Éclair", font=("Arial", 13))
        self.boutton_ecl.place(x=self.modele.taille_case * 11, y=self.modele.taille_case * 21.5,
                               height=self.modele.taille_case * 1.5, width=self.modele.taille_case * 3)

        self.boutton_poi = Button(self.cadre_jeu, text="Poison", font=("Arial", 13))
        self.boutton_poi.place(x=self.modele.taille_case * 15, y=self.modele.taille_case * 21.5,
                               height=self.modele.taille_case * 1.5, width=self.modele.taille_case * 3)

        self.label_nbr_vies = Label(self.cadre_jeu, text="Nbr de vies\n" + str(self.modele.vie), font=("Arial", 13))
        self.label_nbr_vies.place(x=self.modele.taille_case * 25, y=self.modele.taille_case * 21,
                                  height=self.modele.taille_case * 1, width=self.modele.taille_case * 3)

        self.label_argent = Label(self.cadre_jeu, text="Argent\n" + str(self.modele.argent), font=("Arial", 13))
        self.label_argent.place(x=self.modele.taille_case * 25, y=self.modele.taille_case * 22.5,
                                height=self.modele.taille_case * 1, width=self.modele.taille_case * 3)

        self.boutton_pro.bind("<ButtonRelease-1>", lambda event: (self.modele.test()))
        self.boutton_ecl.bind("<ButtonRelease-1>", lambda event: (self.modele.test()))
        self.boutton_poi.bind("<ButtonRelease-1>", lambda event: (self.modele.test()))

    def afficher_vie(self):
        self.label_nbr_vies.config(text="Nbr de vies\n" + str(self.modele.vie))
    def afficher_argent(self):
        self.label_argent.config(text="Argent\n" + str(self.modele.argent))
    def afficher_creep(self):
        for creep in self.creeps:
            self.canevas.delete(creep)
        self.creeps = []
        taille_case = self.modele.taille_case
        for creep in self.modele.creeps:
            x = creep.x
            y = creep.y
            self.creeps.append(self.canevas.create_rectangle(x + taille_case/2, y + taille_case/2, x + taille_case * 1.5, y + taille_case * 1.5, fill="blue"))

    def afficher_cadrier(self):
        for i in range(self.modele.largeur_grille + 1):
            x = i * self.modele.taille_case
            self.canevas.create_line(x, 0, x, self.modele.largeur_grille * self.modele.taille_case)

        for i in range(self.modele.hauteur_grille + 1):
            y = i * self.modele.taille_case
            self.canevas.create_line(0, y, self.modele.largeur_grille * self.modele.taille_case, y)

    def afficher_temps(self, temps):
        self.label_chrono.config(text = str(temps))

    def afficher_debut(self):
        self.label_debut = Label(self.root, text="Bienvenue à Tower Defense!", font=("Arial", 25))
        self.label_debut.pack()
        self.boutton_debut = Button(self.root, text="Jouer", font=("Arial", 25))
        self.boutton_debut.pack()
        self.boutton_debut.bind("<ButtonRelease-1>", lambda event: (self.creer_page_jeu(), self.boutton_debut.forget(), self.label_debut.forget()))

class Projectile:
    def __init__(self, parent, cible, force, empoisone, vitesse, type):
        self.position_initiale = (parent.x, parent.y)
        self.cible = cible
        self.force = force
        self.empoisone = empoisone
        self.vitesse = vitesse
        self.type = type

    def deplacer(self):
        pass


class Tour:
    def __init__(self, parent, x, y, type, cout_amelioration, range):
        self.parent = parent
        self.x = x
        self.y = y
        self.type = type
        self.niveau = 1
        self.cout_amelioration = cout_amelioration
        self.range = range

    def attacker(self):
        pass

    def ameliorer(self):
        pass

    def trouver_cible(self):
        pass


class Creep:
    def __init__(self, parent, x, y,mana):
        self.parent = parent
        self.x = x
        self.y = y
        self.mana = mana
        self.empoisone = False
        self.temps_empoisone = 0
        self.speed = 5
        self.creep_check_points = [(3, 17), (9, 17), (9, 5), (25, 5), (25, 10), (15, 10), (15, 17), (27, 17)]
        for i, point in enumerate(self.creep_check_points):
            self.creep_check_points[i] = (point[0] * self.parent.taille_case, point[1] * self.parent.taille_case)
        self.start = 0
        self.cible = self.creep_check_points[0]
        self.cible_i = 0
        self.angle = HP.calcAngle(self.x,self.y,self.cible[0],self.cible[1])
    def deplacer(self):
        cx,cy = self.cible
        distance = HP.calcDistance(self.x, self.y, cx, cy)
        if distance <= self.speed:
            self.cible_i += 1
            if self.cible_i <= len(self.creep_check_points) - 1:
                self.cible = self.creep_check_points[self.cible_i]
                self.angle = HP.calcAngle(self.x, self.y, self.cible[0], self.cible[1])
            else:
                self.parent.lose_life(self)
        self.x,self.y = HP.getAngledPoint(self.angle, self.speed, self.x, self.y)


class Modele:
    def __init__(self, parent):
        self.game_over = False
        self.parent = parent
        self.tours = []
        self.creep_cree = 20
        self.mana_init = 20
        self.pause_cree = True
        self.creeps = []
        self.projectiles = []
        # amelioration = 1.5^(niveau_tour) * cout_init_tour
        self.cout_init_pro = 30
        self.cout_init_ecl = 50
        self.cout_init_poi = 40
        self.rayon_pro = 5
        self.rayon_ecl = 3
        self.rayon_poi = 4
        self.taille_case = 35
        self.largeur_grille = 32
        self.hauteur_grille = 24
        self.argent = 100
        self.vie = 20
        self.niveau = 1
        self.round_started = False
        self.can_place_towers = True




    def deplacer_creeps(self):
        for creep in self.creeps:
            creep.deplacer()

    def creer_creep(self):
        case_x = 3
        case_y = 0
        self.creeps.append(Creep(self, case_x * self.taille_case, case_y * self.taille_case, self.mana_init * self.niveau))
        self.creep_cree -= 1

    def lose_life(self, creep):
        self.vie -= 1
        self.parent.vue.afficher_vie()
        self.creeps.remove(creep)
        if self.vie <= 0:
            self.parent.game_over()

    #changed
    def finish_round(self):
        self.round_started = False
        self.time_round_ended = time.time()

    def start_round(self):
        self.round_started = True
        self.creer_creep()


class Controler:
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.vue.afficher_creep()
        self.start_game()
        # self.vue.afficher_demarrage()
        # self.boucler()
    def start_loop(self):
        if not self.modele.game_over:
            if self.modele.creep_cree > 0 and self.modele.round_started:
                if self.modele.creeps[-1].y > 200:
                    self.modele.creer_creep()
            elif not self.modele.creeps and self.modele.round_started:
                self.modele.finish_round()
            if not self.modele.round_started:
                if time.time() - self.modele.time_round_ended <= 10:
                    pass
                else:
                    self.modele.start_round()
            self.vue.afficher_temps(f"{time.time() - self.modele.start:0.2f}")
            self.modele.deplacer_creeps()
            self.vue.afficher_creep()
            self.vue.id = self.vue.root.after(20, self.start_loop)

    def start_game(self):
        self.modele.start = time.time()
        self.modele.start_round()
        self.start_loop()
    def game_over(self):
        self.modele.game_over = True
        self.vue.root.after_cancel(self.vue.id)

if __name__ == '__main__':
    c = Controler()
    c.vue.root.mainloop()