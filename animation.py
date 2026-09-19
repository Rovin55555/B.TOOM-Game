import random
import pygame


# creer une classe qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    # definir les choses a faire a la creat de l'antitée
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()

        self.size = size
        self.image = pygame.image.load(f'app/assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 # commencer l'animations à l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # definir une methode pour demarer l'animation
    def start_animation(self):
        self.animation = True

    # definir une nouvelle methode pour animer le sprite
    def animate(self, loop=False):

        # verifier si l'animation est active
        if self.animation:
            # passer a l'animation de l'image suivante
            self.current_image += random.randint(0, 1)

            # verifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre l'animation au depart
                self.current_image = 0

                # verifier si l'animation n'est pas en mode boucle
                if loop is False:
                    # desactivation de l'animation
                    self.animation = False

            # modifier l'image précédente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)



# definir les notions pour charger les images d'un sprite
def load_animations_images(sprite_name):
    # charger les images du sprite dans le dossier correspondant
    images = [] # dans la prochaine boucle for il y a les elements de la liste à la derniere ligne

    # recuper le chemin du dossier pour ce sprite
    path = f"app/assets/{sprite_name}/{sprite_name}"

    # boucler sur chaque image du dossier pour les ajouter à la liste
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'images
    return images

# definir un dictionnaire qui va contenir les images chargées de chaque sprite
# mummy -> [...mummy1.png, ...mummy2.png, ...]
# player -> [...player1.png, ...player2.png, ...]
animations = {
    'mummy': load_animations_images('mummy'),
    'player': load_animations_images('player'),
    'alien': load_animations_images('alien')
}



