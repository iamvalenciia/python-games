import pyray

class Display:
    """ Draw the game outputs on a 2d screen.
    """
    def __init__(self, title, width, height, cell_size, frame_rate, debug = False):
        """Construct a new Display service using the specified debug mode
        
        Args:
        debug (bool): whether ot not to draw in debug mode.
        """
        self._title = title
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._frame_rate = frame_rate
        self._debug = debug

    def close_window(self):
        """Closes the window and releases all computing resources"""
        pyray.close_window()    

    def clear_buffer(self):
        """Clears the buffer for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
    
    def _draw_grid(self):
        """Draw grid on the screen"""
        for y in range(0, self._height, self._cell_size):
            pyray.draw_line(0, y, self._width, y, pyray.GRAY)

        for x in range(0, self._width, self._cell_size):
            pyray.draw_line(x, 0, x, self._height, pyray.GRAY)

    def draw_actor(self, actor):
        """Draws the actor on the screen
        Args:
        actor (actor) The actor to draw"""
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()
        pyray.draw_text(text, x, y, font_size, color)

    def draw_actors(self, actors):
        """Draw all actors on the screen with the given list
        Args: actors (list): the list of actors to draw"""
        for actor in actors:
            self.draw_actor(actor)

    def flush_buffer(self):
        """ Copies the buffer contents to the screen. 
        This method should be called at the end of the game's output phase"""
        pyray.end_drawing()

    def get_cell_size(self):
        """gets the size of each cell on the screen"""
        return self._cell_size

    def get_height(self):
        """gets the height of the screen"""
        return self._height

    def get_width(self):
        """gets the width of the screen"""  
        return self._width

    def is_window_open(self):
        """ Returns True if the windows is closing (the x icon is press) if not returns false.""" 
        return not pyray.window_should_close() 

    def open_window(self):
        """Open a new window with the provided title"""
        pyray.init_window(self._width, self._height, self._title)
        pyray.set_target_fps(self._frame_rate)

