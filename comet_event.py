import pygame
from comet import Comet
pygame.init()

# creer la classe qui va gerer l'evenement


class CometFallEvent:

    # lors du chargement,-> creer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        # definir un groupe de sprite pour stocker les cometes
        self.all_comets = pygame.sprite.Group()
        self.game = game
        self.fall_mode = False


    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # boucle pour les valeurs entre 1 et 10
        for i in range(1, 15):
            # faire apparaitre une 1ere boule de feu
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # essayer de faire la pluie de commettes dans le cas ou la jauge est completement chargée
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True  # pour activer l'evenement

    def update_bar(self, surface):

        # ajouter le pourcentage a la barre
        self.add_percent()


        # barre black (en arriere plan)
        pygame.draw.rect(surface, (0, 0, 0),  [
            0,  # l'axe des x
            surface.get_height() - 20,  # l'axe des y(largeur de la fenetre)
            surface.get_width(),  # longeur de la fenetre
            10  # epaisseur de la barre
        ])

        # barre rouge (jauge d'event)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # l'axe des x
            surface.get_height() - 20,  # l'axe des y(largeur de la fenetre)
            (surface.get_width() / 100) * self.percent,  # longeur de la fenetre
            10  # epaisseur de la barre
        ])