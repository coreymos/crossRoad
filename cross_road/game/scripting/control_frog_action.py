from constants import *
from game.scripting.action import Action
from game.shared.point import Point

class ControlFrogAction(Action):
    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service

    def execute (self, cast, script, callback):

        frog = cast.get_first_actor(FROG_GROUP)
        velocity = self._keyboard_service.get_direction()
        frog.set_velocity(velocity)