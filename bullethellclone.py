import pygame
from pygame.locals import QUIT
import sys
import math
import os
import random
import time
from pygame.math import *

fps = 240

windowHeight = 324  # hieght in pixels of my game windpow
windowLength = 572  # length in pixels of my game window

display = pygame.display.set_mode((windowLength, windowHeight))  # initiises

halfLength = int(windowLength / 2)  # half of length
halfHeight = int(windowHeight / 2)  # half or height

white = (255, 255, 255, 60)

pygame.init()  # initialises pyhame
pygame.mixer.init()
# defines a clock in which the game refereshes at
clock = pygame.time.Clock()

# images used in the game
player1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "Corvette", "boost4.png")), (40, 24))
playerbull1 = pygame.image.load(os.path.join("images", "Corvette", "pixel_art.png"))
imp = pygame.image.load(os.path.join("images", "1.png"))
imp1 = pygame.image.load(os.path.join("images", "2.png"))
imp2 = pygame.image.load(os.path.join("images", "3.png"))
imp3 = pygame.image.load(os.path.join("images", "5.png"))
bossenemy = pygame.image.load(os.path.join("images", "Corvette", "bossenemy.png"))
destroyedplayer = pygame.image.load((os.path.join("images", "Corvette", "destroyedplayer.png")))
destroyedbossenemy = pygame.image.load((os.path.join("images", "Corvette", "destroyedbossenemy.png")))
enemypicture = pygame.image.load(os.path.join("images", "Corvette", "enemynormal.png"))
enemybullet = pygame.image.load((os.path.join("images", "Corvette", "enemybullet.png")))
bossbullet = pygame.image.load((os.path.join("images", "Corvette", "bossbullet.png")))
destroyedenemy = pygame.image.load((os.path.join("images", "Corvette", "destroyedenemy.png")))
multiplier = pygame.image.load((os.path.join("images", "Corvette", "multiplier.png"))), "multiplier"
lazerspeedup = pygame.image.load((os.path.join("images", "Corvette", "lazerspeedup.png"))), "lazerspeedup"
doublelazers = pygame.image.load((os.path.join("images", "Corvette", "doublelazers.png"))), "doublelazers"
healthpickup = pygame.image.load((os.path.join("images", "Corvette", "health.png"))), "healthpickup"
multiplier1 = pygame.transform.scale(pygame.image.load((os.path.join("images", "Corvette", "multiplier.png"))),
                                     (45, 45))
lazerspeedup1 = pygame.transform.scale(pygame.image.load((os.path.join("images", "Corvette", "lazerspeedup.png"))),
                                       (45, 45))
doublelazers1 = pygame.transform.scale(pygame.image.load((os.path.join("images", "Corvette", "doublelazers.png"))),
                                       (45, 45))
healthpickup1 = pygame.transform.scale(pygame.image.load((os.path.join("images", "Corvette", "health.png"))), (45, 45))
greyoverlay = pygame.image.load((os.path.join("images", "greyoverlay.png")))

multiplier1.set_alpha(100)
lazerspeedup1.set_alpha(100)
doublelazers1.set_alpha(100)
healthpickup1.set_alpha(100)

sAn = []


def img1(x, y, z):
    # used for the fake parralax effect
    display.blit(x, (y, 0))  # places the images in the x and y coords i give
    display.blit(x, (z, 0))  # places the images in the x and y coords i give


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image, deathimage, health, timer, speed, boss):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = image
        self.turnedimage = image
        self.rect = self.turnedimage.get_rect()
        self.center1 = self.turnedimage.get_rect(topleft=(self.x, self.y)).center
        self.health = health
        self.timer = time.time()
        self.angle = 0
        self.deathimage = deathimage
        self.ix, self.iy = self.turnedimage.get_rect(topleft=(self.x, self.y)).center
        self.dead = False
        self.transparencyvalue = 255
        self.score = 10
        self.droppowerup = random.choice([False, True])
        self.spawnedpowerup = False
        self.isboss = boss

    def upd(self):
        if self.dead == False:

            if not self.isboss:
                if self.y > 314:
                    directionB = random.choice(['bLeft', 'left'])
                elif self.y < 50:
                    directionB = random.choice(['bRight', 'right'])
                elif self.x > 540:
                    directionB = 'forward'
                elif self.x < pygame.mouse.get_pos()[0] + 30:
                    directionB = random.choice(['back'])
                elif math.sqrt((abs(pygame.mouse.get_pos()[0] - self.x) ^ 2) + (
                        (abs(pygame.mouse.get_pos()[1] - self.y) ^ 2))) < 10:
                    directionB = random.choice(['bLeft', 'bRight', 'back'])

                else:
                    directionB = random.choice(['left', 'right', 'forward'])

                if directionB == "left":
                    self.x -= 1
                    self.y -= 1
                elif directionB == "right":
                    self.x -= 1
                    self.y += 1
                elif directionB == "forward":
                    self.x -= 2
                elif directionB == "bLeft":
                    self.x += 1
                    self.y -= 1
                elif directionB == "bRight":
                    self.x += 1
                    self.y += 1
                else:
                    self.x += 2

                self.ix, self.iy = self.turnedimage.get_rect(topleft=(self.x, self.y)).center
                self.center1 = self.ix, self.iy
            else:
                #update for the boss enemy
                if self.x > 560:
                    directionB = 'forward'
                elif self.y > 314:
                    directionB = random.choice(['right'])
                elif self.y < 50:
                    directionB = random.choice(['left'])
                elif self.x < 470:
                    directionB = random.choice(['back'])
                elif self.y < pygame.mouse.get_pos()[1]:
                    directionB = random.choice(['left'])
                elif self.y > pygame.mouse.get_pos()[1]:
                    directionB = random.choice(['right'])
                else:
                    directionB = random.choice(['forward'])

                if directionB == "left":
                    self.x -= 1
                    self.y += 1
                elif directionB == "right":
                    self.x -= 1
                    self.y -= 1
                elif directionB == "forward":
                    self.x -= 2
                elif directionB == "back":
                    self.x += 2
                    self.y -= 0

                self.ix, self.iy = self.turnedimage.get_rect(topleft=(self.x, self.y)).center
                self.center1 = self.ix, self.iy

    def show(self):
        if self.health > 0:
            if not self.isboss:
                mx, my = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                ix, iy = self.turnedimage.get_rect(topleft=(self.x, self.y)).center
                if mx - ix != 0:
                    self.angle = math.degrees(math.atan((abs(my - iy) / abs(mx - ix))))
                if iy < my:
                    if mx - ix == 0:
                        self.turnedimage = pygame.transform.rotate(self.image, 90)
                    else:
                        angle = math.degrees(math.atan((abs(my - iy) / abs(mx - ix))))
                        self.turnedimage = pygame.transform.rotate(self.image, self.angle)
                elif iy > my:
                    if mx - ix == 0:
                        self.turnedimage = pygame.transform.rotate(self.image, -90)
                    else:
                        # self.angle = -math.degrees(math.atan((abs(my - iy)/abs(mx - ix))))
                        self.turnedimage = pygame.transform.rotate(self.image, -self.angle)
                else:
                    self.turnedimage = pygame.transform.rotate(self.image, 0)
                self.rect = self.turnedimage.get_rect(center=(ix, iy))
                display.blit(self.turnedimage, self.rect)
            else:
                #show for the boss enemy
                self.angle = 0
                self.rect = self.turnedimage.get_rect(center=(self.x, self.y))
                display.blit(self.turnedimage, self.rect)

        else:
            self.dead = True
            self.deathimage.set_alpha(self.transparencyvalue)
            display.blit(self.deathimage, self.deathimage.get_rect(center=(self.ix, self.iy)))
            self.transparencyvalue -= 1
            if self.transparencyvalue <= 0:
                self.kill()


class enemybullets(pygame.sprite.Sprite):
    def __init__(self, e, image, bossimage, bull):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.bossimage = bossimage
        self.turnedimage = image
        self.angle = e.angle
        self.center1 = e.center1
        self.angle1 = 0
        self.noshooting = e.dead
        self.bossbullet = e.isboss
        mx, my = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

        self.direction = 0
        self.ix, self.iy = e.ix, e.iy


        if self.bossbullet == False:
            if self.iy < my:
                if mx - self.ix == 0:
                    self.turnedimage = pygame.transform.rotate(self.image, 90)
                else:
                    # angle = math.degrees(math.atan((abs(my - iy)/abs(mx - ix))))
                    self.turnedimage = pygame.transform.rotate(self.image, self.angle)
            elif self.iy > my:
                if mx - self.ix == 0:
                    self.turnedimage = pygame.transform.rotate(self.image, -90)
                else:
                    # self.angle = -math.degrees(math.atan((abs(my - iy)/abs(mx - ix))))
                    self.turnedimage = pygame.transform.rotate(self.image, -self.angle)

            self.bulletpos = pygame.math.Vector2(self.center1)
            self.mousepos = pygame.math.Vector2(mx, my)
            self.direction = self.mousepos - self.bulletpos
        else:
            # the 4 different values that also get p[assed into the creation of an enemy bullet
            # which take on the value from i in a for loop to add 4 different bullets in different
            # locations for the boss
            if bull == 1:
                self.iy -= 46
            elif bull == 2:
                self.iy -= 38
            elif bull == 4:
                self.iy -= 22
            elif bull == 3:
                self.iy -= 13

        if self.noshooting == True:
            self.kill()

    def movebullet(self):
        if self.bossbullet == False:
            self.center1 += self.direction.normalize() * 2
            if self.center1[0] < 0 - (self.image.get_width() / 2) or self.center1[1] > windowHeight + (
                    self.image.get_width() / 2) or self.iy < 0 - (self.image.get_width() / 2):
                self.kill()
        else:
            self.ix -= 3
            self.center1 = self.ix, self.iy
            if self.ix < 0 - (self.image.get_width() / 2):
                self.kill()

    def drawbullet(self):
        if not self.bossbullet:
            display.blit(self.turnedimage, self.turnedimage.get_rect(center=self.center1))
        else:
            display.blit(self.bossimage, self.bossimage.get_rect(center=(self.ix, self.iy)))


class powerups(pygame.sprite.Sprite):
    def __init__(self, e, image, typeof):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.typeof = typeof
        self.center1 = e.center1
        self.transparencyvalue = 255
        self.ix = e.ix
        self.iy = e.iy

    def movepowerup(self):
        self.ix -= 1
        self.image.set_alpha(self.transparencyvalue)
        self.transparencyvalue -= 1
        if self.transparencyvalue <= 0:
            self.kill()

        if self.center1[0] < 0 - (self.image.get_width() / 2):
            self.kill()

    def drawpowerup(self):

        display.blit(self.image, self.image.get_rect(center=(self.ix, self.iy)))


class Player(pygame.sprite.Sprite):
    def __init__(self, image, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.center1 = (50, 50)
        self.health = health
        self.doublelazers = False
        self.slowdown = False
        self.lazerspeedup = False
        self.multiplier = False

    def moveplayer(self):
        self.center1 = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
        if self.center1[0] < 0:
            pygame.mouse.set_pos(0, pygame.mouse.get_pos()[1])

    def drawplayer(self):
        display.blit(self.image, self.image.get_rect(center=self.center1))
        r = self.image.get_rect(center=self.center1)
        rect = pygame.Rect(r.x, r.y - 20, 40, 6)
        pygame.draw.rect(display, (128, 0, 0), rect)
        rect = pygame.Rect(r.x, r.y - 20, 40 * (self.health / 100), 6)
        pygame.draw.rect(display, (0, 128, 0), rect)

    def resetplayer(self):
        self.health = 100

    def pickuppowerup(self, typeof):
        if typeof == "healthpickup":
            if healthpickup1.get_alpha() == 100:
                if 85 > self.health > 0:
                    self.health += 15
                else:
                    health = 100 - self.health
                    self.health += health
        elif typeof == "lazerspeedup":
            if not self.lazerspeedup:
                self.lazerspeedup = True
                lazerspeedup1.set_alpha(255)
                pygame.time.set_timer(27, 23, 1)
        elif typeof == "doublelazers":
            if not self.doublelazers:
                self.doublelazers = True
                doublelazers1.set_alpha(255)
                pygame.time.set_timer(29, 23, 1)
        elif typeof == "multiplier":
            if not self.multiplier:
                self.multiplier = True
                multiplier1.set_alpha(255)
                pygame.time.set_timer(30, 23, 1)


class playerbullet(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.ix = x
        self.iy = y

    def movebullet(self):
        self.ix += 5
        if self.ix > 572:
            self.kill()

    def drawbullet(self):
        display.blit(self.image, self.image.get_rect(center=(self.ix, self.iy)))
        pygame.display.update()


class Button:
    def __init__(self, x, y, colour, text, height, width, scale):
        self.x = x
        self.y = y
        self.colour = colour
        self.text = text
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rectcenter = self.rect.center
        self.scale = scale
        self.scale1 = scale
        self.scale2 = scale

    #draws the buttons and makes sure the scaling works
    def draw(self):
        outlinerect = pygame.Rect(self.x - 2, self.y - 2, self.width + 5, self.height + 4)
        pygame.draw.rect(display, (255, 255, 255), outlinerect.scale_by(self.scale2, self.scale2), 0, 5)
        pygame.draw.rect(display, self.colour, self.rect.scale_by(self.scale1, self.scale1), 0, 5)

        if self.text != "":
            font = pygame.font.Font('freesansbold.ttf', 12)
            text = font.render(self.text, True, (255, 255, 255))
            display.blit(text, (self.x + ((self.width / 2) - (text.get_width() / 2)),
                                self.y + ((self.height / 2) - (text.get_height() / 2))))
    #checks mousehover but also click, if hover is detected the scale is changed
    def mousehover(self, mousepos):
        if self.rect.collidepoint(mousepos) == True:
            self.scale1 = 0.9
            self.scale2 = 0.92
            if pygame.mouse.get_pressed()[0] == True:
                return True
        else:

            self.scale1 = self.scale
            self.scale2 = self.scale


pygame.time.set_timer(28, 15)


# actual function of gameplay


def main():
    dead = False
    spaceship_clicked = False
    shot = False
    first = False
    enemycooldown = False
    score = 0

    play = False
    highscores = False
    settings = False
    playername = "click to type"
    input = False
    home = True
    scores = []
    death = False
    writehighscore = True
    displayhighscores = False
    boss = 0

    pu1 = 255
    pu2 = 255
    pu3 = 255
    pu4 = 255

    scroll = 0
    scroll1 = display.get_width()
    scroll3 = 0
    scroll4 = display.get_width()
    scroll5 = 0
    scroll6 = display.get_width()
    d = 0
    u = 5
    overlaytransparency = 255
    firerate = 90
    player = Player(player1, 100)


    # group of class instances declared
    enemys = pygame.sprite.Group()
    enemybullett = pygame.sprite.Group()
    powerupss = pygame.sprite.Group()
    playerbullets = pygame.sprite.Group()

    pygame.display.set_caption('Shooting game')
    # while loop that runs while the condition is met
    # at the end the screen gets updated
    # so the values for the moving background get changed then the screen updates at the end of the loop

    while not dead:

        for event in pygame.event.get():
            print(event)

            # locks mouse movement to the window
            #pygame.event.set_grab(True)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    dead = True
                if input == True:
                    if event.key == pygame.K_RETURN:
                        input = False
                    elif event.key == pygame.K_BACKSPACE:
                        playername = playername[:-1]
                    else:
                        if len(playername) < 13:
                            playername += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:

                if spaceship_clicked == False:
                    if player1.get_rect(topleft=(10, halfHeight - 12)).collidepoint(pygame.mouse.get_pos()) == True:
                        spaceship_clicked = True
                        playerbullets.add(playerbullet((player.center1[0]), (player.center1[1]), playerbull1))
                        pygame.mixer.music.load(
                            "music and fx/music_zapsplat_game_music_arcade_electro_repeating_retro_arp_electro_drums_serious_012 (mp3cut.net).mp3")
                        pygame.mixer.music.play(-1, 0, 0)
                        pygame.mixer.Sound.play(pygame.mixer.Sound("music and fx/shoot02wav-14562 (mp3cut.net).mp3"), 0,
                                                0, 0)

                        if first == False:
                            for i in range(1):
                                enemys.add(
                                    Enemy(250, random.randint(50, 100), enemypicture, destroyedenemy, 3, time.time_ns(),
                                          1, False))

                            first = True

            # shot countdown timer
            if event.type == 25:
                shot = False
            # enemy shot countdown timer
            if event.type == 26:
                enemycooldown = False

            if event.type == 27:
                if pu2 > 101:
                    firerate = 60
                    pu2 -= 2
                    lazerspeedup1.set_alpha(pu2)
                    pygame.time.set_timer(27, 23, 1)
                else:
                    firerate = 90
                    player.lazerspeedup = False
                    pu2 = 255

            if event.type == 29:
                if pu3 > 101:
                    pu3 -= 1
                    doublelazers1.set_alpha(pu3)
                    pygame.time.set_timer(29, 23, 1)
                else:
                    pu3 = 255
                    player.doublelazers = False

            if event.type == 30:
                if pu4 > 101:
                    pu4 -= 1
                    multiplier1.set_alpha(pu4)
                    pygame.time.set_timer(30, 23, 1)
                else:
                    pu4 = 255
                    player.multiplier = False

        # home screem. I have a bool which when true allows the main
        # game code to run. else display the play settings and highscore button

        if home == True:
            display.blit(imp, (0, 0))

            scroll = scroll - 0.1
            scroll1 = scroll1 - 0.1
            img1(imp1, scroll, scroll1)
            if (scroll <= -(display.get_width())):
                scroll = 0

            if (scroll1 <= 0):
                scroll1 = display.get_width()
            scroll3 = scroll3 - 1
            scroll4 = scroll4 - 1

            img1(imp2, scroll3, scroll4)
            if (scroll3 <= -(display.get_width())):
                scroll3 = 0

            if (scroll4 <= 0):
                scroll4 = display.get_width()
            scroll5 = scroll5 - 1.5
            scroll6 = scroll6 - 1.5

            img1(imp3, scroll5, scroll6)
            if (scroll5 <= -(display.get_width())):
                scroll5 = 0

            if (scroll6 <= 0):
                scroll6 = display.get_width()

            display.blit(greyoverlay, (0, 0))

            font1 = pygame.font.Font('freesansbold.ttf', 50)
            text2 = font1.render("Shooty Game", True, white, None)
            display.blit(text2, [(halfLength - (text2.get_width() / 2)), 50])

            # displays some buttons
            # and checks for mouse collision and clicks in the
            # button methods

            button1 = Button(230, 130, (0, 0, 0), "play", 30, 90, 1)

            button2 = Button(230, 180, (0, 0, 0), "settings", 30, 90, 1)

            button3 = Button(230, 230, (0, 0, 0), "highscores", 30, 90, 1)

            button4 = Button(512, 284, (0, 0, 0), "exit", 20, 40, 1)

            button1.mousehover(pygame.mouse.get_pos())
            button2.mousehover(pygame.mouse.get_pos())
            button3.mousehover(pygame.mouse.get_pos())
            button4.mousehover(pygame.mouse.get_pos())
            button1.draw()
            button2.draw()
            button3.draw()
            button4.draw()
            if button1.mousehover(pygame.mouse.get_pos()) == True:
                play = True
                home = False
            if button2.mousehover(pygame.mouse.get_pos()) == True:
                settings = True
                home = False
            if button3.mousehover(pygame.mouse.get_pos()) == True:
                highscores = True
                home = False
                displayhighscores = True

                file = open("scores.txt", "r")
                for line in file:
                    scores.append(line.split(";"))
                file.close()
            if button4.mousehover(pygame.mouse.get_pos()) == True:
                dead = True
        if settings == True:
            display.blit(imp, (0, 0))

            scroll = scroll - 0.1
            scroll1 = scroll1 - 0.1
            img1(imp1, scroll, scroll1)
            if (scroll <= -(display.get_width())):
                scroll = 0

            if (scroll1 <= 0):
                scroll1 = display.get_width()
            scroll3 = scroll3 - 1
            scroll4 = scroll4 - 1

            img1(imp2, scroll3, scroll4)
            if (scroll3 <= -(display.get_width())):
                scroll3 = 0

            if (scroll4 <= 0):
                scroll4 = display.get_width()
            scroll5 = scroll5 - 1.5
            scroll6 = scroll6 - 1.5

            img1(imp3, scroll5, scroll6)
            if (scroll5 <= -(display.get_width())):
                scroll5 = 0

            if (scroll6 <= 0):
                scroll6 = display.get_width()

            greyoverlay.set_alpha(255)
            display.blit(greyoverlay, (0, 0))

            font1 = pygame.font.Font('freesansbold.ttf', 50)
            font2 = pygame.font.Font('freesansbold.ttf', 12)
            text2 = font1.render("Settings and Help", True, white, None)
            display.blit(text2, [(halfLength - (text2.get_width() / 2)), 50])
            text7 = font2.render("Enter the name that will show up on highscores", True, white, None)
            text3 = font2.render("To control the player all you need to is move the", True, white, None)
            text4 = font2.render("mouse. To shoot all you need to do is click rmb.", True, white, None)
            text5 = font2.render("And powerups automatially get used but there", True, white, None)
            text6 = font2.render("is a slight cooldown. have fun!", True, white, None)
            display.blit(text7, [(halfLength - 50), 130])
            display.blit(text3, [(halfLength - 50), 170])
            display.blit(text4, [(halfLength - 50), 190])
            display.blit(text5, [(halfLength - 50), 210])
            display.blit(text6, [(halfLength - 50), 230])

            # displays some buttons and text box
            # and checks for mouse collision and clicks in the
            # button methods
            button1 = Button(100, 130, (128, 128, 128), playername, 30, 90, 1)

            button2 = Button(100, 180, (0, 0, 0), "save name ", 30, 90, 1)

            button3 = Button(100, 230, (0, 0, 0), "back", 30, 90, 1)

            button2.mousehover(pygame.mouse.get_pos())
            button3.mousehover(pygame.mouse.get_pos())
            button1.draw()
            button2.draw()
            button3.draw()
            if button3.mousehover(pygame.mouse.get_pos()) == True:
                home = True
                settings = False
                input = False
            if button1.mousehover(pygame.mouse.get_pos()) == True:
                settings = True
                playername = ""
                input = True
            if button2.mousehover(pygame.mouse.get_pos()) == True:
                input = False

                # writes the name typed into the box if the player clicks the submit button
                file = open("currentplayer.txt", "w")
                file.write(playername)
                file.close()

        if highscores == True:
            display.blit(imp, (0, 0))

            scroll = scroll - 0.1
            scroll1 = scroll1 - 0.1
            img1(imp1, scroll, scroll1)
            if (scroll <= -(display.get_width())):
                scroll = 0

            if (scroll1 <= 0):
                scroll1 = display.get_width()
            scroll3 = scroll3 - 1
            scroll4 = scroll4 - 1

            img1(imp2, scroll3, scroll4)
            if (scroll3 <= -(display.get_width())):
                scroll3 = 0

            if (scroll4 <= 0):
                scroll4 = display.get_width()
            scroll5 = scroll5 - 1.5
            scroll6 = scroll6 - 1.5

            img1(imp3, scroll5, scroll6)
            if (scroll5 <= -(display.get_width())):
                scroll5 = 0

            if (scroll6 <= 0):
                scroll6 = display.get_width()

            display.blit(greyoverlay, (0, 0))
            font1 = pygame.font.Font('freesansbold.ttf', 50)
            font2 = pygame.font.Font('freesansbold.ttf', 12)
            text2 = font1.render("Highscores", True, white, None)
            display.blit(text2, [(halfLength - (text2.get_width() / 2)), 50])

            # opens sores file and reads each line into a 2 item list
            # the player name and score
            # then displays them to the screen with variable d and u
            # controlling the space between the text
            if displayhighscores == True:
                with open("scores.txt") as f:
                    for line in f:
                        sAn.append(line.split(";"))

                for i in range(len(sAn)):
                    solved = False
                    for j in range(len(sAn) - 1):

                        if float(sAn[j][1]) < float(sAn[j + 1][1]):
                            item1 = sAn[j][0]
                            item2 = sAn[j][1]
                            sAn[j][0] = sAn[j + 1][0]
                            sAn[j][1] = sAn[j + 1][1]
                            sAn[j + 1][0] = item1
                            sAn[j + 1][1] = item2

                            solved = True
                    if not solved:
                        break

                file = open("scores.txt", "w")
                file.write("")
                file.close()
                for i in range(len(sAn)):
                    file = open("scores.txt", "a")
                    file.write(sAn[i][0] + ";" + sAn[i][1])
                    file.close()
            if len(sAn) < 10:
                for i in range(len(sAn)):
                    if d < 5:
                        pscores = font2.render(str(d + 1) + "). " + sAn[i][0] + "   " + sAn[i][1], True, white, None)
                        display.blit(pscores, (100, 130 + (d * 30)))
                        d = d + 1
                    if i > 4:
                        pscores = font2.render(str(u + 1) + "). " + sAn[i][0] + "   " + sAn[i][1], True, white, None)
                        display.blit(pscores, (372, 160 + (((i - 1) - d) * 30)))
                        u = u + 1
            if len(sAn) >= 10:
                for i in range(10):
                    if d < 5:
                        pscores = font2.render(str(d + 1) + "). " + sAn[i][0] + "   " + sAn[i][1], True, white, None)
                        display.blit(pscores, (100, 130 + (d * 30)))
                        d = d + 1
                    if i > 4:
                        pscores = font2.render(str(u + 1) + "). " + sAn[i][0] + "   " + sAn[i][1], True, white, None)
                        display.blit(pscores, (372, 160 + (((i - 1) - d) * 30)))
                        u = u + 1


            d = 0
            u = 5
            displayhighscores = False

            # displays back button
            # and checks for mouse collision and click in the
            # button method

            button3 = Button(24, 278, (0, 0, 0), "back", 30, 90, 1)
            button3.mousehover(pygame.mouse.get_pos())
            button3.draw()
            if button3.mousehover(pygame.mouse.get_pos()) == True:
                home = True
                highscores = False
                sAn.clear()

        if death == True:
            play = False
            writehighscore =True
            display.blit(imp, (0, 0))

            scroll = scroll - 0.1
            scroll1 = scroll1 - 0.1
            img1(imp1, scroll, scroll1)
            if (scroll <= -(display.get_width())):
                scroll = 0

            if (scroll1 <= 0):
                scroll1 = display.get_width()
            scroll3 = scroll3 - 1
            scroll4 = scroll4 - 1

            img1(imp2, scroll3, scroll4)
            if (scroll3 <= -(display.get_width())):
                scroll3 = 0

            if (scroll4 <= 0):
                scroll4 = display.get_width()
            scroll5 = scroll5 - 1.5
            scroll6 = scroll6 - 1.5

            img1(imp3, scroll5, scroll6)
            if (scroll5 <= -(display.get_width())):
                scroll5 = 0

            if (scroll6 <= 0):
                scroll6 = display.get_width()

            if overlaytransparency < 254:
                greyoverlay.set_alpha(overlaytransparency)
                overlaytransparency += 1

            display.blit(greyoverlay, (0, 0))

            font1 = pygame.font.Font('freesansbold.ttf', 50)
            font2 = pygame.font.Font('freesansbold.ttf', 12)
            text2 = font1.render("You have died...", True, white, None)
            display.blit(text2, [(halfLength - (text2.get_width() / 2)), 50])

            button5 = Button(100, 180, (0, 0, 0), "play again", 30, 90, 1)

            button6 = Button(372, 180, (0, 0, 0), "home", 30, 90, 1)

            button5.mousehover(pygame.mouse.get_pos())
            button5.draw()
            if button5.mousehover(pygame.mouse.get_pos()):
                play = True
                spaceship_clicked = False
                player.resetplayer()
                enemys.empty()
                powerupss.empty()
                playerbullets.empty()
                score = 0
                enemybullett.empty()
                death = False

            button6.mousehover(pygame.mouse.get_pos())
            button6.draw()
            if button6.mousehover(pygame.mouse.get_pos()):
                player.resetplayer()
                enemys.empty()
                powerupss.empty()
                playerbullets.empty()
                score = 0
                enemybullett.empty()
                death = False
                home = True

        # checks if player health is 0 or less
        # then ends the game and displays the endscreen
        if player.health <= 0 and writehighscore:
            play = False
            file = open("currentplayer.txt", "r")
            playername = file.read()
            file.close()
            file = open("scores.txt", "a")
            file.write(playername+ ";" +str(score))
            file.write("\n")
            file.close()
            
            writehighscore = False
            spaceship_clicked = False
            player.resetplayer()
            death = True

        # this loop here checks all the player bullets
        # if they collide with any enemy and the lower its health
        # also remove the player bullet that collided
        for enemy in enemys:
            for b in playerbullets:
                if b.image.get_rect(center=(b.ix, b.iy)).colliderect(
                        enemy.turnedimage.get_rect(center=(enemy.ix, enemy.iy))):
                    enemy.health -= 1
                    playerbullets.remove(b)

        # this loop here checks all the enemy bullets
        # if they collide with the player and the lower its health
        # also remove the enemy bullet that collided
        for bullet in enemybullett:
            if player.image.get_rect(center=player.center1).colliderect(
                    bullet.turnedimage.get_rect(center=bullet.center1)):
                player.health -= 2
                enemybullett.remove(bullet)

        # this loop here checks all the enemies if
        # their health goes to zero and make the enemy "dead" in its class
        # also play bomb sound and adds score to the player
        for enemy in enemys:
            if enemy.health <= 0:
                if enemy.isboss:
                    enemy.score= enemy.score*1.5
                if player.multiplier:
                    score += enemy.score * 1.5
                else:
                    score += enemy.score
                if enemy.score != 0:
                    sound = pygame.mixer.Sound("music and fx/hq-explosion-6288 (1).mp3")
                    sound.set_volume(0.3)
                    sound.play()

                enemy.score = 0


        # some code here is in its on if loop as these are things that are initial at the "start of the game"
        # which is when the spaceship is clicked but the rest code that maybe similar does not need to depend on
        # spaceship clicked as they are derived from the player or the initial 5 enemies
        if play == True:
            home = False
            display.blit(imp, (0, 0))

            scroll = scroll - 0.1
            scroll1 = scroll1 - 0.1
            img1(imp1, scroll, scroll1)
            if (scroll <= -(display.get_width())):
                scroll = 0

            if (scroll1 <= 0):
                scroll1 = display.get_width()
            scroll3 = scroll3 - 1
            scroll4 = scroll4 - 1

            img1(imp2, scroll3, scroll4)
            if (scroll3 <= -(display.get_width())):
                scroll3 = 0

            if (scroll4 <= 0):
                scroll4 = display.get_width()
            scroll5 = scroll5 - 1.5
            scroll6 = scroll6 - 1.5

            img1(imp3, scroll5, scroll6)
            if (scroll5 <= -(display.get_width())):
                scroll5 = 0

            if (scroll6 <= 0):
                scroll6 = display.get_width()

            # this loop runs when the image of the ship
            # that is displayed, when the play button is clicked,
            # has not yet been clicked
            if spaceship_clicked == False:
                font = pygame.font.Font('freesansbold.ttf', 32)
                text2 = font.render("click the shippppp", True, white, None)
                greyoverlay.set_alpha(255)
                display.blit(greyoverlay, (0, 0))
                display.blit(text2, [(halfLength - (text2.get_width() / 2)), 50])
                button3 = Button(24, 278, (0, 0, 0), "back", 30, 90, 1)
                button3.mousehover(pygame.mouse.get_pos())
                button3.draw()
                if button3.mousehover(pygame.mouse.get_pos()) == True:
                    play = False
                    home = True

            # this loop starts when the image of the ship
            # that is displayed, when the play button is clicked,
            # has been clicked
            if spaceship_clicked == True:
                if overlaytransparency > 1:
                    greyoverlay.set_alpha(overlaytransparency)
                    display.blit(greyoverlay, (0, 0))
                    overlaytransparency -= 1

                font = pygame.font.Font('freesansbold.ttf', 32)
                if player.multiplier:
                    text = font.render("score: " + str(score), True, (218, 165, 32), None)
                else:
                    text = font.render("score: " + str(score), True, white, None)
                text1 = font.render("health: " + str(player.health), True, white, None)

                # for each enemy check if it will drop a powerup
                # then drop a random one with a higher chance for heath than the rest
                # then run the enemy move and show method
                for e in enemys:
                    if e.droppowerup == True:
                        if e.dead:
                            if e.spawnedpowerup == False:
                                choice = random.choice(
                                    [multiplier, doublelazers, lazerspeedup, multiplier, doublelazers, lazerspeedup,
                                     healthpickup, healthpickup, healthpickup])
                                powerupss.add(powerups(e, choice[0], choice[1]))
                                e.spawnedpowerup = True
                    e.upd()
                    e.show()

                for powerup in powerupss:
                    powerup.drawpowerup()
                    if player.image.get_rect(center=player.center1).colliderect(
                            powerup.image.get_rect(center=(powerup.ix, powerup.iy))):
                        player.pickuppowerup(powerup.typeof)
                        powerup.kill()
                    powerup.movepowerup()

                # display all the hud elements

                display.blit(text, [10, 5])
                display.blit(text1, [235, 282])
                display.blit(doublelazers1, pygame.Rect(10, 269, 45, 45))
                display.blit(multiplier1, pygame.Rect(65, 269, 45, 45))
                display.blit(lazerspeedup1, pygame.Rect(120, 269, 45, 45))
                display.blit(healthpickup1, pygame.Rect(175, 269, 45, 45))
                display.blit(player1, (pygame.mouse.get_pos()[0] - 20, pygame.mouse.get_pos()[1] - 12))
                player.moveplayer()
                player.drawplayer()

                # check if the enemy respawn timer has gone off and there
                # are less than 5 enemies already on the screen

                if enemycooldown == False:
                    if score < 2000:
                        if len(enemys) < 5:
                            for i in range(random.randint(1, 3)):
                                enemys.add(
                                    Enemy(571, random.randint(50, 274), enemypicture, destroyedenemy, 3, time.time_ns(),
                                          1,
                                          False))
                            if score - boss > 300:
                                boss = boss + 300
                                enemys.add(
                                    Enemy(571, random.randint(50, 274), bossenemy, destroyedbossenemy, 12,
                                          time.time_ns(),
                                          1,
                                          True))
                    else:
                        if len(enemys) < 7:
                            for i in range(random.randint(1, 3)):
                                enemys.add(
                                    Enemy(571, random.randint(50, 274), enemypicture, destroyedenemy, 3, time.time_ns(),
                                          1,
                                          False))
                            if score - boss > 500:
                                boss = boss + 500
                                enemys.add(
                                    Enemy(571, random.randint(50, 274), bossenemy, destroyedbossenemy, 12,
                                          time.time_ns(),
                                          1,
                                          True))

                    # this loop checks the enemy bullet cooldown
                    # and resets it when the loop is over

                    for e in enemys:
                        if time.time_ns() / 1000000 - e.timer > random.randint(250, 350):
                            if not e.isboss:
                                enemybullett.add(enemybullets(e, enemybullet, bossbullet, 0))
                            else:
                                for i in range(4):
                                    enemybullett.add(enemybullets(e, enemybullet, bossbullet, i + 1))

                            pygame.mixer.Sound.play(
                                pygame.mixer.Sound("music and fx/blaster-2-81267 (mp3cut.net) (1).mp3"), 0, 0, 0)
                            e.timer = time.time_ns() / 1000000

                    pygame.time.set_timer(26, 800)
                    enemycooldown = True

                # checks if the mouse has been clicked and if yes then
                # reset the shot cooldown and create another
                # instance of player bullets
                if pygame.mouse.get_pressed()[0]:

                    if shot == False:
                        #checks whther the players double lazer powerup is active and if yes add two different bulltets
                        # with different y values else one bullet will fire from the center of the ship
                        if player.doublelazers:
                            playerbullets.add(playerbullet(player.center1[0], (player.center1[1] + 10), playerbull1))
                            playerbullets.add(playerbullet(player.center1[0], (player.center1[1] - 10), playerbull1))
                        else:
                            playerbullets.add(playerbullet((player.center1[0]), player.center1[1], playerbull1))
                        pygame.mixer.Sound.play(pygame.mixer.Sound("music and fx/shoot02wav-14562 (mp3cut.net).mp3"), 0,
                                                0, 0)
                        # then sets another timer for the shot cooldown with a variable called firerate
                        # as the duration so that when the increase firespeed is picked up the firerate
                        # value can go down
                        pygame.time.set_timer(25, firerate)
                        shot = True
                        # break

            # this piece of code just places an image of the ship that the player has to click
            # to start the actual game
            else:
                display.blit(player1, (10, halfHeight - 12))
                # break

            # two for loops here are for updating and displaying the
            # players bullets and the enemy bullets
            for b in playerbullets:
                b.movebullet()
                b.drawbullet()
            for b in enemybullett:
                b.movebullet()
                b.drawbullet()

        pygame.display.update()
        clock.tick(fps)


main()
