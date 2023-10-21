import pygame, sys, math, os, random, time
from pygame.locals import QUIT


fps = 240

windowHeight = 324 #hieght in pixels of my game windpow
windowLength = 572 #length in pixels of my game window 

display = pygame.display.set_mode((windowLength, windowHeight)) # initiises 

halfLength = int(windowLength / 2) #half of length
halfHeight = int(windowHeight / 2) # hhalf or height 

white = (255,255,255,60)
pygame.init() #initialises pyhame 
clock = pygame.time.Clock() # defines a clock in which the game refereshes at 
bullets = []
bullets1 = []
enemies = []
enemybulls = []
destroyedenemies = []
#images used in the game 
player1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "Corvette", "boost4.png" )), (40,24))
playerbull1 = pygame.image.load(os.path.join("images", "Corvette", "pixel_art.png" ))
playerbull2 = pygame.image.load(os.path.join("images", "Corvette", "pixel_art.png" ))
imp = pygame.image.load(os.path.join("images", "1.png"))
imp1 = pygame.image.load(os.path.join("images", "2.png"))
imp2 = pygame.image.load(os.path.join("images", "3.png"))
imp3 = pygame.image.load(os.path.join("images", "5.png"))
enemypicture = pygame.image.load(os.path.join("images", "Corvette", "enemynormal.png" ))
enemybullet = pygame.image.load((os.path.join("images", "Corvette", "enemybullet.png" )))
destroyedenemy = pygame.image.load((os.path.join("images", "Corvette", "destroyedenemy.png" ))).convert()

def playertracking(image, topleft):
     mx, my = pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]
     ix, iy = image.get_rect(topleft = topleft).center
     if iy < my:
          if mx - ix == 0:
             turnedimage = pygame.transform.rotate(image, 90)
          else:    
             turnedimage = pygame.transform.rotate(image, math.degrees(math.atan((abs(my - iy)/abs(mx - ix)))))
     elif iy> my:
          if mx - ix == 0:
             turnedimage = pygame.transform.rotate(image, -90)
          else:    
             turnedimage = pygame.transform.rotate(image, -math.degrees(math.atan((abs(my - iy)/abs(mx - ix)))))
     else:
          turnedimage = pygame.transform.rotate(image, 0)
     turnedimagerect = turnedimage.get_rect(center = image.get_rect(topleft = topleft).center)
     return turnedimage, turnedimagerect

     u09iu


def enemydirection(x,y):
  if x < pygame.mouse.get_pos()[0]:
     directionB = random.choice(['bLeft', 'bRight', 'back'])
     return directionB   
  elif math.sqrt((abs(pygame.mouse.get_pos()[0] - x)^2) + ((abs(pygame.mouse.get_pos()[1] - y)^2))) < 10:
     valBackRight = math.sqrt((abs(pygame.mouse.get_pos()[0] - (x+7))^2) + ((abs(pygame.mouse.get_pos()[1] - (y+7))^2)))
     valBAckLeft = math.sqrt((abs(pygame.mouse.get_pos()[0] - (x+10))^2) + ((abs(pygame.mouse.get_pos()[1] - y)^2)))
     valBack = math.sqrt((abs(pygame.mouse.get_pos()[0] - (x+7))^2) + ((abs(pygame.mouse.get_pos()[1] - (y-7))^2)))
     if valBackRight >= valBAckLeft or valBack:
          return "bRight"
     elif valBAckLeft >= valBack:
          return "bLeft"
     else:
          return "back"
     
  else:
     directionIn = random.choice(['left', 'right', 'forward'])
     return directionIn

class enemy():
     def __init__(self, x,y, health, timer, angle):
          self.x = x
          self.y = y
          self.health = health
          self.timer = time.time()



def img1(x,y,z):
    #used for the fake parralax effects
    display.blit(x, (y, 0)) #places the images in the x and y coords i give
    display.blit(x, (z, 0)) #places the images in the x and y coords i give
    

pygame.time.set_timer(28, 1000) 
 #actual function of gameplay
def main():
  dead = False
  spaceship_clicked = False   
  shot = False
  first = False
  enemycooldown = False 
  lowertrans = False
  score =0
  
  
  health = 100
  
#   shot = pygame.mixer.Sound("shot.wav")
#   gamemusic = pygame.mixer.Sound("gamemusic.wav")
  gunspeed = 10 

  # different scroll values so that the differnt images 
  # can move at different speed to give a 
  # more realistic effect of movement 
  scroll = 0
  scroll1 = display.get_width()
  scroll3 = 0
  scroll4 = display.get_width()
  scroll5 = 0
  scroll6 = display.get_width()

  pygame.display.set_caption('Shooting game')
  #while loop that runs while the condition is met
  #at the end the screen gets updated 
  #so the values for the moving background get changed 
  # then the screen updates at the end of the loop
  while not dead:
    for event in pygame.event.get():
          print(event)
          
          #pygame.event.set_grab(True)

          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_ESCAPE:
                   dead = True
                                
          
          if event.type == pygame.MOUSEBUTTONDOWN:
               #players hitbox
               
               #made by creating a rectangle which can detect if otther rectangle touch
               
               if spaceship_clicked == False:
                    #when tha game starts checks if ship has been clicked then starts movement 
                    if player1.get_rect(topleft = (10,halfHeight-12)).collidepoint(pygame.mouse.get_pos())==True:
                         spaceship_clicked = True
                         bullets.append([pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]])
                         bullets1.append([pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]])
                         #pygame.time.set_timer(25, 60) 
                         #pygame.time.set_timer(26, 1000)    
                         pygame.mixer.music.load("music and fx/music_zapsplat_game_music_arcade_electro_repeating_retro_arp_electro_drums_serious_012 (mp3cut.net).mp3")
                         pygame.mixer.music.play(-1,0,0)
                         pygame.mixer.Sound.play(pygame.mixer.Sound("music and fx/shoot02wav-14562 (mp3cut.net).mp3"),0,0,0)

                         """ print("jdnc")
                         if first == False:
                              for i in range(4):
                                   enemies.append([571, random.randint(24, 300), 3, time.time_ns()/1000000])
                              first = True
 """
          if event.type == 25:
               shot = False     

          if event.type == 26:
               enemycooldown = False 
          
          if event.type == 28:
               lowertrans = False

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(score), True, white, None)
    text1 = font.render(str(health), True, white, None)

    pygame.draw.rect(display, white, pygame.Rect(10, 282, 32, 32))

    #runs through a list with bullets in it and appends their location by positive 5

    for b in range(len(bullets)):
          bullets[b][0] += 5

    #runs through the enemy list of bullets ans append their location by negative 10

    for b in range(len(enemybulls)):
          enemybulls[b][0] -= 10     
  
    #runs through the player bullets and checks if they are off the screen if yes remove the bullet fron the list
    #introduced in my second iteration as if this wasnt hear the game would dramatically slow down the more bullets were added

    for bullet in bullets[:]:
         if bullet[0] > 572:
               bullets.remove(bullet)


    #does the same as the players bullets but for the enemy bukllets 

    for b in enemybulls[:]:
         if b[0] < -24:
               enemybulls.remove(b)           


    # checks for enemy collision with the player bullets 
    for enemy in enemies:
         for bullet in bullets:
              if playerbull1.get_rect(topleft=(bullet[0],bullet[1])).colliderect(enemypicture.get_rect(topleft=(enemy[0],enemy[1])))==True:
                     enemy[2] -= 1       
                     bullets.remove(bullet)

    # this is the vice versa as it checks the player collision with the enemy bullets 
    for b in enemybulls:
         if player1.get_rect(topleft = (pygame.mouse.get_pos()[0]-20, pygame.mouse.get_pos()[1]-12)).colliderect(enemybullet.get_rect(topleft=(b[0],b[1])))==True:
             health -= 2   
             enemybulls.remove(b)  

     #checks if the  enemies health is 0 and the removes the enemy and replaces with a dedstroyed enemypicture and plays a bomb sound                        

    for enemy in enemies[:]:
         if enemy[2]<= 0:
              score += 10
              destroyedenemies.append([enemy[0], enemy[1], 256])
              enemies.remove(enemy)           
              pygame.mixer.Sound.play(pygame.mixer.Sound("music and fx/hq-explosion-6288 (1).mp3"),0,0,0)
         elif enemy[1] > 348 or enemy[1] < 0:
              enemies.remove(enemy)    



    #code that deals with the parralax
      
    display.blit(imp, (0, 0))
    
    scroll = scroll - 0.1
    scroll1 = scroll1 - 0.1
    img1(imp1,scroll,scroll1)
    if(scroll<= -(display.get_width())):
         scroll = 0

    if(scroll1<= 0):
         scroll1= display.get_width()
    scroll3 = scroll3 - 1
    scroll4 = scroll4 - 1
    
    img1(imp2,scroll3,scroll4)
    if(scroll3<= -(display.get_width())):
         scroll3 = 0

    if(scroll4<= 0):
         scroll4 = display.get_width()
    scroll5 = scroll5 - 1.5
    scroll6 = scroll6 - 1.5
    
    img1(imp3,scroll5,scroll6)
    if(scroll5<= -(display.get_width())):
         scroll5 = 0

    if(scroll6<= 0):
         scroll6 = display.get_width()

    for i in bullets:
          display.blit(playerbull1, pygame.Rect(i[0],i[1], 0, 0)) 

    for i in enemybulls:
          display.blit(enemybullet, pygame.Rect(i[0],i[1], 0, 0))      
          
    for i in destroyedenemies:
          destroyedenemy.set_alpha(i[2])
          display.blit(destroyedenemy, pygame.Rect(i[0],i[1], 0, 0))
          if lowertrans == False:
               i[2] -= 1
               lowertrans = True
               pygame.time.set_timer(28, 1000) 
           
    
    #some code here is in its on if loop as these are are things that are initial at the "start of the game" which is whwn the spaceship is clicked but the rest code that maybe similar ddoes not need to depend on spaceship clickicked as the are derived from the player or the initial 4 enemies
    if spaceship_clicked==True:
          display.blit(player1,(pygame.mouse.get_pos()[0]-20, pygame.mouse.get_pos()[1]-12))
          if enemycooldown == False:
             """ if len(enemies)<8:
               for i in range(random.randint(1,3)):
                  enemies.append([571, random.randint(24, 300), 3, time.time_ns()/1000000])  

             for enemy in enemies:
                  if time.time_ns()/1000000 - enemy[3] > 15 :
                       enemybulls.append([enemy[0],enemy[1]])
                       pygame.mixer.Sound.play(pygame.mixer.Sound("music and fx/blaster-2-81267 (mp3cut.net) (1).mp3"),0,0,0)
                       enemy[3] = time.time_ns()/1000000 """
                       


             pygame.time.set_timer(26, 800) 
             enemycooldown= True

          for enemy in enemies:
              direc = enemydirection(enemy[0], enemy[1])
              if direc == "left":
                    enemy[1] -= 1
                    enemy[0] -= 1
                    
                    display.blit(playertracking(enemypicture, (enemy[0], enemy[1]))[0], playertracking(enemypicture, (enemy[0], enemy[1]))[1])

              elif direc == "right":
                    enemy[1] += 1
                    enemy[0] -= 1	
                    
                    display.blit(playertracking(enemypicture, (enemy[0], enemy[1]))[0], playertracking(enemypicture, (enemy[0], enemy[1]))[1])

              elif direc == "forward":
                    enemy[0] -= 2
                    
                    display.blit(playertracking(enemypicture, (enemy[0], enemy[1]))[0], playertracking(enemypicture, (enemy[0], enemy[1]))[1])

              elif direc == "bLeft":
                    enemy[1] -= 1
                    enemy[0] += 1
                    
                    display.blit(playertracking(enemypicture, (enemy[0], enemy[1]))[0], playertracking(enemypicture, (enemy[0], enemy[1]))[1])


              elif direc == "bRight":
                    enemy[1] += 1
                    enemy[0] += 1
                
                    display.blit(playertracking(enemypicture, (enemy[0], enemy[1]))[0], playertracking(enemypicture, (enemy[0], enemy[1]))[1])


              else:
                    enemy[0] += 2
                    
                    display.blit(playertracking(enemypicture, (enemy[0], enemy[1]))[0], playertracking(enemypicture, (enemy[0], enemy[1]))[1])


          if pygame.mouse.get_pressed()[0]:
               
               if shot == False:
                    bullets.append([pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]])
                    bullets1.append([pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]])
                    pygame.mixer.Sound.play(pygame.mixer.Sound("music and fx/shoot02wav-14562 (mp3cut.net).mp3"),0,0,0)


                    pygame.time.set_timer(25, 80)
                    shot = True
               #break

    #at the end of the game loop the player is displayed on the screen

    else:
          display.blit(player1, (10, halfHeight - 12))
               #break

         
     
   

    """ display.blit(text, [0,0])
    display.blit(text1, [100,292]) """
    #pygame.draw.rect(display, white, pygame.Rect(10, 282, 32, 32))
    #updates the screen with all the elements drawn to it to the display i defined earlier
    pygame.display.update()
    clock.tick(fps)

 

#main function called
main()