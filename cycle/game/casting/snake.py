import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._color_snake = constants.WHITE
        self._segments = []

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        # when pres_key w = move
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments, player_color):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(player_color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)

    #here to edit the position also..
    def prepare_body(self,color_snake,position_y):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)


        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, position_y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "@" if i == 0 else "#"

            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_color(color_snake)
            segment.set_text(text)
            self._segments.append(segment)
    


    
            