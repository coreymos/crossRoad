import pyray
from game.shared.point import Point


class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self, cell_size = 1):
        """Constructs a new KeyboardService using the specified cell size.
        
        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._cell_size = cell_size
        self._keys = {}
        self._keys["left"] = pyray.KEY_LEFT
        self._keys["right"] = pyray.KEY_RIGHT
        self._keys["up"] = pyray.KEY_UP
        self._keys["down"] = pyray.KEY_DOWN
        self._keys["enter"] = pyray.KEY_ENTER
        self._keys["space"] = pyray.KEY_SPACE

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.
        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1
        if pyray.is_key_down(pyray.KEY_UP):
            dy = -1
        if pyray.is_key_down(pyray.KEY_DOWN):
            dy = 1

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction

   
        

    def is_key_down(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_down(raylib_key)
    
    def is_key_pressed(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_pressed(raylib_key)
    
    def is_key_released(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_released(raylib_key)
    
    def is_key_up(self, key):
        raylib_key = self._keys[key.lower()]
        return pyray.is_key_up(raylib_key)