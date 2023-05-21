from greed.actors.actor import Actor

class Rocks(Actor):

    """The responsibility of the rocks is to generate rocks and return score
    
    Attributes:
        score: The description about the rocks."""

    def _init_(self, score):
        super()._init_(score)

        self._score =  ""

    def get_score(self):

        """Gets the rocks's score.
        
        Returns:
            The score. """
        return self._score

    def set_score(self, score):
        """Set the score .
        
        Args:
            score: The given score.
        """
        self._score = score
    
    