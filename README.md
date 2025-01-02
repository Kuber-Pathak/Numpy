# Connect 4 Game

A graphical implementation of the classic **Connect 4** game using numpy and Pygame.

## About the Project

This project is a digital version of the popular Connect 4 board game. It features:
- A **graphical user interface (GUI)** using Pygame.
- Two-player mode with alternating turns.
- Visual indicators for player actions.
- Win detection for horizontal, vertical, and diagonal connections.

---

## Installation

### Prerequisites
Ensure you have Python 3.6+ installed. Additionally, you'll need the following Python libraries:
- `pygame`
- `numpy`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/connect4-game.git
   cd connect4-game
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Linux/macOS
   venv\Scripts\activate      # On Windows
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
## How to Run
1. Start the game by running:
   ```bash
   python connect4.py
   
## Gameplay
- The game alternates between Player 1 (red) and Player 2 (yellow).
- The objective is to connect four pieces in a row, either horizontally, vertically, or diagonally.
- The game announces the winner when a player achieves this.

## Deactivating the Virtual Environment
- If you have activated a virtual environment, you can deactivate it by running:
  ```bash
  deactivate

## Built With
- **Python** - The programming language used.
- **Pygame** - For the graphical interface.
- **NumPy** - For efficient board management.

## Acknowledgments
This project is based on the tutorial by **Keith Galli**.
The code and logic were directly implemented as demonstrated in their video: https://www.youtube.com/watch?v=UYgyRArKDEs&list=PLFCB5Dp81iNV_inzM-R9AKkZZlePCZdtV

