from constants import *
from game.scripting.action import Action


class DrawCarsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        cars = cast.get_actors(CAR_GROUP)
        #self._video_service.draw_actors(cars)
        
        for car in cars:
            position = car.get_position()
            if car.get_value() == CAR_RIGHT_TEXT:
                self._video_service.draw_text(car, position, CAR_BLUE)
            else:
                self._video_service.draw_text(car, position, CAR_ORANGE)


        