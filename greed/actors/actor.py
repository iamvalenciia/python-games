from greed.states.color import Color
from greed.states.point import Point

class Actor:
    """The responsibility of Actor is to keep track of its appearance, position.


     Attributes:
        _Image : The image to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """
    def __init__(self):
        
        self._score = ""
        self._text = ""
        self._font_size = 25
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_score(self):
        """Gets the actor's  score
        
        Returns:
            The actor's score "
        """
        return self._score

    def get_text(self):
        """Gets the actor's textual representation.
        
        Returns:
            string: The actor's textual representation.
        """
        return self._text


    def get_font_size(self):
        """Gets the actor's font size.
        
        Returns:
            Point: The actor's font size.
        """
        return self._font_size
    
    def get_color(self):

        """Gets the actor's  colors or better symbo 
        
        Returns:
            Color: The actor's image color.
        """
        return self._color

    def get_position(self):
        """gets actor's position"""
        return self._position

    def move_next(self, max_x, max_y):
        """ move left or right according to the velocity. 
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)
    
    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity

    
    def set_score(self, score):
        """Set score to the given value.
        
        Args:
            score: The given value.
        """
        self._score = score

    def set_text(self, text):
        """Set the text to the given value.
        
        Args:
            text: The given value.
        """
        self._text = text

    def set_font_size(self, font_size):
        """Set the font size
        
        Args:
            font_size : The given font size.
        """
        self._font_size = font_size

    def set_color(self, color):
        """Set the color .
        
        Args:
            color (Color): The given color.
        """
        self._color = color

    def set_position(self, position):
        """Set the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position

    def set_velocity(self, velocity):
        """Set the velocity.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity

    

    