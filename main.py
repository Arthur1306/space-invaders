import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

# Variaveis da tela
altura, largura = 840, 480
BG_COLOR = ("black")
WHITE = ("white")

bullet = pygame.image.load('assets/pixil-frame-0.png')
bullet = pygame.transform.scale(bullet, (15,25))

# Montando a tela
tela = pygame.display.set_mode((altura, largura))
pygame.display.set_caption('Space Invaders')

# Aqui defino o player e os inimigos
class Player():
    player = pygame.image.load('assets/player.png')
    posx = 380
    posy = 440

    def atirar():
        proy = Player.posy-25
        prox = Player.posx+22
        i=0
        tela.blit(bullet, (prox,proy))
        pygame.display.flip()
        while i<420:
            proy-=1
            i+=1

class Images():
    red_image = pygame.image.load('assets/red.png')
    green_image = pygame.image.load('assets/green.png')
    yellow_image = pygame.image.load('assets/yellow.png')

def draw(tela):
    # Desenhando na tela os elementos
    tela.fill(BG_COLOR)
    tela.blit(Player.player, (Player.posx, Player.posy))

    vezes = 0
    y = 0
    while vezes < 3:
        for x in range(10, 800, 60):
            tela.blit(Images.red_image, (x, y))
        y+=30
        vezes+=1
    
    vezes = 0
    y+=10

    while vezes < 3:
        for x in range(10, 800, 60):
            tela.blit(Images.green_image, (x, y))
        y+=30
        vezes+=1

    y+=5

    for x in range(10, 800, 60):
        tela.blit(Images.yellow_image, (x, y))

    pygame.display.flip()

def main():
    # Loop principal do jogo
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        # Controle do player
        if pygame.key.get_pressed()[K_a]:
            Player.posx -= 2
        if pygame.key.get_pressed()[K_d]:
            Player.posx += 2
        if pygame.key.get_pressed()[K_h]:
            Player.atirar()
        
        draw(tela)
            
if __name__ == "__main__":
    main()