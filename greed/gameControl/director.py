from greed.states.point import Point
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with gems or rocks.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        gems = cast.get_actors("gems")
        rocks = cast.get_actors("rocks")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        banner.set_text(f'Score: {self._score}')
        
        for gem in gems:
            #gems fall from the top of the screen
            x = gem.get_position().get_x()
            y = gem.get_position().get_y() + 3
            gem.set_position(Point(x, y))

            #if robot catch a gem, score += 1
            if robot.get_position().equals(gem.get_position()):
                self._score += 1
                x = gem.get_position().get_x()
                y = 0
                gem.set_position(Point(x, y))
            
            #create a loop in the screen
            if robot.get_position().get_y() == (gem.get_position().get_y()):
                x = gem.get_position().get_x()
                y = 0
                gem.set_position(Point(x, y))
            
        for rock in rocks:
            #rocks fall from the top of the screen
            x = rock.get_position().get_x()
            y = rock.get_position().get_y() + 3
            rock.set_position(Point(x, y))

            #if robot catch a rock, score -= 1
            if robot.get_position().equals(rock.get_position()):
                self._score -= 1
                x = rock.get_position().get_x()
                y = 0
                rock.set_position(Point(x, y))

            #create a loop in the screen
            if robot.get_position().get_y() == (rock.get_position().get_y()):
                x = rock.get_position().get_x()
                y = 0
                rock.set_position(Point(x, y))

                 
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()