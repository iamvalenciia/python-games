#Choose a random word hidden from the director and cheks if letter guessed is in the word
# Ruth Cardona
import random
class Word():
    """ A secret word randomly chosen from a list.
    The responsability of Word is choose a random and secret word from a list. If the director's guess is correct, the letter is revealed.
    
    Attributes:
    self._hidden_word (string): random word from a list. 
    self._letter (string): the reaveled letter.
    self._unique_moment (boolean): to prints the anonymus random word at the begin the of program 
    self._reference (array): each letter of the random word is save it in an array
    self._number_letters (int): calculate the number of letter from the random word
    self._guess_map (array): convert the letters into underscores (____) (4 underscores)
    """
    def __init__(self):
        """ Construct a new word.
        Arg: 
        self (Word): and instance of Word.
        """
        self._hidden_word = ""
        # self._reveal_word  = ""
        self._reveal_word  = []


        self._unique_moment = True

        self._reference = list(self._hidden_word)
        self._number_letters = len(self._reference)
        self._guess_map = ['_'] * self._number_letters


        
    def get_word(self):
        """Choose a random and secret word from a list.
        Arg: 
        self (Word): and instance of Word.
        Returns: A word from the list.
        """
        word_list = ["wolf", "paper", "fence", "guitar", "autumn", "symphony", "rabbit", "dragonfly", 
        "oil", "morning", "clock", "photography", "notebook", "heart", "prophet", "temple", "ballon", 
        "astronomy", "eggs", "milk", "bear", "ladybug", "owl", "winter", "mozart", "keyboard", "inteligence",
        "water", "light", "bedroom", "cat", "dog", "doll", "thunder", "moon", "bateries", "hippocampus", "sun"]
       
        self._hidden_word = random.choice(word_list)
        return self._hidden_word

    
    def reveal_letter(self, letter):
        """analyze the input of the user with the random word
        and update the status of the random word.
        Arg: 
        self (Word): and instance of Word.
        letter (string input): The letter given by the player
        """
        seperator = ' '

        for reference_index, let in enumerate(self._reference):
            if let == letter:
                self._guess_map[reference_index] = letter
    
        self._reveal_word = seperator.join(self._guess_map)
        self.false_keep_playing()

        
    def get_letters(self):
        """Return the complete word with underscore and letters.
        Arg: 
        self (Word): and instance of Word.
        """
        #this is to create the random word and return the correct number of underscores
        if self._unique_moment:

            self.get_word()                                         #select a random word from the list
            self.underscore_word()                                  #this function convert the random word into underscores
            self._unique_moment = False
            # print(self._reveal_word)                             
            return  self._reveal_word           


        return self._reveal_word

    
    def underscore_word(self):
        """at the begin of the program convert the random word
        in the correct number of underscores.

        Arg: 
        self (Word): and instance of Word.
        Returns: A word from the list.
        """
        self._reference = list(self._hidden_word)
        self._number_letters = len(self._reference)
        self._guess_map = ['_'] * self._number_letters
        seperator = ' '

        self._reveal_word = seperator.join(self._guess_map)

        
    def false_keep_playing(self):
        """condition to end the game if the payers guess the word: 
        self (Word): and instance of Word.
        """
        random_word = self._reference[:]            # self._reference is the entire random word

        if self._guess_map == random_word :         # self._guess_map are the updates from each time the user guess a letter
            return True
            
