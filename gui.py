import tkinter as tk
from wordle import Wordle  


class WordleGUI:
    def __init__(self, master, all_words_file):
        self.master = master
        self.master.title("Anson's Wordle Clone")
        self.all_words_file = all_words_file

        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        """
        Create the Wordle grid, message, and on-screen keyboard.
        """

        self.grid_frame = tk.Frame(self.master, padx=20, pady=20)
        self.grid_frame.grid(row=0, column=0, columnspan=5)

        self.labels = [[tk.Label(self.grid_frame, text=" ", width=4, height=2,
                                 font=("Helvetica", 24), borderwidth=2, relief="solid")
                        for i in range(5)] for j in range(6)]

        for r in range(6):
            for c in range(5):
                self.labels[r][c].grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

        for r in range(6):
            self.grid_frame.rowconfigure(r, weight=1)
        for c in range(5):
            self.grid_frame.columnconfigure(c, weight=1)

    
        self.message = tk.Label(self.master, text="", font=("Helvetica", 14))
        self.message.grid(row=1, column=0, columnspan=5, pady=(5, 10))

        
        self.keyboard_frame = tk.Frame(self.master)
        self.keyboard_frame.grid(row=2, column=0, columnspan=5, pady=10, sticky="we")

        self.keys = {}
        total_columns = 20 

        first_row = "QWERTYUIOP"
        for idx, letter in enumerate(first_row):
            key = tk.Button(self.keyboard_frame, text=letter, width=2, height=2,
                            font=("Helvetica", 12), bg="lightgray",
                            command=lambda l=letter.lower(): self.key_pressed(l))
            key.grid(row=0, column=idx*2, columnspan=2, padx=1, pady=2, sticky="we")
            self.keys[letter.lower()] = key

        second_row = "ASDFGHJKL"
        start_col = 1
        for idx, letter in enumerate(second_row):
            key = tk.Button(self.keyboard_frame, text=letter, width=2, height=2,
                            font=("Helvetica", 12), bg="lightgray",
                            command=lambda l=letter.lower(): self.key_pressed(l))
            key.grid(row=1, column=start_col + idx*2, columnspan=2, padx=1, pady=2, sticky="we")
            self.keys[letter.lower()] = key

        enter_button = tk.Button(self.keyboard_frame, text="ENTER", width=4, height=2,
                                 font=("Helvetica", 12), command=self.submit_current_guess)
        enter_button.grid(row=2, column=0, columnspan=4, padx=1, pady=2, sticky="we")

        third_row_letters = "ZXCVBNM"
        for idx, letter in enumerate(third_row_letters):
            key = tk.Button(self.keyboard_frame, text=letter, width=2, height=2,
                            font=("Helvetica", 12), bg="lightgray",
                            command=lambda l=letter.lower(): self.key_pressed(l))
            key.grid(row=2, column=4 + idx*2, columnspan=2, padx=1, pady=2, sticky="we")
            self.keys[letter.lower()] = key

        back_button = tk.Button(self.keyboard_frame, text="⌫", width=4, height=2,
                                font=("Helvetica", 12), command=self.delete_last_letter)
        back_button.grid(row=2, column=18, columnspan=4, padx=1, pady=2, sticky="we")

        for col in range(total_columns):
            self.keyboard_frame.columnconfigure(col, weight=1)

    def new_game(self):
        """
        Reset everything for a new game.
        """
        self.game = Wordle(self.all_words_file)
        self.current_attempt = 0
        self.message.config(text="")

        for r in range(6):
            for c in range(5):
                self.labels[r][c].config(text=" ", bg="SystemButtonFace", fg="black")

        for key in self.keys.values():
            key.config(bg="lightgray", fg="black")

    def key_pressed(self, letter):
        """
        Add a letter to the current attempt (max 5 letters).
        """
        for i in range(5):
            if self.labels[self.current_attempt][i].cget("text") == " ":
                self.labels[self.current_attempt][i].config(text=letter.upper())
                break

    def delete_last_letter(self):
        """
        Delete the last letter from the current attempt.
        """
        for i in reversed(range(5)):
            if self.labels[self.current_attempt][i].cget("text") != " ":
                self.labels[self.current_attempt][i].config(text=" ")
                break

    def submit_current_guess(self):
        """
        Submit the current row as a guess.
        """
        guess = "".join([self.labels[self.current_attempt][i].cget("text").lower() for i in range(5)])
        if len(guess) != 5 or not self.game.validguess(guess):
            self.message.config(text="Not in word list")
            return

        feedback = self.game.checkguess(guess)

        for i, letter in enumerate(guess):
            if feedback[i] == 'green':
                self.labels[self.current_attempt][i].config(bg="green", fg="white")
                self.keys[letter].config(bg="green", fg="white")
            elif feedback[i] == 'yellow':
                self.labels[self.current_attempt][i].config(bg="yellow", fg="black")
                if self.keys[letter].cget("bg") != "green":
                    self.keys[letter].config(bg="yellow", fg="black")
            else:
                self.labels[self.current_attempt][i].config(bg="gray", fg="white")
                if self.keys[letter].cget("bg") not in ("green", "yellow"):
                    self.keys[letter].config(bg="gray", fg="white")

        self.current_attempt += 1
        self.message.config(text="")

        result = self.game.game_over(guess)
        if result == "Win":
            self.message.config(
            text=f"🎉✨ You Win! The word was '{self.game.answer}'! 🏆",
            fg="white",
            bg="green",
            font=("Helvetica", 16, "bold")
            )
        elif result == "Lose" or self.current_attempt >= 6:
            self.message.config(
            text=f"😢 Out of attempts! The word was '{self.game.answer}' 😢",
            fg="white",      # text color
            bg="red",        # background color
            font=("Helvetica", 16, "bold")
            )


