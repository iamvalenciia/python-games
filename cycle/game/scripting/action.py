from game.casting.actor import Actor

class Action:
    """An action that do something important in the game
    method: execute(), which should be overridden by derived classes.
     """
    def execute(self, cast, script):
        """Executes something important in the game.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        pass