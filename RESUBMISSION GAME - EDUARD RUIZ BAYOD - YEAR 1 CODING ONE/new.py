import pygame
import os
import random
import time



pygame.mixer.init()
pygame.init()

HEIGHT = 500
WIDTH = 500
PLAYER1_SPACESHIP = pygame.image.load(os.path.join('Assets', 'player1_spaces.png'))
PLAYER2_SPACESHIP = pygame.image.load(os.path.join('Assets', 'player2_spaces.png'))

SPACESHIP_1 = pygame.transform.rotate(pygame.transform.scale(PLAYER1_SPACESHIP, (50, 50)), -180)
SPACESHIP_2 = pygame.transform.rotate(pygame.transform.scale(PLAYER2_SPACESHIP, (50, 50)), 0)
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'background1.png')), (WIDTH, HEIGHT))

p1_score = 0
p2_score = 0

# Asteroid
aster_img = pygame.image.load(os.path.join('Assets', 'asteroid.png'))
asteroids = pygame.transform.scale(aster_img, (50, 50))
asterX = 250
asterY = 215
asteroidX_vary = 0.3

def asteroid (x, y):
    window.blit(asteroids, (x, y))

P1_HIT = pygame.USEREVENT + 1
P2_HIT = pygame.USEREVENT + 2



HIT_SOUND = pygame.mixer.Sound('Assets/explode.wav')
FIRE_SOUND = pygame.mixer.Sound('Assets/shoot.wav')
WINNER_SOUND = pygame.mixer.Sound('Assets/winner.wav')



window = pygame.display.set_mode((HEIGHT, WIDTH))



run = True


def get_font(size):
    return pygame.font.Font("Assets/font.ttf", size)

def bullets_movement(p1_bullets, p2_bullets, player1, player2, ast):        ##################### BULLETS MOVEMENT FUNCTION USED AND EDITED FROM https://github.com/techwithtim/PygameForBeginners


    for bullet1 in p1_bullets:                                   ###### P1 TO SHOOT BULLETS

        bullet1.y += 5

        if ast.colliderect(bullet1):

            p1_bullets.remove(bullet1)
            

        if player2.colliderect(bullet1):


            pygame.event.post(pygame.event.Event(P2_HIT))
            p1_bullets.remove(bullet1)


        elif bullet1.y > HEIGHT:
            p1_bullets.remove(bullet1)

        for bullet2 in p2_bullets:                               ###### IF BULLETS COLLIDE, REMOVE THEM
            if bullet2.colliderect(bullet1):
                p1_bullets.remove(bullet1)
                p2_bullets.remove(bullet2)  


    for bullet2 in p2_bullets:                                   ###### IF BULLETS ARE CREATED, 1ST DECREASE X TO MOVE THEM

        bullet2.y -= 5

        if player1.colliderect(bullet2):                         ###### IF BULLEIT RECTANGLE COLLIDE WITH SPACESHIP RECTANGE         
            p2_bullets.remove(bullet2)                           ###### BULLETS TO BE REMOVED FROM LIST    
            pygame.event.post(pygame.event.Event(P1_HIT))         

    
        if ast.colliderect(bullet2):                         ###### IF BULLEIT RECTANGLE COLLIDE WITH SPACESHIP RECTANGE         
            p2_bullets.remove(bullet2)                           ###### BULLETS TO BE REMOVED FROM LIST    



        elif bullet2.y < 0:
            p2_bullets.remove(bullet2)

        for bullet1 in p1_bullets:
            if bullet2.colliderect(bullet1):
                p2_bullets.remove(bullet2)
                p1_bullets.remove(bullet1)
 


def draw(p1, p2, bullets_1, bullets_2, p1_health, p2_health, asterX):
    
    window.blit(BACKGROUND, (0 ,0))
    window.blit(SPACESHIP_1, (p1.x, p1.y))
    window.blit(SPACESHIP_2, (p2.x, p2.y))
    asteroid(asterX, asterY)

    if p1_health <= 5:                                                                      ################### DISPLAY BOTH PLAYERS HEALTH WITH A RECTANGLE THAT DECREASED SIZE AND CHANGE COLOR DEPENDING ON HEALTH 
        pygame.draw.rect(window, (255, 0, 0), pygame.Rect(10, 10, 20, p1_health * 22))    
    else:
        pygame.draw.rect(window, (0, 255, 0), pygame.Rect(10, 10, 20, p1_health * 22))

    if p2_health <= 5:
        pygame.draw.rect(window, (255, 0, 0), pygame.Rect(10, 255, 20, p2_health * 22))
    else:
        pygame.draw.rect(window, (0, 255, 0), pygame.Rect(10, 255, 20, p2_health * 22))

    for bullet in bullets_1:
       pygame.draw.rect(window, (255,0,0), bullet)
    
    for bullet in bullets_2:
        pygame.draw.rect(window, (255, 255, 0), bullet)

    pygame.display.update()

def draw_winner(text):                                                                  ########### Draw name of the winner in screen and wait to reset the game
    draw_text = get_font(10).render(text, 1, (255,255,255))
    window.blit(draw_text, (WIDTH//2 - draw_text.get_width() / 2, HEIGHT//2 - draw_text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(5000)





def game():

    asterX = 250
    p1 = pygame.Rect((WIDTH/2), 0, 50, 50)
    p2 = pygame.Rect((WIDTH/2), HEIGHT - 50, 50, 50)
    ast = pygame.Rect(asterX, asterY, 50, 50)
    p1_health = 10
    p2_health = 10
    p1_score = 0
    p2_score = 0
    asterX = 250
    asteroidX_vary = 1

    play = True

    bullets1 = []
    bullets2 = []

    clock = pygame.time.Clock()

    while play:

        clock.tick(120)

        for event in pygame.event.get():   

            if event.type == pygame.QUIT :           ####### IF USER CLOSES WINDOWS, QUIT GAME
                play = False
                pygame.quit()


            if event.type == pygame.KEYDOWN:                                            ######### CHECK FOR KEYBOARD INPUTS AND UPDATE PLAYER1 & 2 X


                if event.key == pygame.K_LEFT and p1.x > 50:
                        p1.x = p1.x - 15
                        
                if event.key == pygame.K_RIGHT and p1.x < WIDTH - 65:
                        p1.x = p1.x + 15
                        
                if event.key == pygame.K_d and p2.x < WIDTH - 65:
                        p2.x = p2.x + 15
                        
                if event.key == pygame.K_a and p2.x > 50:
                        p2.x = p2.x - 15

                if event.key == pygame.K_RALT:
                    if (len(bullets1) < 3):
                        bullet = pygame.Rect(p1.x + 20, p1.y + 30, 5, 10)       ###### BULLETS TO BE CREATED FROM THE CENTER OF THE SPACESHIP
                        bullets1.append(bullet)
                        FIRE_SOUND.play() 

                if event.key == pygame.K_LALT:
                    if (len(bullets2) < 3):
                        bullet = pygame.Rect(p2.x + 20, p2.y - 20 + 10, 5, 10)       ###### BULLETS TO BE CREATED FROM THE CENTER OF THE SPACESHIP
                        bullets2.append(bullet)
                        FIRE_SOUND.play() 

            if event.type == P1_HIT:
                p1_health -= 1
                HIT_SOUND.play()
            
            if event.type == P2_HIT:
                p2_health -= 1
                HIT_SOUND.play()

        win_message = ""

        if p1_health < 0:
            win_message = "Player 2 Wins!"
            p1_score += 1

        if p2_health < 0:
            win_message = "Player 1 Wins!"
            p2_score += 1

        if win_message != "":                               #### WHEN HEALTH OF ANY PLAYERS DROPS BELOW 0, WINNER MESSAGE GETS UPDATED AND DISPLAYED ON SCREEN,
            WINNER_SOUND.play()
            draw_winner(win_message)

            break

        asterX += asteroidX_vary        ########## ASTEROID TO BE MOVED FROM RIGHT TO LEFT OF SCREEN
        ast.x += asteroidX_vary

        if asterX <= 50:
            asteroidX_vary = 1
        elif asterX >= 450:
            asteroidX_vary = -1


        bullets_movement(bullets1, bullets2, p1, p2, ast)

        draw(p1, p2, bullets1, bullets2, p1_health, p2_health, asterX)

        
    game()

        

game()