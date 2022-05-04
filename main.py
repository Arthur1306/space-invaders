import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

# Variaveis da tela
altura, largura = 840, 480
WHITE = ("white")

# Montando a tela
tela = pygame.display.set_mode((altura, largura))
pygame.display.set_caption('Space Invaders')
listared = []
listagreen = []
listayellow = []


def update():
    pygame.display.flip()

# Aqui defino o player e os inimigos
class Player():
    player = pygame.image.load('assets/player.png')
    posx = 380
    posy = 440
    proy = posy-25
    prox = posx+22

    def atirar():
        pass

class Images():
    red_image = pygame.image.load('assets/red.png')
    green_image = pygame.image.load('assets/green.png')
    yellow_image = pygame.image.load('assets/yellow.png')
    bg = pygame.image.load('assets/space.jpg')
    
    bullet = pygame.image.load('assets/pixil-frame-0.png')
    bullet = pygame.transform.scale(bullet, (15,25))

def draw(tela):
    # Desenhando na tela os elementos
    tela.blit(Images.bg, (0, 0))
    tela.blit(Player.player, (Player.posx, Player.posy))

    vezes = 0
    y = 0
    while vezes < 3:
        for x in range(10, 800, 60):
            tela.blit(Images.red_image, (x, y))
            listared.append(x)
            listared.append(y)
            red_center = Images.red_image.get_rect(center=(x,y))
        y+=30
        vezes+=1
    
    vezes = 0
    y+=10

    while vezes < 3:
        for x in range(10, 800, 60):
            tela.blit(Images.green_image, (x, y))
            listagreen.append(x)
            listagreen.append(y)
            green_center = Images.green_image.get_rect(center=(x,y))
        y+=30
        vezes+=1

    y+=5

    for x in range(10, 800, 60):
        tela.blit(Images.yellow_image, (x, y))
        listayellow.append(x)
        listayellow.append(y)
        yellow_center = Images.yellow_image.get_rect(center=(x,y))

    update()

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
            if Player.posx >= 5:
                Player.posx -= 3
        if pygame.key.get_pressed()[K_d]:
            if Player.posx <= 775:
                Player.posx += 3
        if pygame.key.get_pressed()[K_h]:
            for i in range(2000):
                proy = Player.proy
                prox = Player.prox
                tela.blit(Images.bullet, (prox,proy))
                update()
                proy-=1
        
        draw(tela)
            
if __name__ == "__main__":
    main()