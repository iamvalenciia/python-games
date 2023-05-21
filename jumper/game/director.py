
from .terminal_service import TerminalService
from .jumper import Jumper
from .hidden_word import Word


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _jumperObject(class): save the class jumper
        _wordObject(class): save the class Word
        _tsObject(class): For getting and displaying information on the terminal
        _keep_playing (boolean): To keep playing the game until player stop it
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumperObject = Jumper()
        self._wordObject= Word()
        self._tsObject = TerminalService()
        self._keep_playing = True
       

    # Starts the game and stops when the while loop gets false
    # Author: Rose Merilus
    def start_game(self):
        while self._keep_playing:
            self._do_outputs()
            self._do_inputs()
            self._do_updates()

    #Ouputs
    #Author: Juan Valencia
    def _do_outputs(self):
        """provide the updates of the hiden word and the status of the parachutes.

        Args:
            self (Director): An instance of Director.
        """
        hiden_word_status = self._wordObject.get_letters()
        # jumper_status = self._jumperObject.get_parachute_graphic()
        self._tsObject.write_text(hiden_word_status)
        # self._tsObject.write_text(jumper_status)
        self._tsObject.display_parachute_graphic(self._jumperObject._parachute_graphic)


    # Inputs
    # Author: Ruth Cardona
    def _do_inputs(self):
        """ Call to show parachute graphic and receive a letter from the player.
        Args:
            self (Director): an instance of Director.
        """
       
        #show parachute
        #this two lines in _do_outputs

        #read letter
        # input_letter = self._tsObject.read_text("\n Guess a letter (a-z): ")
        self._letter = self._tsObject.read_text("\n Guess a letter (a-z): ")
        self._wordObject.reveal_letter(self._letter) #analyze the input letter with the ranodm word
        

    #Update
    # Author: Juan Valencia
    def _do_updates(self):
        """calculate the conditions to end the game.

        Args:
            self (Director): An instance of Director.
        """

        self._jumperObject.check_input_letter(self._letter,self._wordObject)

                # I am still working on this...
        # more code here..
        # if self._jumperObject.get_game_over_value() == True:
        if self._jumperObject._game_over:
            self._tsObject.write_text("Game over!!")
            self._keep_playing = False
        

        #In case the player guess the word
        condition = self._wordObject.false_keep_playing()
        if condition == True:
            self._keep_playing = False
            hiden_word_status = self._wordObject.get_letters()
            # jumper_status = self._jumperObject.get_parachute_graphic()
            self._tsObject.write_text(hiden_word_status)
            # self._tsObject.write_text(jumper_status)
            self._tsObject.display_parachute_graphic(self._jumperObject._parachute_graphic)
            self._tsObject.write_text('You Win')

    