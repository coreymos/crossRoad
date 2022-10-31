from turtle import position
from constants import * 
from game.shared.point import Point
import random
import pyray as rl


class Text:
    """A text message."""

    def __init__(self, value, fontfile = FONT_FILE, size = FONT_LARGE, alignment = ALIGN_LEFT):
        """Constructs a new Text."""
        self._value = value
        self._fontfile = fontfile
        self._size = size
        self._alignment = alignment
        self._position = None
        self._velocity = Point(1, 0)
        self._cooldown = False
        self._frame_time = 0
        

    def get_alignment(self):
        """Gets the alignment for the text.
        
        Returns:
            A number representing the text alignment.
        """
        return self._alignment

    def get_fontfile(self):
        """Gets the font file for the text.
        
        Returns:
            A string containing the font file.
        """
        return self._fontfile

    def get_size(self):
        """Gets the font size of the text.
        
        Returns:
            A number representing the font size.
        """
        return self._size

    def get_value(self):
        """Gets the text's value.
        
        Returns:
            A string containing the text's value.
        """
        return self._value

    def set_value(self, value):
        """Sets the text's value.
        
        Args:
            A string containing the text's value.
        """
        self._value = value

    def set_position(self, position):
        self._position = position

    def get_position(self):
        return self._position

    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        """
        if self._value == CAR_RIGHT_TEXT:
            x = (self._position.get_x() + self._velocity.get_x()) % MAX_X
        elif self._value == CAR_LEFT_TEXT:
            x = (self._position.get_x() - self._velocity.get_x()) % MAX_X

        y = (self._position.get_y())

        self._position = Point(x, y)

    def set_velocity(self, velocity):
        self._velocity = velocity

    def get_velocity(self):
        return self._velocity

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
