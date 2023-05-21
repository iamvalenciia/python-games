import constants

from game.casting.score import Score
from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.snake import Snake
from game.directing.director import Director
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.handle_collisions_actions import HandleCollisionsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.script import Script
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point

WHITE = Color(255, 255, 255)

def main():

    #create the cast
    cast = Cast()

    #snakes
    snake = Snake()
    snake.prepare_body(constants.GREEN, 150)
    snake.grow_tail(5, constants.GREEN)
    cast.add_actor("snakes", snake)

    snake2 = Snake()
    snake2.prepare_body(constants.RED, 450)
    snake2.grow_tail(5, constants.RED)
    cast.add_actor("snakes2", snake2)

    #Scores
    score = Score()
    score.set_color(Color(0, 255, 0))
    cast.add_actor("scores", score)

    score2 = Score()
    score2.set_position(Point(800,600))
    score2.set_color(Color(255, 0, 0))
    cast.add_actor("scores2", score2)


    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()

    
