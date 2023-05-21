from constants import *
from game.scripting.action import Action


class DrawHelicopterAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        helicopter = cast.get_first_actor(HELICOPTER_GROUP)
        body = helicopter.get_body()

        if helicopter.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = helicopter.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)