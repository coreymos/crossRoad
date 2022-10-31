from game.shared.color import Color
from game.shared.point import Point
from game.casting.actor import Actor
from constants import *

class Car(Actor):
    """a four-wheeled road vehicle that is powered by an engine and is able to carry a small number of people.
    """
    
    def __init__(self):
        super().__init__()
        self.__points = ""
        self.__points = 1 if self._text == "*" else -1 # Here is where the math is being created for each one of the Gems and Rocks.


    #def get_points(self):
    #    return self.__points

    #def set_points(self, points):
    #     self.__points = points

    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        """
        if self._text == CAR_RIGHT_TEXT:
            x = (self._position.get_x() + self._velocity.get_x()) % MAX_X
        elif self._text == CAR_LEFT_TEXT:
            x = (self._position.get_x() - self._velocity.get_x()) % MAX_X

        y = (self._position.get_y())

        self._position = Point(x, y)
    
