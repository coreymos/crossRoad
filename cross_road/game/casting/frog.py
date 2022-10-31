import random
import pyray as rl

from constants import *
from game.shared.color import Color
from game.shared.point import Point
from game.casting.actor import Actor


class Frog(Actor):
    """a tailless amphibian with a short squat body, moist smooth skin, and very long hind legs for leaping.
    """
    def __init__(self):
        super().__init__()
        self._cooldown = False
        self._frame_time = 0
        
    def _detected_movement(self):
        if self._velocity.get_x() < 0 or self._velocity.get_x() > 0:
            return True
        elif self._velocity.get_y() < 0 or self._velocity.get_y() > 0:
            return True
        else:
            return False
    
    def jump_cooldown(self):
        if self._frame_time <= FROG_SPEED:
            self._frame_time += rl.get_frame_time()
            self._cooldown = False
        else:
            if self._detected_movement():
                self._cooldown = True
                self._frame_time = 0
        return self._cooldown