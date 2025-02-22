from circleshape import *
from constants import *
import pygame

class Player (CircleShape):
    def __init__(self,x,y):
        self.x = int(SCREEN_WIDTH/2)
        self.y = int(SCREEN_HEIGHT/2)
        super.__init__()
        self.radius = PLAYER_RADIUS
        self.rotation = 0
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(screen,"white",points=self.triangle(),width=2)
