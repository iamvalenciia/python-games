from greed.actors.actor import Actor

class Gems(Actor):

    """The responsibility of the gems is to provide the score
    
    Attributes:
        score: The description about the gems."""

    def _init_(self, score):
        super()._init_(score)

        self._score =  ""

    def get_score(self):

        """Gets the gems's score.
        
        Returns:
            The score. """
        return self._score

    def set_score(self, score):
        """Set the score .
        
        Args:
            score: The given score.
        """
        self._score = score

