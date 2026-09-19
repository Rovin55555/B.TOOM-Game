import pygame
import math
from game import Game
pygame.init()

# definir une clock
clock = pygame.time.Clock()
FPS = 120

# chargement de la fenetre du jeu
screen = pygame.display.set_mode((1372, 720))
pygame.display.set_caption('B°TOOM')

# importer charger l'arriere plan
background = pygame.image.load('app/assets/bg.jpg')

# importer et charger la baniere
banner = pygame.image.load('app/assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4) + 70
banner_rect.y = math.ceil(screen.get_height() / 4)

# importer et charger le boutton pour commencer la partie
play_button = pygame.image.load('app/assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33) + 70
play_button_rect.y = math.ceil(screen.get_height() / 4) + 370

# chargement du jeu
game = Game()


running = True
while running:
    # appliquage d'images
    screen.blit(background, (-1000, -200))

    # verifier si le jeu a commencer ou non
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(screen)

    # verifier si le jeu n'a pas commencer
    else:
        # ajouter l'ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
        


    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


        # detecter si un joueur lache unr touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True 
            
            # detecter si la touche espace est enclenchee pour lancer un projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # mettre le jeu  en mode lance
                    game.start()
                    # jouer le son après avoir lancé le jeu
                    game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est en collision avec le boutton
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu  en mode lance
                game.start()
                # jouer le son après avoir lancé le jeu
                game.sound_manager.play('click')

    # fixer le nombre de FPS sur la clock
    clock.tick(FPS)