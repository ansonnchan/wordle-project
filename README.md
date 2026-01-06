# Wordle Clone

A desktop implementation of the classic **Wordle** game, built from scratch in **Python** with a graphical user interface using the **Tkinter** library.  
This project demonstrates object-oriented programming, game state management, and GUI development.

---

## Features

- 5-letter Wordle gameplay with 6 attempts
- Interactive Tkinter-based graphical interface
- On-screen keyboard with real-time color feedback
- Validation of guesses against a dictionary of valid words
- Clear separation between backend game logic and frontend UI

---

## Word List

The `all_words.txt` file contains a comprehensive list of valid five-letter English words, including less commonly used or archaic terms (e.g., *"aahed"*).  
As a result, some answers may appear uncommon, but are still considered valid dictionary words.

The word list used in this project was sourced from the public GitHub Gist **dracos/valid-wordle-words.txt** and is used here for educational purposes.

---

## Requirements

- Python 3.x
- Tkinter (generally included with standard Python installations)

---

## How to Run

1. Clone the repository
2. Navigate to the project directory
3. Run `python main.py`

---

## What I Learned

- Structuring a project with clear separation between logic and UI
- Managing game state and user input in a GUI application
- Applying object-oriented programming principles in Python
- Building interactive desktop applications using Tkinter

---

## Future Improvements

- Separate word lists for common words (answers) and all valid words (guess validation)
- Support for physical keyboard input
- Restart/new game button
- Game statistics (win rate, streaks, attempt distribution)
- Unit tests for backend game logic
- Animations (e.g. tile flip animations when guessing) 
