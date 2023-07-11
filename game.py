import pygame
import os
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("game")
clock = pygame.time.Clock()

root_dir = os.path.dirname(__file__) + "/"

test_font = pygame.font.Font(root_dir +"Pixeltype.ttf", 50)
test_surface = pygame.Surface((100,200))
test_surface.fill("red")

sky_surface = pygame.image.load(root_dir + "sky.png").convert()

ground_surface = pygame.image.load(root_dir + "ground.png").convert()

score_surface = test_font.render("My Game", False, "white")
score_rect = score_surface.get_rect(center=(400,50))

snail_surface = pygame.image.load(root_dir + "snail.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(600,300))

player_surface = pygame.image.load(root_dir + "player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80,300))

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type ==pygame.MOUSEMOTION:
            print(event.pos)

    screen.blit(test_surface, (200,100))
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    pygame.draw.rect()
    screen.blit(score_surface, (300,50))
    
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)
    
    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint( mouse_pos):
        print("collision")

    #draw elements & update everything
    pygame.display.update()
    clock.tick(60)
