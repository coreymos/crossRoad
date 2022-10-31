from re import X
from turtle import position
import pyray

from game.shared.color import Color
from game.shared.point import Point
from game.casting.actor import Actor

class Area(Actor):
    """A visible, area that participates in the game. 
        
        The responsibility of Area is to keep track of its appearance of areas.
        """
    def __init__(self):
        
        self._position = Point(0,0)
        self.width = 0
        self.height = 0
        self._color = Color(0,0,0)

    def get_position(self):
        return self._position

    def set_position(self, x, y):
        position = Point(x, y)  
        self._position = position

    def get_width(self):
        return self._width

    def set_width(self, width):
        
        self._width = width
    
    def get_height(self):
        return self._height

    def set_height(self, height):  
        self._height = height

    def set_color(self, color):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._color = color

    def get_color(self):
        """Gets the actor's color as a tuple of three ints (r, g, b).
        
        Returns:
            Color: The actor's text color.
        """
        return self._color
        