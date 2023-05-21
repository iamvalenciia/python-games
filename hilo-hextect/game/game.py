from .card import Card


class Game:

    """
    The responsibility of a Game class is to control the rules of the game, and make it work

    Attributes:
        card(random_number): A random number for the first card
        score(int): The score of the player after the first card
        next_card_value: this will store the new card number
        keep_playing(boolean): To keep playing the game until player stop it
        playersInput(string): this will store the players input, either "h" or "l"
        cardObject(Card): This will store an instance of the card class
    """

    def __init__(self):
        self.card = 0
        self.score = 300
        self.next_card_value = 0
        self.card_value = 0
        self.keep_playing = True
        self.playersInput = ""
        self.cardObject = Card()

    # Starts the game and stops when the while loop gets false
    # Author: Cardona Guzman, RUTH VERONICA
    def start_game(self):
        """Stars the game and stops when the while loop gets false.
        Args: self (Game) an instance of Game.
        """
        
        while self.keep_playing:
            self.show_random_card() 
            self.get_input() #asks player if higher or lower
            self.show_next_card()
            self.get_score()
            self.get_play_again() #asks player if wants to keep playing


    # It will show a random card number from a range of 1 to 13
    # Author: CHEMARIEV, VADYM
    def show_random_card(self):
        """It will It will show a random card
        Args: self (Game) an instance of Game.
        """
        if not self.keep_playing:
            return 

        card = self.cardObject
        card.get_random_card()
        self.card = card.value
        print(f"\nThe card is: {self.card}")

    # It will ask the player if higher(h) or lower(l)
    # Author: Merilus, Rose Berline
    def get_input (self):
        """It will ask the player if higher(h) or lower(l)
        Args: self (Game) an instance of Game.
        """
        if not self.keep_playing:
            return 

        self.playersInput = input("Higher or Lower? [h/l]")

    # It will show a random card
    # Note: you can use the get_random_card() method from the card class
    # Author: Cardona Guzman, RUTH VERONICA
    def show_next_card(self):
        """It will show an additional random card
        Args: self (Game) an instance of Game.
        """
        if not self.keep_playing:
            return 

        card = self.cardObject
        card.get_random_card()
        self.next_card_value = card.value  
        print(f"Next card was: {self.next_card_value}")

    # This will calculate and show the final score based on what the player guessed
    # Author: Juan Valencia
    def get_score(self):
        """It calculate and show the final score
        Args: self (Game) an instance of Game.
        """
        if not self.keep_playing:
            return 


        condition_a = ''
        user_option = ''
        
        if self.card > self.next_card_value:
            condition_a = 'lower'
        elif self.card < self.next_card_value:
            condition_a = 'higher'
        
        if self.playersInput == 'h':
            user_option = 'higher'
        elif self.playersInput == 'l':
            user_option = 'lower'
        
        if condition_a == user_option:
            self.score += 100
        elif condition_a != user_option:
            self.score -= 75

        print(f'Your score is {self.score}')
    
    # This will keep playing or stops the game based in the players input
    # Author: Thierry Alexandre
    def get_play_again(self):

        if not self.keep_playing:
            return 

        user_option = input("play again? [y/n] ")
        self.keep_playing = (user_option == "y")
    
