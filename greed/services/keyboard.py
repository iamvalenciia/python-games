import pyray
from greed.states.point import Point

class Keyboard:
    """ Detects player input

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """
    def __init__(self, cell_size = 1):
        """Constructs a new Keyboard using the specified cell_size
        Args:
            cell_size (int): the size of a cell in the 2d screen
        """
        self._cell_size = cell_size

    def get_direction(self):
        """Gets direction according to the key pressed
        
        Returns:
            Point: the direction
        """

        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1      

        direction = Point(dx,dy)
        direction = direction.scale(self._cell_size)

        return direction    