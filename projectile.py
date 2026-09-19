


import pygame


#definir la classe du projectle
class Projectile(pygame.sprite.Sprite):

    #definition du constructeur de la classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 10
        self.player = player
        self.image = pygame.image.load('app/assets/projectile.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect.x = player.rect.x + 130
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    #faire roter le projectile
    def rotate(self):
        self.angle += 5
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, float(0.5))
        #retablir le sens de rotation de facon a ce que la rotation du projectile soit plus fluide
        #self.rect = self.image.get_rect(center=self.rect.center)


    #supprimer le projectile puisqu'il est sorti de l'ecran
    def remove(self):
        self.player.all_projectiles.remove(self)

        
    def move(self):
        self.rect.x += self.velocity
        self.rotate()
  
        #vrifier si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #supprimer le projectile
            self.remove()
            #infliger des degats
            monster.damage(self.player.attack)

        #verifier si le projectile lance n'est plus sur l'ecran
        if self.rect.x > 1372:
            self.remove()
            