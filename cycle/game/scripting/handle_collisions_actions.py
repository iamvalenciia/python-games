import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._collision = "snake"

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        score = cast.get_first_actor("scores")
        snake = cast.get_first_actor("snakes")
        head = snake.get_head()

        if head.get_position().scale(0.1):
            points =+ 1
            head.get_position().scale(1)
            snake.grow_tail(points, constants.GREEN)
            score.add_points(points)

        score2 = cast.get_first_actor("scores2")
        snake2 = cast.get_first_actor("snakes2")
        head2 = snake2.get_head()

        if head2.get_position().scale(0.1):
            points2 =+ 1
            head2.get_position().scale(1)
            snake2.grow_tail(points, constants.RED)
            score2.add_points(points2)


        

        


    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        #When snake collision with their body
        snake = cast.get_first_actor("snakes")
        head = snake.get_segments()[0]
        segments = snake.get_segments()[1:]
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._collision = "snakes"

        #When snake2 collision with their body
        snake2 = cast.get_first_actor("snakes2")
        head2 = snake2.get_segments()[0]
        segments2 = snake2.get_segments()[1:]
        
        for segment2 in segments2:
            if head2.get_position().equals(segment2.get_position()):
                self._is_game_over = True
                self._collision = "snakes2"

        #When the snakes collision with the enemy
        for segment2 in segments2:
            if head.get_position().equals(segment2.get_position()):
                self._is_game_over = True
                self._collision = "snakes"

        for segment in segments:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._collision = "snakes2"


        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """


        if self._is_game_over:

            if self._collision == "snakes":
                snake = cast.get_first_actor("snakes")
            else:
                snake = cast.get_first_actor("snakes2")

            segments = snake.get_segments()
            food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)