import random
import os 

class Wordle:
    """
    Backend class for Wordle game logic 
    Handles game state, guess checking, and loading answer 
    """
    
    def __init__ (self, all_words_file, max_attempts=6):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, all_words_file)

        with open(file_path, "r") as file:
            self.word_list = [line.strip().lower() for line in file]

        self.max_attempts = max_attempts
        self.answer = random.choice(self.word_list)
        self.attempts = 0


    def checkguess (self, guess) :
        """
        Matches user's guess with answer 
            - Returns 'green' if letter is in correct spot
            - Returns 'yellow' if answer contains letter but not in correct spot
            - Returns 'gray' if answer doesn't contain letter
        """

        feedback = []
        for i in range(5) :
            if guess[i] == self.answer[i] :
                feedback.append('green')
            elif guess[i] in self.answer :
                feedback.append('yellow')
            else :
                feedback.append('gray')
        self.attempts += 1
        return feedback 
    

    def validguess (self, guess) :
        return guess in self.word_list
    

    def game_over (self, guess) :
        """
        Checks game state 
            - Returns 'Win', 'Lose' or None if game is still in progress 
        """
        if self.attempts >= self.max_attempts :
            return 'Lose'
        elif guess == self.answer :
            return 'Win'
        else :
            return None 
