import pygame
import utils

class Player:

    def __init__(self, size, color, pos):
        self.SIZE = size
        self.COLOR = color
        self.pos = pos
        self.vel = [0,0]

    # getter method
    def get_velocity(self):
        return self.vel

    def draw(self, screen):
        pygame.draw.circle(screen, self.COLOR, self.pos , self.SIZE)


    def move(self, dt, keys):

        acceleration = 25
        resistance = 0.05
        max_spd = 3

        #velocity dampening
        self.vel[0] += self.vel[0] * -resistance
        self.vel[1] += self.vel[1] * -resistance


        # changing velocity on input
        if keys[pygame.K_w]:
            self.vel[1] -= acceleration * dt
        if keys[pygame.K_s]:
            self.vel[1] += acceleration * dt
        if keys[pygame.K_a]:
            self.vel[0] -= acceleration * dt
        if keys[pygame.K_d]:
            self.vel[0] += acceleration * dt

        #setting boundary of velocity
        self.vel[0] = utils.clamp_f(self.vel[0], -max_spd, max_spd)
        self.vel[1] = utils.clamp_f(self.vel[1], -max_spd, max_spd)

        # converting velocity to pixel movement
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])



