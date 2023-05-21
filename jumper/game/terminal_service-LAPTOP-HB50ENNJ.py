#Author Rose Merilus

class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """

    def read_text(self,prompt):

        return input(prompt)

    def read_letter(self, prompt):
        """Gets letter input from the terminal. Directs the user with the given prompt.

        Args:
            self (TerminalService): An instance of TerminalService.
            prompt(string): The prompt to display on the terminal.

        Returns:
            str.isalpha: The user's input as a letter.
        """
        return str.isalpha(input(prompt))

    def write_text(self, text):
        """Displays the given text on the terminal.


        Args:
           self(TerminalService): An instance of Terminal Service.
           text(string): The text to display.
           
        """
        print(text)
        print()
    def display_parachute_graphic(self,parachute):
        
        for i in parachute:
            print(i)
