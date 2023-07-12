import pygame
import os
from sys import exit
def display_score():
    current_time =int (pygame.time.get_ticks()/1000) - start_time
    score_surface =test_font.render(f'{current_time}' ,False,(64,64,64))
    score_rect =score_surface.get_rect(center=(400,50))
    screen.blit(score_surface,score_rect)
    


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("game")
clock = pygame.time.Clock()
root_dir = os.path.dirname(__file__) + "/"
test_font = pygame.font.Font(root_dir +"Pixeltype.ttf", 50)
game_active = True
start_time =0


test_surface = pygame.Surface((100,200))
test_surface.fill("red")

sky_surface = pygame.image.load(root_dir + "sky.png").convert()

ground_surface = pygame.image.load(root_dir + "ground.png").convert()

#score_surface = test_font.render("My Game", False, (64,64,64))
#score_rect = score_surface.get_rect(center=(360,60))

snail_surface = pygame.image.load(root_dir + "snail.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(600,300))

player_surface = pygame.image.load(root_dir + "player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80,300))

player_gravity =0  

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:  
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom>=300 :
                        player_gravity = -20 
                
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE and player_rect.bottom>=300:
                        player_gravity = -20 
        else:
             if event.type == pygame.KEYDOWN and event.key == pygame.K_space:
                  game_active = True
                  snail_rect.left = 800  
                  start_time = pygame.time.get_ticks() 
            
          
            
    if game_active:
        screen.blit(test_surface, (200,100))
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        #pygame.draw.rect(screen,"#c0e8ec",score_rect)
        #pygame.draw.rect(screen,"#c0e8ec",score_rect,10)
        #pygame.draw.ellipse(screen,"Brown",pygame.Rect(50,200,100,100))
        #screen.blit(score_surface, score_rect)
        display_score()

        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)
    #player
        player_gravity +=1
        player_rect.y+= player_gravity
        if player_rect.bottom >=300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)
        
        #keys= pygame.key.get_pressed()
        #if keys[pygame.K_SPACE]:
        # print("jump")
        
        #mouse_pos = pygame.mouse.get_pos()
        #if player_rect.collidepoint( mouse_pos):
        #    print("collision")
        

        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    else: 
        screen.fill("yellow")
    
    
    #draw elements & update everything
    pygame.display.update()
    clock.tick(60)
