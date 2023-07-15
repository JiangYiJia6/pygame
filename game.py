import pygame
import os
from sys import exit
from random import randint

def display_score():
    current_time =int (pygame.time.get_ticks()/1000) - start_time
    score_surface =test_font.render(f'Scroe:{current_time}' ,False,(64,64,64))
    score_rect =score_surface.get_rect(center=(400,50))
    screen.blit(score_surface,score_rect)
    return current_time
def obstacle_movement(obstacle_list):
     if obstacle_list:
          for obstacle_rect in obstacle_list:
               obstacle_rect.x -= 5
               if obstacle_rect.bottom == 300:
                    screen.blit(snail_surface, obstacle_rect)
               else:
                    screen.blit(fly_surface, obstacle_rect)
          obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
          return obstacle_list
     else: return[]
def collisions(player,obstacles):
     if obstacle_rect_list:
          for obstacle_rect in obstacle_rect_list:
               if player.colliderect(obstacle_rect):
                    return False
     return True


     
     
    
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("game")
clock = pygame.time.Clock()
root_dir = os.path.dirname(__file__) + "/"
test_font = pygame.font.Font(root_dir +"Pixeltype.ttf", 50)
game_active = False
start_time =0
score =0


test_surface = pygame.Surface((100,200))
test_surface.fill("red")

sky_surface = pygame.image.load(root_dir + "sky.png").convert()

ground_surface = pygame.image.load(root_dir + "ground.png").convert()

#score_surface = test_font.render("My Game", False, (64,64,64))
#score_rect = score_surface.get_rect(center=(360,60))

#obstacles
snail_surface = pygame.image.load(root_dir + "snail1.png").convert_alpha()
fly_surface = pygame.image.load(root_dir + "fly.png").convert_alpha()
obstacle_rect_list = []


player_surface = pygame.image.load(root_dir + "player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80,300))

player_gravity =0  

#Intro screen
player_stand = pygame.image.load(root_dir + "player_stand.png").convert_alpha() 
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect= player_stand.get_rect(center=(400,200)) 

game_name   = test_font.render("Pixel Runner", False, (111,196,169))
game_name_rect = game_name.get_rect(center=(400,80))

game_message = test_font.render("Press space to start",False,(111,196,169))
game_message_rect = game_message.get_rect(center=(400,340))


#timer
obstacle_timer = pygame.USEREVENT +1
pygame.time.set_timer(obstacle_timer,1500)



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
             if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                  game_active = True
                  
                  start_time = int(pygame.time.get_ticks() /1000)
            
        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(snail_surface.get_rect(bottomright=(randint(900,1100),300)))
            else:
                obstacle_rect_list.append(fly_surface.get_rect(bottomright=(randint(900,1100),210)))
            
    if game_active: 
        screen.blit(test_surface, (200,100))
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        #pygame.draw.rect(screen,"#c0e8ec",score_rect)
        #pygame.draw.rect(screen,"#c0e8ec",score_rect,10)
        #pygame.draw.ellipse(screen,"Brown",pygame.Rect(50,200,100,100))
        #screen.blit(score_surface, score_rect)
        score = display_score()

        #snail_rect.x -= 4
        #if snail_rect.right <= 0:
        #    snail_rect.left = 800
        #screen.blit(snail_surface, snail_rect)
        
        #player
        player_gravity +=1
        player_rect.y+= player_gravity
        if player_rect.bottom >=300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)
        

        #obstacles movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        game_active = collisions(player_rect,obstacle_rect_list)

        #keys= pygame.key.get_pressed()
        #if keys[pygame.K_SPACE]:
        # print("jump")
        
        #mouse_pos = pygame.mouse.get_pos()
        #if player_rect.collidepoint( mouse_pos):
        #    print("collision")
        

        
        
    else: 
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
       
        score_message = test_font.render(f"Your score: {score}",False,(111,196,169))
        score_message_rect = score_message.get_rect(center=(400,340))
        
        screen.blit(game_name, game_name_rect)
        
        if score==0:
             screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
             
        
    #draw elements & update everything
    pygame.display.update()
    clock.tick(60)
