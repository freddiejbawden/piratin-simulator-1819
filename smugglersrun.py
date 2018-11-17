import math
import pygame
import random
from os import path


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
img_dir = path.join(path.dirname(__file__), 'sprites')


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
        self.imageMaster = pygame.image.load(path.join(img_dir, 'player_boat.png'))
        self.imageMaster = self.imageMaster.convert()
        self.image = pygame.transform.scale(self.imageMaster, (75, 75))
        self.original_image = self.image

        self.position = vec(WIDTH / 2, HEIGHT / 2)
        self.rect = self.image.get_rect(center=self.position)
        
        self.anchored = False

        self.velocity = Vector2(0.0, 0.0)
        self.angle = 0.0
        self.length = 4
        self.max_acceleration = 3
        self.max_steering = 6
        self.max_velocity = 20
        self.brake_deceleration = 10
        self.free_deceleration = 2



    def update(self):
        if(not self.anchored ):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                #if(self.vel.length()>0.0):
                    #self.vel -= self.acceleration
                self.angle_speed = -1
                player.rotate()
            if keys[pygame.K_RIGHT]:
                #if(self.vel.length()>0.0):
                    #self.vel -= self.acceleration
                self.angle_speed = 1
                player.rotate()
            # If up or down is pressed, accelerate the ship by
            # adding the acceleration to the velocity vector.
            if keys[pygame.K_UP]:
                self.vel += self.acceleration
            if keys[pygame.K_DOWN]:
                if(self.vel[1]<0):
                    self.vel -= self.acceleration

            # max speed
            if self.vel.length() > MAX_SPEED:
                self.vel.scale_to_length(MAX_SPEED)

            self.position += self.vel
            self.rect.center = self.position
    def anchor(self):
        self.anchored = True
        self.change_y = 0



    def rotate(self):
        # Rotate the acceleration vector.
        self.acceleration.rotate_ip(self.angle_speed)
        self.angle += self.angle_speed
        if self.angle > 360:
            self.angle -= 360
        elif self.angle < 0:
            self.angle += 360
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

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
all_sprites.add(player)


######### MAIN GAME LOOP #########
done = False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_LEFT:
        #             player.turnLeft()
        #         if event.key == pygame.K_RIGHT:
        #             player.turnRight()
        #         if event.key == pygame.K_UP:
        #             player.speedUp()
        #         if event.key == pygame.K_SPACE:
        #             player.anchor()


    player.wrap_around_screen()
    all_sprites.update()


    # --- Draw a frame --- #

    # Clear the screen
    screen.fill(WHITE)

    # Draw all the spites
    all_sprites.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    pygame.display.set_caption('angle {:.1f} accel {} accel angle {:.1f}, velocity {}'.format(
        player.angle, player.acceleration, player.acceleration.as_polar()[1], player.vel))
    pygame.display.update()
    # --- Limit to 20 frames per second
    clock.tick(60)

pygame.quit()









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
