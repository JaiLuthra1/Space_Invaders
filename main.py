'''
Author: Jai Luthra
'''

import pygame
import random
import time

pygame.init()

width, height = 800, 600
center = (240, 260)
score_loc = (10, 10)
life_loc = (720, 10)
bullet_Speed = 0.4
score = 0
lives = 3
window = pygame.display.set_mode((width, height))

pygame.display.set_caption('Space Invaders')

playerImg = pygame.image.load('spaceship.png')
playerX = (width - 64)/2
playerY = height - 10 - 64
playerX_change = 0

enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, width - 64)
enemyY = 0

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = playerY - 30
bulletX_change = 0
bulletY_change = bullet_Speed
bullet_fired = False

def show_score():
    text = pygame.font.Font('freesansbold.ttf', 16)
    return text.render(f'Score: {score}', True, (255,255,255))

def player(playerX, playerY):
    window.blit(playerImg, (playerX, playerY))

def enemy(enemyX, enemyY):
    window.blit(enemyImg, (enemyX, enemyY))

def bullet(bulletX, bulletY):
    window.blit(bulletImg, (bulletX, bulletY))

# run until a quit
loop = True

while(loop == True):
    window.fill((0,0,0))

    for event in pygame.event.get():
        # if window closed
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change += -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.5

            if event.key == pygame.K_SPACE:
                if not bullet_fired:
                    bulletX = playerX + 16
                    bullet_fired = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    playerX = max(0, playerX)
    playerX = min(width - 64, playerX)
    player(playerX, playerY)

    enemyY += (score//5 + 1) * 0.1
    enemy(enemyX, enemyY)
    
    if bullet_fired:
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        if(bulletY < -16):
            bullet_fired = False
            bulletY = playerY - 30

        if enemyX - 28 < bulletX < enemyX + 56 and enemyY - 56 < bulletY < enemyY + 56:
            bullet_fired = False
            bulletY = playerY - 30
            enemyX = random.randint(0, width - 64)
            enemyY = 0
            score += 1

    if enemyY > height - 50:
        lives-= 1
        if enemyX - 56 < playerX < enemyX + 56:
            lives = 0
        enemyX = random.randint(0, width - 64)
        enemyY = 0

    if lives == 0:
        for i in range(5,0,-1):
            time.sleep(1)
            window.fill((0,0,0))
            text = pygame.font.Font('freesansbold.ttf', 50)
            out = text.render('Game Over!', True, (255,255,0))
            window.blit(out, center)
            out = text.render(f'Window will exit in {i}s', True, (255,255,0))
            window.blit(out, (120,300))
            window.blit(show_score(), score_loc)
            pygame.display.update()
        loop = False

    else:
        text = pygame.font.Font('freesansbold.ttf', 16)
        life = text.render(f'Live(s): {lives}', True, (255,255,255))
        window.blit(life, life_loc)
        window.blit(show_score(), score_loc)
        pygame.display.update()

