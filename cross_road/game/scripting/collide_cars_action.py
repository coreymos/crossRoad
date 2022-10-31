import random

from game.scripting.action import Action
from constants import *
from game.shared.point import Point

class CollideCarsAction(Action):
    def __init__(self):
        pass

    def execute (self, cast, script, callback):
        cars = cast.get_actors(CAR_GROUP)
        frog = cast.get_first_actor(FROG_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)

        for car in cars:
            car_x = car.get_position().get_x()
            car_y = car.get_position().get_y()
            frog_x = frog.get_position().get_x()
            frog_y = frog.get_position().get_y()
            #This checks if the frog and car are within a certain amount of pixels. (FROG_COLLISION)
            if ((car_x - LEFT_FROG_COLLISION) <= frog_x <= (RIGHT_FROG_COLLISION + car_x)) and (car_y == frog_y): 
                stats.lose_life()
                # Brings frog back to start
                position = FROG_START
                position.scale(30)
                frog.set_position(position)

                # This code is to be used once TRY_AGAIN and GAME_OVER are implemented
                if stats.get_lives() > 0:
                   callback.on_next(TRY_AGAIN) 
                else:
                   callback.on_next(GAME_OVER)