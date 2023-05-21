# Author: Vadym Chemariev

class Jumper:
    """The Jumper drawing. 
    
    The responsibility of the Jumper is to cut a line on the player's of parachute if the director's guess is incorrect.
        
    """
    def __init__(self):
        self._game_over = False
        self._parachute_graphic = self.__get_parachute_graphic()
        

    #This returns from the _game_over  attribute its value
    def get_game_over_value(self):
        return self._game_over
    
    #This returns from the _parachute_graphic  attribute its value
    def get_parachute_graphic(self):
        return self._parachute_graphic

    #This returns the parachute graphic        
    def __get_parachute_graphic(self):
        # return "\n  ___ \n /___\\\n \   /\n  \ /\n   0\n  /|\\\n  / \\\n^^^^^^^^^^^\n"
        
        return ["  ___ "," /___\\"," \   /","  \ /","   0","  /|\\","  / \\"] 

    #This checks if the player guesses a letter or not
    def check_input_letter(self,letter,hiddenWord):
        guessed = False
        self.__get_parachute_graphic()
        wordStr = hiddenWord._hidden_word
        for index in range(len(wordStr)):
            if wordStr[index] == letter:
                # self.__set_letter_in_list(index,letter,hiddenWord)
                guessed = True

        self.__update_players_parachute(guessed)    
    #This stores a letter in a list
    # def __set_letter_in_list(self,index,letter,hiddenWord):
    #     hiddenWord = hiddenWord._reveal_word
    #     # if hiddenWord[index] == "_":
    #     #     hiddenWord[index] = letter
    
    #This cuts a line on the player's parachute.
    def __update_players_parachute(self,guessed):
        if not guessed:
            if self._parachute_graphic[0] == "   0":
                self._parachute_graphic[0] = "   x"
                self._game_over = True
            else:
                del self._parachute_graphic[0]
    #This checks if the list of "_" is full of letters
    def check_empty_word_is_full(self,hiddenWord):
        count = 0
        for i in hiddenWord:
            if i != "_":
                count += 1
        if  len(hiddenWord) == count:
            return True