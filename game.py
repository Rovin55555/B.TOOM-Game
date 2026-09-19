import time
from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
import pygame
from sounds import SoundManager


# classe representant le jeu


class Game:

    def __init__(self):
        # definir si notre jeu a commencer ou non
        self.is_playing = False
        self.font = pygame.font.SysFont('monospace', 16)

        # generer le joueur quand une new party est creee
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer l'evenement
        self.comet_event = CometFallEvent(self)

        # definition du groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        # gerer le son
        self.sound_manager = SoundManager()
        # mettre le score à 0
        self.score = 0
        self.pressed = {}
       

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, amount=10):
        self.score += amount


    def game_over(self):
        # remettre le joueur a neuf, retirer les monstres, remettre le joueur a 100 de vie, jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        # jouer le son du game_over à partir de la class SoundManager
        self.sound_manager.play('game_over')
        time.sleep(2)

    def update(self, screen):

        # on peut changer la police
        # d'ecriture en allant sur __google font__,et en telechargeant la police quui nous
        # plait et en la glissant dans le projet
        # la police qu'on a ici est 'monospace'
        # le script pour choisir une police qui n'est pas sur le Systeme par defaut est:
        # font = pygame.font.Font( (chemin vers le font), (taille decriture) )'


        # afficher le score sur l'ecran
        score_text = self.font.render(f'SCORE : {self.score}', 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # appliquage de l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre du player
        self.player.update_health_bar(screen)

        # actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)

        # actualiser l'animation du joueur
        self.player.update_animation()

        # reupertion de projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # recuperer les cometes de mon jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        self.player.all_projectiles.draw(screen)

        # appliquer/dessiner le groupe de joueur
        self.all_monsters.draw(screen)

        # appliquer l'ensemble des images du groupe de comets
        self.comet_event.all_comets.draw(screen)

    
        # verifier si le joueur souhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
             self.player.move_right()


        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x >0:
            self.player.move_left()




    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))
