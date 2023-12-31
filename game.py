from typing import Any
import pygame
import os
from sys import exit
from random import randint


class Player(pygame.sprite.Sprite):
     def __init__(self):
          super().__init__()
          player_walk1 = pygame.image.load(root_dir + "player_walk_1.png").convert_alpha()
          player_walk2 = pygame.image.load(root_dir + "player_walk_2.png").convert_alpha()
          self.player_walk=[player_walk1,player_walk2]
          self.player_index =0
          self.player_jump= pygame.image.load(root_dir + "player_jump.png").convert_alpha()    
          
          self.image = self.player_walk[self.player_index]
          self.rect = self.image.get_rect(midbottom=(80,300))
          self.gravity =0
     
     def player_input(self):
          keys = pygame.key.get_pressed()
          if keys[pygame.K_SPACE] and self.rect.bottom >=300:
               self.gravity = -20
     
     def apply_gravity(self):
          self.gravity +=1
          self.rect.y +=self.gravity
          if self.rect.bottom >=300:
               self.rect.bottom =300
     
     def animation_state(self):
          if self.rect.bottom<300:
               self.image=self.player_jump
          else:
               self.player_index+=0.1
               if self.player_index>= len(self.player_walk):self.player_index=0
               self.image =self,player_walk[int(self.player_index)]
     
     def update(self):
          self.player_input()
          self.apply_gravity()
          self.animation_state()

class Obstacle(pygame.sprite.Sprite):
     def _int_(self,type):

          super().__init__()
          if type == "fly":
               fly_1=pygame.image.load(root_dir + "fly.png").convert_alpha()
               fly_2=pygame.image.load(root_dir + "fly2.png").convert_alpha()
               self.frames=[fly_1,fly_2]
               y_pos =210
          else:
               snail_1=pygame.image.load(root_dir + "snail1.png").convert_alpha()
               snail_2=pygame.image.load(root_dir + "snail2.png").convert_alpha()
               self.frames=[snail_1,snail_2]
               y_pos =300

          self.animation_index =0
          self.image = self.frames[self.animation_index]
          self.rect = self.image.get_rect(midbottom=(randint(900,1100),y_pos))
     def animation_state(self):
          self.animation_index +=0.1
          if self.animation_index >= len(self.frames):self.animation_index =0
          self.image   = self.frames[int(self.animation_index)]
     def update(self):
          self.animation_state()




          

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
def player_animation():
     global palyer_surface,player_index
     
     if player_rect.bottom < 300:
         player_surface = player_jump
     else:
            player_index +=0.1
            if player_index >= len(player_walk): player_index =0
            player_surface = player_walk[int(player_index)]


     
     
    
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("game")
clock = pygame.time.Clock()
root_dir = os.path.dirname(__file__) + "/"
test_font = pygame.font.Font(root_dir +"Pixeltype.ttf", 50)
game_active = False
start_time =0
score =0
#groups
player= pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()

test_surface = pygame.Surface((100,200))
test_surface.fill("red")

sky_surface = pygame.image.load(root_dir + "sky.png").convert()

ground_surface = pygame.image.load(root_dir + "ground.png").convert()

#score_surface = test_font.render("My Game", False, (64,64,64))
#score_rect = score_surface.get_rect(center=(360,60))

#obstacles
snail_frame_1 = pygame.image.load(root_dir + "snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load(root_dir + "snail2.png").convert_alpha()
snail_frames=[snail_frame_1,snail_frame_2]
snail_index =0
snail_surface = snail_frames[snail_index]

fly_frame_1 = pygame.image.load(root_dir + "fly.png").convert_alpha()
fly_frame_2 = pygame.image.load(root_dir + "fly2.png").convert_alpha()
fly_frames=[fly_frame_1,fly_frame_2]
fly_index =0
fly_surface = fly_frames[fly_index]
obstacle_rect_list = []


player_walk1 = pygame.image.load(root_dir + "player_walk_1.png").convert_alpha()
player_walk2 = pygame.image.load(root_dir + "player_walk_2.png").convert_alpha()
player_walk=[player_walk1,player_walk2]
player_index =0
player_jump= pygame.image.load(root_dir + "player_jump.png").convert_alpha()

player_surface = player_walk[player_index]
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

snail_animation_timer = pygame.USEREVENT +2
pygame.time.set_timer(snail_animation_timer,500)
fly_animation_timer = pygame.USEREVENT +3
pygame.time.set_timer(fly_animation_timer,200)



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
        if game_active:  
     
             if event.type == obstacle_timer :
               
                if randint(0,2):
                   obstacle_rect_list.append(snail_surface.get_rect(bottomright=(randint(900,1100),300)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(bottomright=(randint(900,1100),210)))
        
             if event.type == snail_animation_timer:
                if snail_index ==0:
                    snail_index =1
                else:
                    snail_index =0
                snail_surface = snail_frames[snail_index]
             if event.type == fly_animation_timer:
                if fly_index ==0:
                    fly_index =1
                else:
                    fly_index =0
                fly_surface = fly_frames[fly_index]
    
    
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
        if player_rect.bottom >=300:player_rect.bottom = 300
        player_animation()
        screen.blit(player_surface, player_rect)
        
        player.update()
       
        

        #obstacles movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        #collisions
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
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity =0
       
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
