import os
import random
from tkinter import END

from constants import *

from game.casting.actor import Actor
from game.casting.car import Car
from game.casting.cast import Cast


from game.directing.director import Director
from game.directing.scene_manager import SceneManager

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

def main():
    #starts the game
    keyboard_service = KeyboardService(CELL_SIZE)
    
    director = Director(keyboard_service, SceneManager.VIDEO_SERVICE)
    director.start_game()


if __name__ == "__main__":
    main()