from game.scripting.action import Action

class MoveActorsAction(Action):
    
    def __init__(self):
        """Construct a new MoveActorsAction"""

    def execute(self, cast, script):
        """executes the move actors action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        actors = cast.get_all_actors()

        for actor in actors:
            actor.move_next()