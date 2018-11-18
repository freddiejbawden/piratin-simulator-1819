import math
import pygame as pg
from pygame.math import Vector2


pg.init()
screen = pg.display.set_mode((640, 480))
FONT = pg.font.Font(None, 24)
BLACK = pg.Color('black')
BULLET_IMAGE = pg.Surface((20, 11), pg.SRCALPHA)
pg.draw.polygon(BULLET_IMAGE, pg.Color('grey11'), [(0, 0), (20, 5), (0, 11)])


class Bullet(pg.sprite.Sprite):

    def __init__(self, pos, angle):
        super(Bullet, self).__init__()
        self.image = pg.transform.rotate(BULLET_IMAGE, -angle)
        self.rect = self.image.get_rect(center=pos)
        # To apply an offset to the start position,
        # create another vector and rotate it as well.
        offset = Vector2(40, 0).rotate(angle)
        # Add the offset vector to the position vector.
        self.pos = Vector2(pos) + offset  # Center of the sprite.
        # Rotate the velocity vector (9, 0) by the angle.
        self.velocity = Vector2(9, 0).rotate(angle)

    def update(self):
        # Add velocity to pos to move the sprite.
        self.pos += self.velocity
        self.rect.center = self.pos


def main():
    clock = pg.time.Clock()
    # The cannon image and rect.
    cannon_img = pg.Surface((60, 22), pg.SRCALPHA)
    pg.draw.rect(cannon_img, pg.Color('grey19'), [0, 0, 35, 22])
    pg.draw.rect(cannon_img, pg.Color('grey19'), [35, 6, 35, 10])
    orig_cannon_img = cannon_img  # Store orig image to preserve quality.
    cannon = cannon_img.get_rect(center=(320, 240))
    angle = 0
    # Add bullets to this group.
    bullet_group = pg.sprite.Group()

    playing = True
    while playing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                playing = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                # Left button fires a bullet from cannon center with
                # current angle. Add the bullet to the bullet_group.
                if event.button == 1:
                    bullet_group.add(Bullet(cannon.center, angle))

        bullet_group.update()
        # Find angle to target (mouse pos).
        x, y = Vector2(pg.mouse.get_pos()) - cannon.center
        angle = math.degrees(math.atan2(y, x))
        # Rotate the cannon image.
        cannon_img = pg.transform.rotate(orig_cannon_img, -angle)
        cannon = cannon_img.get_rect(center=cannon.center)

        # Draw
        screen.fill(pg.Color('darkseagreen4'))
        bullet_group.draw(screen)
        screen.blit(cannon_img, cannon)
        txt = FONT.render('angle {:.1f}'.format(angle), True, BLACK)
        screen.blit(txt, (10, 10))
        pg.draw.line(
            screen, pg.Color(150, 60, 20),
            cannon.center, pg.mouse.get_pos(), 2)
        pg.display.update()

        clock.tick(30)

if __name__ == '__main__':
    main()
    pg.quit()
