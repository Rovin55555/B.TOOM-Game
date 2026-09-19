import pygame
import random

# creer une clase pour gerer la comete


class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # definir quelle est l'image associée a la comete
        self.image = pygame.image.load('app/assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(3, 8)
        self.rect.x = random.randint(0, 1200)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # jouer le son quand la comette touche le sol
        self.comet_event.game.sound_manager.play('meteorite')

        # verf si le nbre de cometes est de 0
        if len(self.comet_event.all_comets) == 0:
            # remettre la barre à 0
            self.comet_event.reset_percent()
            # faire apparaitre les 2 premiers monstres
            self.comet_event.game.start()


    def fall(self):
        self.rect.y += self.velocity
        # detecter si lors de son deplacement la comete ne tombe pas au sol
        if self.rect.y >= 500:
            # retirer la boule de feu pour ne pas surcharger la RAM
            self.remove()

            # verf si il n'y a plus de boule de feu sur le jeu
            if len(self.comet_event.all_comets) == 0:
                print("l'evenement est fini")
                # remettre la jauge au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # verifier si la comete touche le joueur
        if self.comet_event.game.check_collision(
                self, self.comet_event.game.all_players
        ):
            print('joueur touché')
            # retirer la boule de feu
            self.remove()
            # faire subir au joueur 20 points de degats
            self.comet_event.game.player.damage(20)