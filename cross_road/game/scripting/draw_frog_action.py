from constants import *
from game.scripting.action import Action


class DrawFrogAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        frog = cast.get_first_actor(FROG_GROUP)
        #self._video_service.draw_actor(frog)
        position = frog.get_position()
        self._video_service.draw_text(frog, position, FROG_GREEN)
