


import animation
import pygame
from projectile import Projectile
from sounds import SoundManager


class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.all_projectiles= pygame.sprite.Group()
        self.velocity = 8
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.sound_manager = SoundManager()

    def damage(self, amount):
        if self.health - amount > amount :
            self.health -= amount
        else:
            # si le joueur n'a plus de points de vie
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        # dessin de la barre de vie
        # avec toutes ces proprietes
        pygame.draw.rect(surface, (0, 0, 200), [self.rect.x +50, self.rect.y +25, self.max_health, 10])
        pygame.draw.rect(surface, (200, 0, 0), [self.rect.x +50, self.rect.y +25, self.health, 10])

    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
         
    def launch_projectile(self):
        # creer une nouvelle instance de la classe Projectile
        self.all_projectiles.add(Projectile(self))
        self.sound_manager.play('tir')

        # demarer l'animation du lancer
        self.start_animation()
