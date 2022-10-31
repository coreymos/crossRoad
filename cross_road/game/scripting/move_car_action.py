from constants import *
from game.scripting.action import Action

class MoveCarAction(Action):
    def __init__(self):
        pass
    def execute (self, cast, script, callback):
        cars = cast.get_actors(CAR_GROUP)
        for car in cars:
            car.move_next()