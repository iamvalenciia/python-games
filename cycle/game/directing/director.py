class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to Controls every part of the game.

    Attributes:
        _video_service (VideoService): For providing video output.
    """
    def __init__(self, video_service):
        """ Director using the specified video service.
        
        """
        self._video_service = video_service
        
    def start_game(self, cast, script):
        """ Runs the main loop for the game.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
           
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            self._execute_actions("output", cast, script)
        self._video_service.close_window()

    def _execute_actions(self, group, cast, script):
        """Calls execute for each action in the given group.
        
        """
        actions = script.get_actions(group)    
        for action in actions:
            action.execute(cast, script)          