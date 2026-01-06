import tkinter as tk
from gui import WordleGUI

"""""
Starts the wordle game
"""

root = tk.Tk()
game = WordleGUI(root, "all_words.txt")
root.mainloop()

