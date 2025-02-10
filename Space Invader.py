import math
import random
import pygame

#Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

#Initialize Pygame
pygame.init()

#Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#BACKGROUND
Background = pygame.image.load('Background.png')

#Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('UFO.png')
pygame.display.set_icon(icon)

#Player
PlayerImg = pygame.image.load('Player.png')
PlayerX = PLAYER_START_X
PlayerY = PLAYER_START_Y
PlayerX_change = 0

#Enemy
EnemyImg = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    EnemyImg.append(pygame.image.load('Enemy.png'))
    EnemyX.append(random.randint(0,SCREEN_WIDTH - 64)) #64 is the size of the enemy
    EnemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    EnemyX_change.append(ENEMY_SPEED_X)
    EnemyY_change.append(ENEMY_SPEED_Y)

#Bullet
BulletImg = pygame.image.load('Bullet.png')
BulletX = 0
BulletY = PLAYER_START_Y
BulletX_change = 0
BulletY_change = BULLET_SPEED_Y
Bullet_state = "ready"

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

#Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    #Display the score on the screen
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def game_over_text():
    #Display the game over text
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    #Draw the player on the screen
    screen.blit(PlayerImg, (x, y))

def enemy(x, y, i):
    #Draw the enemy on the screen
    screen.blit(EnemyImg[i], (x, y))

def fire_bullet(x, y):
    #Fire a bullet from the player's position
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(BulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    #Check if the bullet has hit the enemy
    distance = math.sqrt((enemyX - bulletX)**2 + (enemyY - bulletY)**2)
    return distance < COLLISION_DISTANCE