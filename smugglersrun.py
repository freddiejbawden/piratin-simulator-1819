import math
import pygame
import random
import os
import numpy as np
from pygame.math import Vector2
from math import tan, radians, degrees, copysign



####### COLOURS ########
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,  0,  255)
########################



####### CONSTANTS ######
WIDTH = 800
HEIGHT = 600
MAX_SPEED = 5
########################


############# Sprites #############
all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()
cannon_list = pygame.sprite.Group()
###################################

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)

        self.position = Vector2(200,200)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = 90.0
        self.acceleration = 1.2
    def update(self):
        """ Move the bullet. """
        self.velocity -= (self.acceleration * 0.2, 0.0)
        self.velocity.x = 1.2

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), "player_boat.png"))
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.anchored = False
        self.position = Vector2(200,200)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = 0.0
        self.length = 16
        self.max_acceleration = 5
        self.max_steering = 15
        self.max_velocity = 50
        self.brake_deceleration = 10
        self.free_deceleration = 2



        self.acceleration = 0.0
        self.steering = 0.0

    def update(self, dt):
        self.velocity -= (0,self.acceleration * 0.2)
        self.velocity.y = max(-self.max_velocity, min(self.velocity.y, self.max_velocity))

        if self.steering:
            turning_radius = self.length / tan(radians(self.steering))
            angular_velocity = self.velocity.y / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle) * dt
        self.angle += degrees(angular_velocity) * dt

    def anchor(self):
        self.anchored = True

    def wrap_around_screen(self):
        """Wrap around screen."""
        if self.position.x > WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = WIDTH
        if self.position.y <= 0:
            self.position.y = HEIGHT
        if self.position.y > HEIGHT:
            self.position.y = 0


class Game:
    def __init__(self):

        pygame.init()
        pygame.mixer.init()  ## For sound
        pygame.display.set_caption("Smugglers Run")
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.ticks = 60
        self.finished = False

    def run(self):


        player = Player()
        all_sprites.add(player)
        ppu = 2

        while not self.finished:
            dt = self.clock.get_time() / 1000

            # Event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True

            # User input
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_UP]:
                if player.velocity.y < 0:
                    player.acceleration = player.brake_deceleration
                else:
                    player.acceleration += 1 * dt
            elif pressed[pygame.K_DOWN]:
                if player.velocity.y > 0:
                    player.acceleration = -player.brake_deceleration
                else:
                    player.acceleration -= 1 * dt
            elif pressed[pygame.K_SPACE]:
                if abs(player.velocity.y) > dt * player.brake_deceleration:
                    player.acceleration = copysign(player.brake_deceleration, player.velocity.y)
                else:
                    player.acceleration = -player.velocity.x / dt
            else:
                if abs(player.velocity.y) > dt * player.free_deceleration:
                    player.acceleration = copysign(player.free_deceleration, player.velocity.y)
                else:
                    if dt != 0:
                        player.acceleration = -player.velocity.y / dt
            player.acceleration = max(-player.max_acceleration, min(player.acceleration, player.max_acceleration))

            if pressed[pygame.K_RIGHT]:
                player.steering += 10 * dt
            elif pressed[pygame.K_LEFT]:
                player.steering -= 10 * dt
            else:
                player.steering = 0
            player.steering = max(-player.max_steering, min(player.steering, player.max_steering))

            if pressed[pygame.K_f]:
                # Fire a bullet if the user clicks the mouse button
                bullet = Bullet()
                # Set the bullet so it is where the player is

                # Add the bullet to the lists
                all_sprites.add(bullet)
                cannon_list.add(bullet)
                rotated_bullet = pygame.transform.rotate(bullet.image, bullet.angle)
                rect_bullet = rotated_bullet.get_rect(center=bullet.position)
                self.screen.blit(rotated_bullet, bullet.position * ppu - (rect.width / 2, rect.height / 2))



            # Game Logic
            player.update(dt)
            cannon_list.update()
            #print(cannon_list)
            #print("Player Position: {}, Player Velocity: {}, Player acceleration: {}, Player center: {}, Player angle: {}." .format(player.position, player.velocity, player.acceleration, player.rect, player.angle,))

            # Drawing
            self.screen.fill(WHITE)
            rotated = pygame.transform.rotate(player.image, player.angle)


            rect = rotated.get_rect(center=player.position)
            print(pygame.mouse.get_pos())


            self.screen.blit(rotated, player.position * ppu - (rect.width / 2, rect.height / 2))

            pygame.display.flip()
            self.clock.tick(self.ticks)
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
