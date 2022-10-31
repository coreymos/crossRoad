import pyray as rl

from game.scripting.action import Action
from constants import *

class CollideEndAreaAction(Action):
    def __init__(self):
        self._frame_time = 0
        self._add_points = True

    def execute (self, cast, script, callback):
        frog = cast.get_first_actor(FROG_GROUP)
        frog_height = frog.get_position().get_y()
        stats = cast.get_first_actor(STATS_GROUP)

        if frog_height <= START_HEIGHT_ROAD * (CELL_SIZE): 
            if self._frame_time <= 1 and self._add_points:
                self._frame_time += rl.get_frame_time()
                self._add_points = False
            else:
                stats.add_points(1)
                position = FROG_START
                position.scale(30)
                frog.set_position(position)
                self._add_points = True