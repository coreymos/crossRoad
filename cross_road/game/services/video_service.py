import os
import pathlib
import pyray
from constants import *
from game.shared.color import Color
from game.casting.text import Text
from game.shared.point import Point


class VideoService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, caption, width, height, cell_size, frame_rate, debug = True):
        """Constructs a new VideoService using the specified debug mode.
        
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._caption = caption
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._frame_rate = frame_rate
        self._debug = debug
        self._fonts = {}
        self._textures = {}

    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()

    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
    
    def draw_actor(self, actor):
        """Draws the given actor's text on the screen.

        Args:
            actor (Actor): The actor to draw.
        """ 
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()
        pyray.draw_text(text, x, y, font_size, color)

    def draw_area(self, area):
        """Draws the given area on the screen.

        Args:
            area (Area): The actor to draw.
        """
        x = area.get_position().get_x()
        y = area.get_position().get_y()
        w = area.get_width()
        h = area.get_height()
        color = area.get_color().to_tuple()
        pyray.draw_rectangle(x, y, w, h, color)
        
    def draw_actors(self, actors):
        """Draws the text for the given list of actors on the screen.

        Args:
            actors (list): A list of actors to draw.
        """ 
        for actor in actors:
            self.draw_actor(actor)

    def draw_areas(self, areas):
        """Draws the areas for the given list of areas on the screen.

        Args:
            areas (list): A list of areas to draw.
        """
        for area in areas:
            self.draw_area(area)
    
    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        pyray.end_drawing()

    def get_cell_size(self):
        """Gets the video screen's cell size.
        
        Returns:
            Grid: The video screen's cell size.
        """
        return self._cell_size

    def get_height(self):
        """Gets the video screen's height.
        
        Returns:
            Grid: The video screen's height.
        """
        return self._height

    def get_width(self):
        """Gets the video screen's width.
        
        Returns:
            Grid: The video screen's width.
        """
        return self._width

    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        pyray.init_window(self._width, self._height, self._caption)
        pyray.set_target_fps(self._frame_rate)

    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0, self._height, 30): #This draws the road lines
            pyray.draw_line(0, y, self._width, y, pyray.GRAY)
        #for x in range(0, self._width, self._cell_size):
            #pyray.draw_line(x, 0, x, self._height, pyray.GRAY)

    def release(self):
        pyray.close_window()

    def load_fonts(self, directory):
        filepaths = self._get_filepaths(directory, [".otf", ".ttf"])
        for filepath in filepaths:
            if filepath not in self._fonts.keys():
                font = pyray.load_font(filepath)
                self._fonts[filepath] = font

    def unload_fonts(self):
        for font in self._fonts.values():
            pyray.unload_font(font)
        self._fonts.clear()

    def _get_filepaths(self, directory, filter):
        filepaths = []
        for file in os.listdir(directory):
            filename = os.path.join(directory, file)
            extension = pathlib.Path(filename).suffix.lower()
            if extension in filter:
                filename = str(pathlib.Path(filename))
                filepaths.append(filename)
        return filepaths

    def _to_raylib_color(self, color):
        r, g, b, a = color.to_tuple()
        return pyray.Color(r, g, b, a)

    def draw_text(self, text, position, color):
        filepath = text.get_fontfile()
        # fixed os dependent filepath
        filepath = str(pathlib.Path(filepath))
        value = text.get_value()
        size = text.get_size()
        spacing = 0
        alignment = text.get_alignment()
        tint = self._to_raylib_color(color)

        font = self._fonts[filepath]
        text_image = pyray.image_text_ex(font, value, size, spacing, tint)
        
        x = position.get_x()
        y = position.get_y()

        if alignment == ALIGN_CENTER:
            x = (position.get_x() - text_image.width / 2) 
            # y = (position.get_y() - text_image.height / 2)
        elif alignment == ALIGN_RIGHT:
            x = (position.get_x() - text_image.width) 

        raylib_position = pyray.Vector2(x, y)
        pyray.draw_text_ex(font, value, raylib_position, size, spacing, tint)
    

