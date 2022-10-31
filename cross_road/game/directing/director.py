import random

from game.scripting.action_callback import ActionCallback

from game.shared.point import Point
from game.directing.scene_manager import SceneManager
from game.casting.cast import Cast
from game.scripting.script import Script

from constants import *

class Director(ActionCallback):
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._scene_manager = SceneManager()
        self._score = 0
        self._frame_time = 0
        self._cast = Cast()
        self._script = Script()

    def on_next(self, scene):
        """Overriden ActionCallback method transitions to next scene.
        
        Args:
            A number representing the next scene to transition to.
        """
        self._scene_manager._prepare_scene(scene, self._cast, self._script)
        
    def start_game(self):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """

        self.on_next(NEW_GAME)
        self._execute_actions(INITIALIZE)
        self._execute_actions(LOAD)
        while self._video_service.is_window_open():
            self._execute_actions(INPUT)
            self._execute_actions(UPDATE)
            self._execute_actions(OUTPUT)
        self._execute_actions(UNLOAD)
        self._execute_actions(RELEASE)

    def _get_inputs(self, cast):
         """Gets directional input from the keyboard and applies it to the frog.
        
         Args:
             cast (Cast): The cast of actors.
         """
         frog = cast.get_first_actor("frogs")
         velocity = self._keyboard_service.get_direction()
         frog.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the frog's position and resolves any collisions with cars.
        
        Args:
            cast (Cast): The cast of actors.
        """
        stats = cast.get_first_actor(STATS_GROUP)
        #frog = cast.get_first_actor(FROG_GROUP)
        #cars = cast.get_actors(CAR_GROUP)
        areas = cast.get_areas(AREA_GROUP)

        stats.add_points(self._score)
        
        
        #for car in cars: # here is where the correlation between the cars and score updates and is displayed.
            #car.move_next(max_x, max_y) 

            #car_x = car.get_position().get_x()
            #car_y = car.get_position().get_y()
            #frog_x = frog.get_position().get_x()
            #frog_y = frog.get_position().get_y()

            #This checks if the frog and car are in the same cell instead of a pixel perfect match in position.
            # **************************************************
            # Code below has been moved to CollideCars()
            # **************************************************
            #if ((car_x - FROG_COLLISION) <= frog_x <= (FROG_COLLISION + car_x)) and (car_y == frog_y): 
            #    self._score += car.get_points()
            #    random_x = random.randint(0, max_x)
            #    random_y = random.randint(0, max_y)
            #    position = Point(random_x, random_y)
            #    position = position.scale(15)
            #    car.set_position(position)
            #stats.set_text("Score = " + str(self._score))
               
        
    # def _do_outputs(self, cast):
    #     """Draws the actors on the screen.
        
    #     Args:
    #         cast (Cast): The cast of actors.
    #     """
    #     self._video_service.clear_buffer()
    #     actors = cast.get_all_actors()
    #     areas = cast.get_all_areas()
        
    #     self._video_service.draw_areas(areas)
    #     self._video_service.draw_actors(actors)
    #     self._video_service.flush_buffer()

    def _execute_actions(self, group):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = self._script.get_actions(group)    
        for action in actions:
            action.execute(self._cast, self._script, self) 

        # self._video_service.clear_buffer()
        # actors = self._cast.get_all_actors()
        # areas = self._cast.get_all_areas()

        # self._video_service.draw_areas(areas)
        # self._video_service.draw_actors(actors)
        # self._video_service.flush_buffer()