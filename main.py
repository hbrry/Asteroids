import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable,drawable,bullets)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)        
        #print(len(bullets))
        for item in asteroids:
            if item.collision(player):
                print("Game over!")
                sys.exit()

            for bullet in bullets:
                if item.collision(bullet):
                    #print("Touched")
                    bullet.kill() 
                    item.split()
        
        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        dt = clock.tick(60)/1000
        pygame.display.flip()




if __name__ == "__main__":
    main()