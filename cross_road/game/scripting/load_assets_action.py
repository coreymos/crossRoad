from pathlib import Path
from game.scripting.action import Action
from constants import *


class LoadAssetsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script, callback):
        self._video_service.load_fonts("cross_road/assets/fonts")

 
