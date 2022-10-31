from constants import *
from game.scripting.action import Action
from game.shared.point import Point

class MoveFrogAction(Action):
    def __init__(self):
        pass

    def execute (self, cast, script, callback):

        frog = cast.get_first_actor(FROG_GROUP)
        velocity = frog.get_velocity()
        position = frog.get_position()

        x = (position.get_x() + (FROG_JUMP_DISTANCE * velocity.get_x()))
        y = (position.get_y() + (FROG_JUMP_DISTANCE * velocity.get_y()))
        
        # This code prevents the frog from moving out of the screen boundaries. 
        if x >= MAX_X - 15:
            x = MAX_X - 15
        elif x <= 0:
            x = 0
        if y >= MAX_Y - 30:
            y = MAX_Y - 30
        elif y <= 0:
            y = 0

        new_position = Point(x, y)

        # if the jump cooldown timer is not in effect, the frog is allowed to jump (move).
        if frog.jump_cooldown():
            frog.set_position(new_position)
        
