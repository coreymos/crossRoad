from constants import *

class DrawAreasAction ():

    def __init__(self, video_service):
        self._video_service = video_service
    def execute(self, cast, script, callback):
        areas = cast.get_areas(AREA_GROUP)
        self._video_service.draw_areas(areas)
