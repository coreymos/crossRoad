import os
import random
from this import d
from tkinter import END

from constants import *


from game.casting.actor import Actor
from game.casting.car import Car
from game.casting.cast import Cast
from game.casting.area import Area
from game.casting.frog import Frog
from game.casting.stats import Stats
from game.casting.text import Text
from game.casting.label import Label

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.scripting.initialize_device_action import InitializeDevicesAction
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_cars_action import DrawCarsAction
from game.scripting.draw_frog_action import DrawFrogAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_areas_action import DrawAreasAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.collide_cars_action import CollideCarsAction
from game.scripting.collide_end_area_action import CollideEndAreaAction
from game.scripting.move_frog_action import MoveFrogAction
from game.scripting.move_car_action import MoveCarAction
from game.scripting.control_frog_action import ControlFrogAction


from game.shared.color import Color
from game.shared.point import Point

class SceneManager():
    """The person in charge of setting up the cast and script for each scene."""
    VIDEO_SERVICE = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    KEYBOARD_SERVICE = KeyboardService()

    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(VIDEO_SERVICE)
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(VIDEO_SERVICE)

    COLLIDE_CARS_ACTION = CollideCarsAction()
    COLLIDE_END_AREA_ACTION = CollideEndAreaAction()

    CONTROL_FROG_ACTION = ControlFrogAction(KEYBOARD_SERVICE)

    MOVE_FROG_ACTION = MoveFrogAction()
    MOVE_CAR_ACTION = MoveCarAction()

    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    DRAW_FROG_ACTION = DrawFrogAction(VIDEO_SERVICE)
    DRAW_CARS_ACTION = DrawCarsAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_AREAS_ACTION = DrawAreasAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)

    def __init__(self):
        pass
    
    def _prepare_scene (self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)

    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------

    def _prepare_new_game (self, cast, script):
        
        self._add_end_area(cast)
        self._add_start_area(cast)
        self._add_stats(cast)
        self._add_lives(cast)
        self._add_score(cast)
        self._add_frog(cast)
        self._add_cars(cast)
        
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)

    def _prepare_next_level(self, cast, script):

        self._add_dialog(cast, PREP_TO_LAUNCH)
        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        
    def _prepare_try_again(self, cast, script):

        self._add_frog(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        # This resets the frog's velocity after hitting a car
        self._reset_frog(cast)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):

        cast.clear_actors(DIALOG_GROUP)
        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_FROG_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)
        

    def _prepare_game_over(self, cast, script):
        self._add_frog(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)
        

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
        
    def _add_frog(self, cast):
        position = FROG_START
        position.scale(30)
        text = FROG_TEXT
        frog = Text(text, FONT_FILE_FROG, 35)
        frog.set_position(position)
        
        cast.add_actor(FROG_GROUP, frog)

    def _add_cars(self, cast):
        cast.clear_actors(CAR_GROUP)
        for n in range(CAR_AMOUNT):
            text = random.choice([CAR_LEFT_TEXT, CAR_RIGHT_TEXT])
            #if text == CAR_LEFT_TEXT:
            #    points = 1
            #elif text == CAR_RIGHT_TEXT:
            #    points = -1

            x = random.randint(1, COLS - 1)
            y = random.randint(START_HEIGHT_ROAD, END_HEIGHT_ROAD)

            position = Point(x, y)
            position = position.scale(30)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
            
            car = Text(text, FONT_FILE_CAR)
            #car = Car()
            #car.set_text(text)
            #car.set_font_size(FONT_SIZE)
            #car.set_color(color)
            car.set_position(position)
            #car.set_points(points)
            cast.add_actor(CAR_GROUP, car)
            
    
    def _add_end_area(self, cast):
        #adds the end green area
        area = Area()
        area.set_color(GREEN)
        area.set_position(0, 0)
        area.set_width(MAX_X)
        area.set_height(59)
        cast.add_area(AREA_GROUP, area)

    def _add_start_area(self, cast):
        #adds the start green area
        area = Area()
        area.set_color(GREEN)
        area.set_position(0, 541)
        area.set_width(MAX_X)
        area.set_height(100)
        cast.add_area(AREA_GROUP, area)
    
    def _reset_frog(self, cast):
        frog = cast.get_first_actor(FROG_GROUP)
        velocity = Point(0, 0)
        frog.set_velocity(velocity)
    
    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)
    
    # def _add_level(self, cast):
    #     cast.clear_actors(LEVEL_GROUP)
    #     text = Text(LEVEL_FORMAT, FONT_FILE_DEFAULT, FONT_SMALL, ALIGN_LEFT)
    #     position = Point(HUD_MARGIN, HUD_MARGIN)
    #     label = Label(text, position)
    #     cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_AREAS_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_CARS_ACTION)
        
        script.add_action(OUTPUT, self.DRAW_FROG_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_FROG_ACTION)
        script.add_action(UPDATE, self.MOVE_CAR_ACTION)
        script.add_action(UPDATE, self.COLLIDE_CARS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_END_AREA_ACTION)
        #script.add_action(UPDATE, self.CHECK_OVER_ACTION)