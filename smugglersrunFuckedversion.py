import math
import pygame
import random
import os
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


## assets folder


# class Player(pygame.sprite.Sprite):
#
#     def __init__(self):
#         """ Set up the player on creation. """
#         # Call the parent class (Sprite) constructor
#         super().__init__()
#
#         self.image = pygame.Surface([20, 20])
#         self.image.fill(RED)
#
#         self.rect = self.image.get_rect()
#
#
#

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.position = Vector2(0,0)
        self.anchored = False

        self.velocity = Vector2(0.0, 0.0)
        self.angle = 0.0
        self.length = 20
        self.max_acceleration = 8
        self.max_steering = 10
        self.max_velocity = 75
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









######## initialize pygame and create window ##########
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smugglers Run")
clock = pygame.time.Clock()     ## For syncing the FPS
#######################################################



############# Sprites #############
all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
###################################


# Create a red player block
player = Player()


######### MAIN GAME LOOP #########
done = False
ppu = 32
while not done:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "player_boat.png")
    player_image = pygame.image.load(image_path)
    player_image = pygame.transform.scale(player_image, (100, 100))


    ppu = 32
    dt = clock.get_time() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # User input
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if player.velocity.y< 0:
            print("{}." .format(player.velocity))
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
            player.acceleration = -player.velocity.y / dt
    else:
        if abs(player.velocity.y) > dt * player.free_deceleration:
            player.acceleration = copysign(player.free_deceleration, player.velocity.y)
        else:
            if dt != 0:
                player.acceleration = -player.velocity.y / dt
    player.acceleration = max(-player.max_acceleration, min(player.acceleration, player.max_acceleration))

    if pressed[pygame.K_RIGHT]:
        player.steering -= 12 * dt
    elif pressed[pygame.K_LEFT]:
        player.steering += 12 * dt
    else:
        player.steering = 0
    player.steering = max(-player.max_steering, min(player.steering, player.max_steering))

    # Logic
    player.update(dt)

    # Drawing
    screen.fill(WHITE)
    rotated = pygame.transform.rotate(player_image, player.angle)
    rect = rotated.get_rect(center=player.position)
    screen.blit(rotated, player.position * ppu - (rect.width / 2, rect.height / 2))
    pygame.display.flip()

    clock.tick(60)
pygame.quit()



        # if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LEFT:
        #             player.turnLeft()
        #         if event.key == pygame.K_RIGHT:
        #             player.turnRight()
        #         if event.key == pygame.K_UP:
        #             player.speedUp()
        #         if event.key == pygame.K_SPACE:
        #             player.anchor()


#     player.wrap_around_screen()
#     all_sprites.update()
#
#
#     # --- Draw a frame --- #
#
#     # Clear the screen
#     screen.fill(WHITE)
#
#     # Draw all the spites
#     all_sprites.draw(screen)
#
#     # Go ahead and update the screen with what we've drawn.
#     pygame.display.flip()
#
#     pygame.display.set_caption('angle {:.1f} accel {} accel angle {:.1f}, velocity {}'.format(
#         player.angle, player.acceleration, player.acceleration.as_polar()[1], player.vel))
#     pygame.display.update()
#     # --- Limit to 20 frames per second
#     clock.tick(60)
#
# pygame.quit()









################# MEGA COMMENT SHIT THAT WILL BE USEFUL SOON ###################

# class Bullet(pygame.sprite.Sprite):
#     """ This class represents the bullet . """
#     def __init__(self):
#         # Call the parent class (Sprite) constructor
#         super().__init__()
#
#         self.image = pygame.Surface([4, 10])
#         self.image.fill(BLACK)
#
#         self.rect = self.image.get_rect()
#
#     def update(self):
#         """ Move the bullet. """
#         self.rect.y -= 3

# class Block(pygame.sprite.Sprite):
#     """ This class represents the block. """
#     def __init__(self, color):
#         # Call the parent class (Sprite) constructor
#         super().__init__()
#
#         self.image = pygame.Surface([20, 15])
#         self.image.fill(color)
#
#         self.rect = self.image.get_rect()

# for bullet in bullets:
#
#     block_hit_list = pygame.sprite.spritecollide(bullet, blocks, True)
#
#     for block in block_hit_list:
#         bullets.remove(bullet)
#         all_sprites.remove(bullet)
#
#     # Remove bullets off screen
#     if bullet.rect.y < -10:
#         bullets.remove(bullet)
#         all_sprites.remove(bullet)

        #
        #
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT and player.change_x < 0:
        #         player.stop()
        #     if event.key == pygame.K_RIGHT and player.change_x > 0:
        #         player.stop()
        #     if event.key == pygame.K_DOWN and player.change_y > 0:
        #         player.stop()
        #     if event.key == pygame.K_UP and player.change_y < 0:
        #         player.stop()
