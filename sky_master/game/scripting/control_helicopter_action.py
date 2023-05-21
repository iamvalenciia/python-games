from constants import *
from game.scripting.action import Action


class ControlHelicopterAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        helicopter = cast.get_first_actor(HELICOPTER_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            helicopter.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            helicopter.swing_right()
        elif self._keyboard_service.is_key_down(UP): 
            helicopter.swing_up()  
        elif self._keyboard_service.is_key_down(DOWN): 
            helicopter.swing_down()    
        else: 
            helicopter.stop_moving()        