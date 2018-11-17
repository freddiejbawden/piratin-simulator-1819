import math
import pygame
import random
from os import path

vec = pygame.math.Vector2

vel = vec(0, 0)
acceleration = vec(0, -0.2)  # The acceleration vec points upwards.
print(vel.length())
